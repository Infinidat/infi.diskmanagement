'''comtypes.client - High level client level COM support package.
'''

################################################################
#
# TODO:
#
# - refactor some code into modules
#
################################################################

import sys, os
import ctypes

import comtypes
from comtypes.hresult import *
import comtypes.automation
import comtypes.typeinfo
import comtypes.client.dynamic

from comtypes.client._events import GetEvents, ShowEvents, PumpEvents
from comtypes.client._generate import GetModule

import logging
logger = logging.getLogger(__name__)

__all__ = ["CreateObject", "GetActiveObject", "CoGetObject",
           "GetEvents", "ShowEvents", "PumpEvents", "GetModule",
           "GetClassObject"]

from comtypes.client._code_cache import _find_gen_dir

gen_dir = _find_gen_dir()
import comtypes.gen

### for testing
##gen_dir = None

from comtypes.gen._565783C6_CB41_11D1_8B02_00600806D9B6_0_1_2 import ISWbemObjectEx

def wrap_outparam(punk):
    if not punk:
        return None
    if punk.__com_interface__ == comtypes.automation.IDispatch:
        return punk.QueryInterface(ISWbemObjectEx)
    return punk

def GetBestInterface(punk):
    """Try to QueryInterface a COM pointer to the 'most useful'
    interface.

    Get type information for the provided object, either via
    IDispatch.GetTypeInfo(), or via IProvideClassInfo.GetClassInfo().
    Generate a wrapper module for the typelib, and QI for the
    interface found.
    """
    if not punk: # NULL COM pointer
        return punk # or should we return None?
    # find the typelib and the interface name
    try:
        try:
            pci = punk.QueryInterface(comtypes.typeinfo.IProvideClassInfo)
        except comtypes.COMError:
            # Some COM objects support IProvideClassInfo2, but not IProvideClassInfo.
            # These objects are broken, but we support them anyway.
            pci = punk.QueryInterface(comtypes.typeinfo.IProvideClassInfo2)
        tinfo = pci.GetClassInfo() # TypeInfo for the CoClass
        # find the interface marked as default
        ta = tinfo.GetTypeAttr()
        for index in range(ta.cImplTypes):
            if tinfo.GetImplTypeFlags(index) == 1:
                break
        else:
            if ta.cImplTypes != 1:
                # Hm, should we use dynamic now?
                raise TypeError("No default interface found")
            # Only one interface implemented, use that (even if
            # not marked as default).
            index = 0
        href = tinfo.GetRefTypeOfImplType(index)
        tinfo = tinfo.GetRefTypeInfo(href)
    except comtypes.COMError:
        try:
            pdisp = punk.QueryInterface(comtypes.automation.IDispatch)
        except comtypes.COMError:
            return punk
        try:
            tinfo = pdisp.GetTypeInfo(0)
        except comtypes.COMError:
            pdisp = comtypes.client.dynamic.Dispatch(pdisp)
            return pdisp
    typeattr = tinfo.GetTypeAttr()
    try:
        punk.QueryInterface(comtypes.IUnknown, typeattr.guid)
    except comtypes.COMError:
        return comtypes.client.dynamic.Dispatch(punk)

    itf_name = tinfo.GetDocumentation(-1)[0] # interface name
    tlib = tinfo.GetContainingTypeLib()[0] # typelib

    # import the wrapper, generating it on demand
    mod = GetModule(tlib)
    # Python interface class
    interface = getattr(mod, itf_name)
    # QI for this interface
    # XXX
    # What to do if this fails?
    # In the following example the engine.Eval() call returns
    # such an object.
    #
    # engine = CreateObject("MsScriptControl.ScriptControl")
    # engine.Language = "JScript"
    # engine.Eval("[1, 2, 3]")
    #
    # Could the above code, as an optimization, check that QI works,
    # *before* generating the wrapper module?
    result = punk.QueryInterface(interface)
    return result
# backwards compatibility:
wrap = GetBestInterface

# Should we do this for POINTER(IUnknown) also?
ctypes.POINTER(comtypes.automation.IDispatch).__ctypes_from_outparam__ = wrap_outparam

################################################################
#
# Typelib constants
#
class Constants(object):
    """This class loads the type library from the supplied object,
    then exposes constants in the type library as attributes."""
    def __init__(self, obj):
        obj = obj.QueryInterface(comtypes.automation.IDispatch)
        tlib, index = obj.GetTypeInfo(0).GetContainingTypeLib()
        self.tcomp = tlib.GetTypeComp()

    def __getattr__(self, name):
        try:
            kind, desc = self.tcomp.Bind(name)
        except (WindowsError, comtypes.COMError):
            raise AttributeError(name)
        if kind != "variable":
            raise AttributeError(name)
        return desc._.lpvarValue[0].value

    def _bind_type(self, name):
        return self.tcomp.BindType(name)

################################################################
#
# Object creation
#
def GetActiveObject(progid, interface=None, dynamic=False):
    """Return a pointer to a running COM object that has been
    registered with COM.

    'progid' may be a string like "Excel.Application",
       a string specifying a clsid, a GUID instance, or an object with
       a _clsid_ attribute which should be any of the above.
    'interface' allows to force a certain interface.
    'dynamic=True' will return a dynamic dispatch object.
    """
    clsid = comtypes.GUID.from_progid(progid)
    if dynamic:
        if interface is not None:
            raise ValueError("interface and dynamic are mutually exclusive")
        interface = comtypes.automation.IDispatch
    elif interface is None:
        interface = getattr(progid, "_com_interfaces_", [None])[0]
    obj = comtypes.GetActiveObject(clsid, interface=interface)
    if dynamic:
        return comtypes.client.dynamic.Dispatch(obj)
    return _manage(obj, clsid, interface=interface)

def _manage(obj, clsid, interface):
    obj.__dict__['__clsid'] = str(clsid)
    if interface is None:
        obj = GetBestInterface(obj)
    return obj

def GetClassObject(progid,
                   clsctx=None,
                   pServerInfo=None,
                   interface=None):
    """Create and return the class factory for a COM object.

    'clsctx' specifies how to create the object, use the CLSCTX_... constants.
    'pServerInfo', if used, must be an instance of comtypes.COSERVERINFO
    'interface' may be used to request an interface other than IClassFactory
    """
    clsid = comtypes.GUID.from_progid(progid)
    return comtypes.CoGetClassObject(clsid,
                                     clsctx, pServerInfo, interface)

def CreateObject(progid,                  # which object to create
                 clsctx=None,             # how to create the object
                 machine=None,            # where to create the object
                 interface=None,          # the interface we want
                 dynamic=False):          # use dynamic dispatch
    """Create a COM object from 'progid', and try to QueryInterface()
    it to the most useful interface, generating typelib support on
    demand.  A pointer to this interface is returned.

    'progid' may be a string like "InternetExplorer.Application",
       a string specifying a clsid, a GUID instance, or an object with
       a _clsid_ attribute which should be any of the above.
    'clsctx' specifies how to create the object, use the CLSCTX_... constants.
    'machine' allows to specify a remote machine to create the object on.
    'interface' allows to force a certain interface
    'dynamic=True' will return a dynamic dispatch object

    You can also later request to receive events with GetEvents().
    """
    clsid = comtypes.GUID.from_progid(progid)
    if dynamic:
        if interface:
            raise ValueError("interface and dynamic are mutually exclusive")
        interface = comtypes.automation.IDispatch
    elif interface is None:
        interface = getattr(progid, "_com_interfaces_", [None])[0]
    if machine is None:
        obj = comtypes.CoCreateInstance(clsid, clsctx=clsctx, interface=interface)
    else:
        obj = comtypes.CoCreateInstanceEx(clsid, clsctx=clsctx, interface=interface, machine=machine)
    if dynamic:
        return comtypes.client.dynamic.Dispatch(obj)
    return _manage(obj, clsid, interface=interface)

def CoGetObject(displayname, interface=None, dynamic=False):
    """Create an object by calling CoGetObject(displayname).

    Additional parameters have the same meaning as in CreateObject().
    """
    if dynamic:
        if interface is not None:
            raise ValueError("interface and dynamic are mutually exclusive")
        interface = comtypes.automation.IDispatch
    punk = comtypes.CoGetObject(displayname, interface)
    if dynamic:
        return comtypes.client.dynamic.Dispatch(punk)
    return _manage(punk,
                   clsid=None,
                   interface=interface)

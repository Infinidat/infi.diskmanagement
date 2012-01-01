# -*- coding: mbcs -*-
typelib_path = u'C:\\Windows\\system32\\wbem\\wbemdisp.TLB'
_lcid = 0 # change this if required
from ctypes import *
from comtypes import GUID
from comtypes import CoClass
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import BSTR
from comtypes.automation import IDispatch
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import IUnknown
from ctypes.wintypes import VARIANT_BOOL
from comtypes.automation import VARIANT
from comtypes import DISPMETHOD, DISPPROPERTY, helpstring
from comtypes.automation import VARIANT


class SWbemObjectSet(CoClass):
    u'A collection of Classes or Instances'
    _reg_clsid_ = GUID('{04B83D61-21AE-11D2-8B33-00600806D9B6}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
class ISWbemObjectSet(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A collection of Classes or Instances'
    _iid_ = GUID('{76A6415F-CB41-11D1-8B02-00600806D9B6}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation', 'hidden']
SWbemObjectSet._com_interfaces_ = [ISWbemObjectSet]

class SWbemNamedValue(CoClass):
    u'A named value'
    _reg_clsid_ = GUID('{04B83D60-21AE-11D2-8B33-00600806D9B6}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
class ISWbemNamedValue(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A named value'
    _iid_ = GUID('{76A64164-CB41-11D1-8B02-00600806D9B6}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
SWbemNamedValue._com_interfaces_ = [ISWbemNamedValue]

class SWbemNamedValueSet(CoClass):
    u'A collection of Named Values'
    _reg_clsid_ = GUID('{9AED384E-CE8B-11D1-8B05-00600806D9B6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
class ISWbemNamedValueSet(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A collection of named values'
    _iid_ = GUID('{CF2376EA-CE8C-11D1-8B05-00600806D9B6}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
SWbemNamedValueSet._com_interfaces_ = [ISWbemNamedValueSet]

class ISWbemLocator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Used to obtain Namespace connections'
    _iid_ = GUID('{76A6415B-CB41-11D1-8B02-00600806D9B6}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
class ISWbemServices(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A connection to a Namespace'
    _iid_ = GUID('{76A6415C-CB41-11D1-8B02-00600806D9B6}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
class ISWbemSecurity(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A Security Configurator'
    _iid_ = GUID('{B54D66E6-2287-11D2-8B33-00600806D9B6}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation', 'hidden']
ISWbemLocator._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Connect to a Namespace')], HRESULT, 'ConnectServer',
              ( ['in', 'optional'], BSTR, 'strServer', u'.' ),
              ( ['in', 'optional'], BSTR, 'strNamespace', u'' ),
              ( ['in', 'optional'], BSTR, 'strUser', u'' ),
              ( ['in', 'optional'], BSTR, 'strPassword', u'' ),
              ( ['in', 'optional'], BSTR, 'strLocale', u'' ),
              ( ['in', 'optional'], BSTR, 'strAuthority', u'' ),
              ( ['in', 'optional'], c_int, 'iSecurityFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemServices)), 'objWbemServices' )),
    COMMETHOD([dispid(2), helpstring(u'The Security Configurator for this Object'), 'propget'], HRESULT, 'Security_',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemSecurity)), 'objWbemSecurity' )),
]
################################################################
## code template for ISWbemLocator implementation
##class ISWbemLocator_Impl(object):
##    @property
##    def Security_(self):
##        u'The Security Configurator for this Object'
##        #return objWbemSecurity
##
##    def ConnectServer(self, strServer, strNamespace, strUser, strPassword, strLocale, strAuthority, iSecurityFlags, objWbemNamedValueSet):
##        u'Connect to a Namespace'
##        #return objWbemServices
##


# values for enumeration 'WbemChangeFlagEnum'
wbemChangeFlagCreateOrUpdate = 0
wbemChangeFlagUpdateOnly = 1
wbemChangeFlagCreateOnly = 2
wbemChangeFlagUpdateCompatible = 0
wbemChangeFlagUpdateSafeMode = 32
wbemChangeFlagUpdateForceMode = 64
wbemChangeFlagStrongValidation = 128
wbemChangeFlagAdvisory = 65536
WbemChangeFlagEnum = c_int # enum

# values for enumeration 'WbemImpersonationLevelEnum'
wbemImpersonationLevelAnonymous = 1
wbemImpersonationLevelIdentify = 2
wbemImpersonationLevelImpersonate = 3
wbemImpersonationLevelDelegate = 4
WbemImpersonationLevelEnum = c_int # enum
class Library(object):
    u'Microsoft WMI Scripting V1.2 Library'
    name = u'WbemScripting'
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)


# values for enumeration 'WbemAuthenticationLevelEnum'
wbemAuthenticationLevelDefault = 0
wbemAuthenticationLevelNone = 1
wbemAuthenticationLevelConnect = 2
wbemAuthenticationLevelCall = 3
wbemAuthenticationLevelPkt = 4
wbemAuthenticationLevelPktIntegrity = 5
wbemAuthenticationLevelPktPrivacy = 6
WbemAuthenticationLevelEnum = c_int # enum
class SWbemMethodSet(CoClass):
    u'A collection of Methods'
    _reg_clsid_ = GUID('{04B83D5A-21AE-11D2-8B33-00600806D9B6}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
class ISWbemMethodSet(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A collection of Methods'
    _iid_ = GUID('{C93BA292-D955-11D1-8B09-00600806D9B6}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation', 'hidden']
SWbemMethodSet._com_interfaces_ = [ISWbemMethodSet]

class ISWbemRefresher(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A Collection of Refreshable Objects'
    _iid_ = GUID('{14D8250E-D9C2-11D3-B38F-00105A1F473A}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
class ISWbemRefreshableItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A single item in a Refresher'
    _iid_ = GUID('{5AD4BF92-DAAB-11D3-B38F-00105A1F473A}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
class ISWbemServicesEx(ISWbemServices):
    _case_insensitive_ = True
    u'A connection to a Namespace'
    _iid_ = GUID('{D2F68443-85DC-427E-91D8-366554CC754C}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation', 'hidden']
ISWbemRefresher._methods_ = [
    COMMETHOD([dispid(-4), 'restricted', 'propget'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'pUnk' )),
    COMMETHOD([dispid(0), helpstring(u'Get an item from this refresher')], HRESULT, 'Item',
              ( ['in'], c_int, 'iIndex' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemRefreshableItem)), 'objWbemRefreshableItem' )),
    COMMETHOD([dispid(1), helpstring(u'The number of items in this refresher'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'iCount' )),
    COMMETHOD([dispid(2), helpstring(u'Add a refreshable instance to this refresher')], HRESULT, 'Add',
              ( ['in'], POINTER(ISWbemServicesEx), 'objWbemServices' ),
              ( ['in'], BSTR, 'bsInstancePath' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemRefreshableItem)), 'objWbemRefreshableItem' )),
    COMMETHOD([dispid(3), helpstring(u'Add a refreshable enumerator to this refresher')], HRESULT, 'AddEnum',
              ( ['in'], POINTER(ISWbemServicesEx), 'objWbemServices' ),
              ( ['in'], BSTR, 'bsClassName' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemRefreshableItem)), 'objWbemRefreshableItem' )),
    COMMETHOD([dispid(4), helpstring(u'Remove an item from this refresher')], HRESULT, 'Remove',
              ( ['in'], c_int, 'iIndex' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 )),
    COMMETHOD([dispid(5), helpstring(u'Refresh all items in this collection')], HRESULT, 'Refresh',
              ( ['in', 'optional'], c_int, 'iFlags', 0 )),
    COMMETHOD([dispid(6), helpstring(u'Whether to attempt auto-reconnection to a remote provider'), 'propget'], HRESULT, 'AutoReconnect',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bCount' )),
    COMMETHOD([dispid(6), helpstring(u'Whether to attempt auto-reconnection to a remote provider'), 'propput'], HRESULT, 'AutoReconnect',
              ( ['in'], VARIANT_BOOL, 'bCount' )),
    COMMETHOD([dispid(7), helpstring(u'Delete all items in this collection')], HRESULT, 'DeleteAll'),
]
################################################################
## code template for ISWbemRefresher implementation
##class ISWbemRefresher_Impl(object):
##    @property
##    def Count(self):
##        u'The number of items in this refresher'
##        #return iCount
##
##    @property
##    def _NewEnum(self):
##        '-no docstring-'
##        #return pUnk
##
##    def Remove(self, iIndex, iFlags):
##        u'Remove an item from this refresher'
##        #return 
##
##    def Item(self, iIndex):
##        u'Get an item from this refresher'
##        #return objWbemRefreshableItem
##
##    def Add(self, objWbemServices, bsInstancePath, iFlags, objWbemNamedValueSet):
##        u'Add a refreshable instance to this refresher'
##        #return objWbemRefreshableItem
##
##    def DeleteAll(self):
##        u'Delete all items in this collection'
##        #return 
##
##    def Refresh(self, iFlags):
##        u'Refresh all items in this collection'
##        #return 
##
##    def _get(self):
##        u'Whether to attempt auto-reconnection to a remote provider'
##        #return bCount
##    def _set(self, bCount):
##        u'Whether to attempt auto-reconnection to a remote provider'
##    AutoReconnect = property(_get, _set, doc = _set.__doc__)
##
##    def AddEnum(self, objWbemServices, bsClassName, iFlags, objWbemNamedValueSet):
##        u'Add a refreshable enumerator to this refresher'
##        #return objWbemRefreshableItem
##

class ISWbemObject(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A Class or Instance'
    _iid_ = GUID('{76A6415A-CB41-11D1-8B02-00600806D9B6}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
class ISWbemEventSource(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An Event source'
    _iid_ = GUID('{27D54D92-0EBE-11D2-8B22-00600806D9B6}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation', 'hidden']
ISWbemServices._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Get a single Class or Instance')], HRESULT, 'Get',
              ( ['in', 'optional'], BSTR, 'strObjectPath', u'' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObject)), 'objWbemObject' )),
    COMMETHOD([dispid(2), helpstring(u'Get a single Class or Instance asynchronously')], HRESULT, 'GetAsync',
              ( ['in'], POINTER(IDispatch), 'objWbemSink' ),
              ( ['in', 'optional'], BSTR, 'strObjectPath', u'' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemAsyncContext' )),
    COMMETHOD([dispid(3), helpstring(u'Delete a Class or Instance')], HRESULT, 'Delete',
              ( ['in'], BSTR, 'strObjectPath' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' )),
    COMMETHOD([dispid(4), helpstring(u'Delete a Class or Instance asynchronously')], HRESULT, 'DeleteAsync',
              ( ['in'], POINTER(IDispatch), 'objWbemSink' ),
              ( ['in'], BSTR, 'strObjectPath' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemAsyncContext' )),
    COMMETHOD([dispid(5), helpstring(u'Enumerate the Instances of a Class')], HRESULT, 'InstancesOf',
              ( ['in'], BSTR, 'strClass' ),
              ( ['in', 'optional'], c_int, 'iFlags', 16 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObjectSet)), 'objWbemObjectSet' )),
    COMMETHOD([dispid(6), helpstring(u'Enumerate the Instances of a Class asynchronously')], HRESULT, 'InstancesOfAsync',
              ( ['in'], POINTER(IDispatch), 'objWbemSink' ),
              ( ['in'], BSTR, 'strClass' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemAsyncContext' )),
    COMMETHOD([dispid(7), helpstring(u'Enumerate the subclasses of a Class')], HRESULT, 'SubclassesOf',
              ( ['in', 'optional'], BSTR, 'strSuperclass', u'' ),
              ( ['in', 'optional'], c_int, 'iFlags', 16 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObjectSet)), 'objWbemObjectSet' )),
    COMMETHOD([dispid(8), helpstring(u'Enumerate the subclasses of a Class asynchronously ')], HRESULT, 'SubclassesOfAsync',
              ( ['in'], POINTER(IDispatch), 'objWbemSink' ),
              ( ['in', 'optional'], BSTR, 'strSuperclass', u'' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemAsyncContext' )),
    COMMETHOD([dispid(9), helpstring(u'Execute a Query')], HRESULT, 'ExecQuery',
              ( ['in'], BSTR, 'strQuery' ),
              ( ['in', 'optional'], BSTR, 'strQueryLanguage', u'WQL' ),
              ( ['in', 'optional'], c_int, 'iFlags', 16 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObjectSet)), 'objWbemObjectSet' )),
    COMMETHOD([dispid(10), helpstring(u'Execute an asynchronous Query')], HRESULT, 'ExecQueryAsync',
              ( ['in'], POINTER(IDispatch), 'objWbemSink' ),
              ( ['in'], BSTR, 'strQuery' ),
              ( ['in', 'optional'], BSTR, 'strQueryLanguage', u'WQL' ),
              ( ['in', 'optional'], c_int, 'lFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemAsyncContext' )),
    COMMETHOD([dispid(11), helpstring(u'Get the Associators of a class or instance')], HRESULT, 'AssociatorsOf',
              ( ['in'], BSTR, 'strObjectPath' ),
              ( ['in', 'optional'], BSTR, 'strAssocClass', u'' ),
              ( ['in', 'optional'], BSTR, 'strResultClass', u'' ),
              ( ['in', 'optional'], BSTR, 'strResultRole', u'' ),
              ( ['in', 'optional'], BSTR, 'strRole', u'' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bClassesOnly', False ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bSchemaOnly', False ),
              ( ['in', 'optional'], BSTR, 'strRequiredAssocQualifier', u'' ),
              ( ['in', 'optional'], BSTR, 'strRequiredQualifier', u'' ),
              ( ['in', 'optional'], c_int, 'iFlags', 16 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObjectSet)), 'objWbemObjectSet' )),
    COMMETHOD([dispid(12), helpstring(u'Get the Associators of a class or instance asynchronously')], HRESULT, 'AssociatorsOfAsync',
              ( ['in'], POINTER(IDispatch), 'objWbemSink' ),
              ( ['in'], BSTR, 'strObjectPath' ),
              ( ['in', 'optional'], BSTR, 'strAssocClass', u'' ),
              ( ['in', 'optional'], BSTR, 'strResultClass', u'' ),
              ( ['in', 'optional'], BSTR, 'strResultRole', u'' ),
              ( ['in', 'optional'], BSTR, 'strRole', u'' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bClassesOnly', False ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bSchemaOnly', False ),
              ( ['in', 'optional'], BSTR, 'strRequiredAssocQualifier', u'' ),
              ( ['in', 'optional'], BSTR, 'strRequiredQualifier', u'' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemAsyncContext' )),
    COMMETHOD([dispid(13), helpstring(u'Get the References to a class or instance')], HRESULT, 'ReferencesTo',
              ( ['in'], BSTR, 'strObjectPath' ),
              ( ['in', 'optional'], BSTR, 'strResultClass', u'' ),
              ( ['in', 'optional'], BSTR, 'strRole', u'' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bClassesOnly', False ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bSchemaOnly', False ),
              ( ['in', 'optional'], BSTR, 'strRequiredQualifier', u'' ),
              ( ['in', 'optional'], c_int, 'iFlags', 16 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObjectSet)), 'objWbemObjectSet' )),
    COMMETHOD([dispid(14), helpstring(u'Get the References to a class or instance asynchronously')], HRESULT, 'ReferencesToAsync',
              ( ['in'], POINTER(IDispatch), 'objWbemSink' ),
              ( ['in'], BSTR, 'strObjectPath' ),
              ( ['in', 'optional'], BSTR, 'strResultClass', u'' ),
              ( ['in', 'optional'], BSTR, 'strRole', u'' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bClassesOnly', False ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bSchemaOnly', False ),
              ( ['in', 'optional'], BSTR, 'strRequiredQualifier', u'' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemAsyncContext' )),
    COMMETHOD([dispid(15), helpstring(u'Execute a Query to receive Notifications')], HRESULT, 'ExecNotificationQuery',
              ( ['in'], BSTR, 'strQuery' ),
              ( ['in', 'optional'], BSTR, 'strQueryLanguage', u'WQL' ),
              ( ['in', 'optional'], c_int, 'iFlags', 48 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemEventSource)), 'objWbemEventSource' )),
    COMMETHOD([dispid(16), helpstring(u'Execute an asynchronous Query to receive Notifications')], HRESULT, 'ExecNotificationQueryAsync',
              ( ['in'], POINTER(IDispatch), 'objWbemSink' ),
              ( ['in'], BSTR, 'strQuery' ),
              ( ['in', 'optional'], BSTR, 'strQueryLanguage', u'WQL' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemAsyncContext' )),
    COMMETHOD([dispid(17), helpstring(u'Execute a Method')], HRESULT, 'ExecMethod',
              ( ['in'], BSTR, 'strObjectPath' ),
              ( ['in'], BSTR, 'strMethodName' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemInParameters' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObject)), 'objWbemOutParameters' )),
    COMMETHOD([dispid(18), helpstring(u'Execute a Method asynchronously')], HRESULT, 'ExecMethodAsync',
              ( ['in'], POINTER(IDispatch), 'objWbemSink' ),
              ( ['in'], BSTR, 'strObjectPath' ),
              ( ['in'], BSTR, 'strMethodName' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemInParameters' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemAsyncContext' )),
    COMMETHOD([dispid(19), helpstring(u'The Security Configurator for this Object'), 'propget'], HRESULT, 'Security_',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemSecurity)), 'objWbemSecurity' )),
]
################################################################
## code template for ISWbemServices implementation
##class ISWbemServices_Impl(object):
##    @property
##    def Security_(self):
##        u'The Security Configurator for this Object'
##        #return objWbemSecurity
##
##    def AssociatorsOfAsync(self, objWbemSink, strObjectPath, strAssocClass, strResultClass, strResultRole, strRole, bClassesOnly, bSchemaOnly, strRequiredAssocQualifier, strRequiredQualifier, iFlags, objWbemNamedValueSet, objWbemAsyncContext):
##        u'Get the Associators of a class or instance asynchronously'
##        #return 
##
##    def SubclassesOfAsync(self, objWbemSink, strSuperclass, iFlags, objWbemNamedValueSet, objWbemAsyncContext):
##        u'Enumerate the subclasses of a Class asynchronously '
##        #return 
##
##    def Get(self, strObjectPath, iFlags, objWbemNamedValueSet):
##        u'Get a single Class or Instance'
##        #return objWbemObject
##
##    def GetAsync(self, objWbemSink, strObjectPath, iFlags, objWbemNamedValueSet, objWbemAsyncContext):
##        u'Get a single Class or Instance asynchronously'
##        #return 
##
##    def ReferencesTo(self, strObjectPath, strResultClass, strRole, bClassesOnly, bSchemaOnly, strRequiredQualifier, iFlags, objWbemNamedValueSet):
##        u'Get the References to a class or instance'
##        #return objWbemObjectSet
##
##    def ExecNotificationQueryAsync(self, objWbemSink, strQuery, strQueryLanguage, iFlags, objWbemNamedValueSet, objWbemAsyncContext):
##        u'Execute an asynchronous Query to receive Notifications'
##        #return 
##
##    def SubclassesOf(self, strSuperclass, iFlags, objWbemNamedValueSet):
##        u'Enumerate the subclasses of a Class'
##        #return objWbemObjectSet
##
##    def ExecMethod(self, strObjectPath, strMethodName, objWbemInParameters, iFlags, objWbemNamedValueSet):
##        u'Execute a Method'
##        #return objWbemOutParameters
##
##    def ExecNotificationQuery(self, strQuery, strQueryLanguage, iFlags, objWbemNamedValueSet):
##        u'Execute a Query to receive Notifications'
##        #return objWbemEventSource
##
##    def InstancesOfAsync(self, objWbemSink, strClass, iFlags, objWbemNamedValueSet, objWbemAsyncContext):
##        u'Enumerate the Instances of a Class asynchronously'
##        #return 
##
##    def DeleteAsync(self, objWbemSink, strObjectPath, iFlags, objWbemNamedValueSet, objWbemAsyncContext):
##        u'Delete a Class or Instance asynchronously'
##        #return 
##
##    def ExecQueryAsync(self, objWbemSink, strQuery, strQueryLanguage, lFlags, objWbemNamedValueSet, objWbemAsyncContext):
##        u'Execute an asynchronous Query'
##        #return 
##
##    def AssociatorsOf(self, strObjectPath, strAssocClass, strResultClass, strResultRole, strRole, bClassesOnly, bSchemaOnly, strRequiredAssocQualifier, strRequiredQualifier, iFlags, objWbemNamedValueSet):
##        u'Get the Associators of a class or instance'
##        #return objWbemObjectSet
##
##    def InstancesOf(self, strClass, iFlags, objWbemNamedValueSet):
##        u'Enumerate the Instances of a Class'
##        #return objWbemObjectSet
##
##    def ReferencesToAsync(self, objWbemSink, strObjectPath, strResultClass, strRole, bClassesOnly, bSchemaOnly, strRequiredQualifier, iFlags, objWbemNamedValueSet, objWbemAsyncContext):
##        u'Get the References to a class or instance asynchronously'
##        #return 
##
##    def ExecMethodAsync(self, objWbemSink, strObjectPath, strMethodName, objWbemInParameters, iFlags, objWbemNamedValueSet, objWbemAsyncContext):
##        u'Execute a Method asynchronously'
##        #return 
##
##    def ExecQuery(self, strQuery, strQueryLanguage, iFlags, objWbemNamedValueSet):
##        u'Execute a Query'
##        #return objWbemObjectSet
##
##    def Delete(self, strObjectPath, iFlags, objWbemNamedValueSet):
##        u'Delete a Class or Instance'
##        #return 
##

class ISWbemObjectEx(ISWbemObject):
    _case_insensitive_ = True
    u'A Class or Instance'
    _iid_ = GUID('{269AD56A-8A67-4129-BC8C-0506DCFE9880}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
class ISWbemObjectPath(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'An Object path'
    _iid_ = GUID('{5791BC27-CE9C-11D1-97BF-0000F81E849C}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
class ISWbemSink(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Asynchronous operation control'
    _iid_ = GUID('{75718C9F-F029-11D1-A1AC-00C04FB6C223}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation', 'hidden']
ISWbemServicesEx._methods_ = [
    COMMETHOD([dispid(20), helpstring(u'Save the Object to this Namespace')], HRESULT, 'Put',
              ( ['in'], POINTER(ISWbemObjectEx), 'objWbemObject' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObjectPath)), 'objWbemObjectPath' )),
    COMMETHOD([dispid(21), helpstring(u'Save the Object to this Namespace asynchronously')], HRESULT, 'PutAsync',
              ( ['in'], POINTER(ISWbemSink), 'objWbemSink' ),
              ( ['in'], POINTER(ISWbemObjectEx), 'objWbemObject' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemAsyncContext' )),
]
################################################################
## code template for ISWbemServicesEx implementation
##class ISWbemServicesEx_Impl(object):
##    def Put(self, objWbemObject, iFlags, objWbemNamedValueSet):
##        u'Save the Object to this Namespace'
##        #return objWbemObjectPath
##
##    def PutAsync(self, objWbemSink, objWbemObject, iFlags, objWbemNamedValueSet, objWbemAsyncContext):
##        u'Save the Object to this Namespace asynchronously'
##        #return 
##


# values for enumeration 'WbemTextFlagEnum'
wbemTextFlagNoFlavors = 1
WbemTextFlagEnum = c_int # enum

# values for enumeration 'WbemComparisonFlagEnum'
wbemComparisonFlagIncludeAll = 0
wbemComparisonFlagIgnoreQualifiers = 1
wbemComparisonFlagIgnoreObjectSource = 2
wbemComparisonFlagIgnoreDefaultValues = 4
wbemComparisonFlagIgnoreClass = 8
wbemComparisonFlagIgnoreCase = 16
wbemComparisonFlagIgnoreFlavor = 32
WbemComparisonFlagEnum = c_int # enum
class SWbemPrivilegeSet(CoClass):
    u'A collection of Privilege Overrides'
    _reg_clsid_ = GUID('{26EE67BE-5804-11D2-8B4A-00600806D9B6}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
class ISWbemPrivilegeSet(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A collection of Privilege Overrides'
    _iid_ = GUID('{26EE67BF-5804-11D2-8B4A-00600806D9B6}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation', 'hidden']
SWbemPrivilegeSet._com_interfaces_ = [ISWbemPrivilegeSet]

ISWbemNamedValueSet._methods_ = [
    COMMETHOD([dispid(-4), 'restricted', 'propget'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'pUnk' )),
    COMMETHOD([dispid(0), helpstring(u'Get a named value from this Collection')], HRESULT, 'Item',
              ( ['in'], BSTR, 'strName' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemNamedValue)), 'objWbemNamedValue' )),
    COMMETHOD([dispid(1), helpstring(u'The number of items in this collection'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'iCount' )),
    COMMETHOD([dispid(2), helpstring(u'Add a named value to this collection')], HRESULT, 'Add',
              ( ['in'], BSTR, 'strName' ),
              ( ['in'], POINTER(VARIANT), 'varValue' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemNamedValue)), 'objWbemNamedValue' )),
    COMMETHOD([dispid(3), helpstring(u'Remove a named value from this collection')], HRESULT, 'Remove',
              ( ['in'], BSTR, 'strName' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 )),
    COMMETHOD([dispid(4), helpstring(u'Make a copy of this collection')], HRESULT, 'Clone',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemNamedValueSet)), 'objWbemNamedValueSet' )),
    COMMETHOD([dispid(5), helpstring(u'Delete all items in this collection')], HRESULT, 'DeleteAll'),
]
################################################################
## code template for ISWbemNamedValueSet implementation
##class ISWbemNamedValueSet_Impl(object):
##    @property
##    def Count(self):
##        u'The number of items in this collection'
##        #return iCount
##
##    @property
##    def _NewEnum(self):
##        '-no docstring-'
##        #return pUnk
##
##    def Clone(self):
##        u'Make a copy of this collection'
##        #return objWbemNamedValueSet
##
##    def Remove(self, strName, iFlags):
##        u'Remove a named value from this collection'
##        #return 
##
##    def Item(self, strName, iFlags):
##        u'Get a named value from this Collection'
##        #return objWbemNamedValue
##
##    def Add(self, strName, varValue, iFlags):
##        u'Add a named value to this collection'
##        #return objWbemNamedValue
##
##    def DeleteAll(self):
##        u'Delete all items in this collection'
##        #return 
##

class SWbemRefreshableItem(CoClass):
    u'A single item from a Refresher'
    _reg_clsid_ = GUID('{8C6854BC-DE4B-11D3-B390-00105A1F473A}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
SWbemRefreshableItem._com_interfaces_ = [ISWbemRefreshableItem]

ISWbemSink._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Cancel an asynchronous operation')], HRESULT, 'Cancel'),
]
################################################################
## code template for ISWbemSink implementation
##class ISWbemSink_Impl(object):
##    def Cancel(self):
##        u'Cancel an asynchronous operation'
##        #return 
##

ISWbemNamedValue._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'The Value of this Named element'), 'propget'], HRESULT, 'Value',
              ( ['retval', 'out'], POINTER(VARIANT), 'varValue' )),
    COMMETHOD([dispid(0), helpstring(u'The Value of this Named element'), 'propput'], HRESULT, 'Value',
              ( ['in'], POINTER(VARIANT), 'varValue' )),
    COMMETHOD([dispid(2), helpstring(u'The Name of this Value'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'strName' )),
]
################################################################
## code template for ISWbemNamedValue implementation
##class ISWbemNamedValue_Impl(object):
##    @property
##    def Name(self):
##        u'The Name of this Value'
##        #return strName
##
##    def _get(self):
##        u'The Value of this Named element'
##        #return varValue
##    def _set(self, varValue):
##        u'The Value of this Named element'
##    Value = property(_get, _set, doc = _set.__doc__)
##

class ISWbemSinkEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'A sink for events arising from asynchronous operations'
    _iid_ = GUID('{75718CA0-F029-11D1-A1AC-00C04FB6C223}')
    _idlflags_ = ['nonextensible', 'hidden']
    _methods_ = []

# values for enumeration 'WbemErrorEnum'
wbemNoErr = 0
wbemErrFailed = -2147217407
wbemErrNotFound = -2147217406
wbemErrAccessDenied = -2147217405
wbemErrProviderFailure = -2147217404
wbemErrTypeMismatch = -2147217403
wbemErrOutOfMemory = -2147217402
wbemErrInvalidContext = -2147217401
wbemErrInvalidParameter = -2147217400
wbemErrNotAvailable = -2147217399
wbemErrCriticalError = -2147217398
wbemErrInvalidStream = -2147217397
wbemErrNotSupported = -2147217396
wbemErrInvalidSuperclass = -2147217395
wbemErrInvalidNamespace = -2147217394
wbemErrInvalidObject = -2147217393
wbemErrInvalidClass = -2147217392
wbemErrProviderNotFound = -2147217391
wbemErrInvalidProviderRegistration = -2147217390
wbemErrProviderLoadFailure = -2147217389
wbemErrInitializationFailure = -2147217388
wbemErrTransportFailure = -2147217387
wbemErrInvalidOperation = -2147217386
wbemErrInvalidQuery = -2147217385
wbemErrInvalidQueryType = -2147217384
wbemErrAlreadyExists = -2147217383
wbemErrOverrideNotAllowed = -2147217382
wbemErrPropagatedQualifier = -2147217381
wbemErrPropagatedProperty = -2147217380
wbemErrUnexpected = -2147217379
wbemErrIllegalOperation = -2147217378
wbemErrCannotBeKey = -2147217377
wbemErrIncompleteClass = -2147217376
wbemErrInvalidSyntax = -2147217375
wbemErrNondecoratedObject = -2147217374
wbemErrReadOnly = -2147217373
wbemErrProviderNotCapable = -2147217372
wbemErrClassHasChildren = -2147217371
wbemErrClassHasInstances = -2147217370
wbemErrQueryNotImplemented = -2147217369
wbemErrIllegalNull = -2147217368
wbemErrInvalidQualifierType = -2147217367
wbemErrInvalidPropertyType = -2147217366
wbemErrValueOutOfRange = -2147217365
wbemErrCannotBeSingleton = -2147217364
wbemErrInvalidCimType = -2147217363
wbemErrInvalidMethod = -2147217362
wbemErrInvalidMethodParameters = -2147217361
wbemErrSystemProperty = -2147217360
wbemErrInvalidProperty = -2147217359
wbemErrCallCancelled = -2147217358
wbemErrShuttingDown = -2147217357
wbemErrPropagatedMethod = -2147217356
wbemErrUnsupportedParameter = -2147217355
wbemErrMissingParameter = -2147217354
wbemErrInvalidParameterId = -2147217353
wbemErrNonConsecutiveParameterIds = -2147217352
wbemErrParameterIdOnRetval = -2147217351
wbemErrInvalidObjectPath = -2147217350
wbemErrOutOfDiskSpace = -2147217349
wbemErrBufferTooSmall = -2147217348
wbemErrUnsupportedPutExtension = -2147217347
wbemErrUnknownObjectType = -2147217346
wbemErrUnknownPacketType = -2147217345
wbemErrMarshalVersionMismatch = -2147217344
wbemErrMarshalInvalidSignature = -2147217343
wbemErrInvalidQualifier = -2147217342
wbemErrInvalidDuplicateParameter = -2147217341
wbemErrTooMuchData = -2147217340
wbemErrServerTooBusy = -2147217339
wbemErrInvalidFlavor = -2147217338
wbemErrCircularReference = -2147217337
wbemErrUnsupportedClassUpdate = -2147217336
wbemErrCannotChangeKeyInheritance = -2147217335
wbemErrCannotChangeIndexInheritance = -2147217328
wbemErrTooManyProperties = -2147217327
wbemErrUpdateTypeMismatch = -2147217326
wbemErrUpdateOverrideNotAllowed = -2147217325
wbemErrUpdatePropagatedMethod = -2147217324
wbemErrMethodNotImplemented = -2147217323
wbemErrMethodDisabled = -2147217322
wbemErrRefresherBusy = -2147217321
wbemErrUnparsableQuery = -2147217320
wbemErrNotEventClass = -2147217319
wbemErrMissingGroupWithin = -2147217318
wbemErrMissingAggregationList = -2147217317
wbemErrPropertyNotAnObject = -2147217316
wbemErrAggregatingByObject = -2147217315
wbemErrUninterpretableProviderQuery = -2147217313
wbemErrBackupRestoreWinmgmtRunning = -2147217312
wbemErrQueueOverflow = -2147217311
wbemErrPrivilegeNotHeld = -2147217310
wbemErrInvalidOperator = -2147217309
wbemErrLocalCredentials = -2147217308
wbemErrCannotBeAbstract = -2147217307
wbemErrAmendedObject = -2147217306
wbemErrClientTooSlow = -2147217305
wbemErrNullSecurityDescriptor = -2147217304
wbemErrTimeout = -2147217303
wbemErrInvalidAssociation = -2147217302
wbemErrAmbiguousOperation = -2147217301
wbemErrQuotaViolation = -2147217300
wbemErrTransactionConflict = -2147217299
wbemErrForcedRollback = -2147217298
wbemErrUnsupportedLocale = -2147217297
wbemErrHandleOutOfDate = -2147217296
wbemErrConnectionFailed = -2147217295
wbemErrInvalidHandleRequest = -2147217294
wbemErrPropertyNameTooWide = -2147217293
wbemErrClassNameTooWide = -2147217292
wbemErrMethodNameTooWide = -2147217291
wbemErrQualifierNameTooWide = -2147217290
wbemErrRerunCommand = -2147217289
wbemErrDatabaseVerMismatch = -2147217288
wbemErrVetoPut = -2147217287
wbemErrVetoDelete = -2147217286
wbemErrInvalidLocale = -2147217280
wbemErrProviderSuspended = -2147217279
wbemErrSynchronizationRequired = -2147217278
wbemErrNoSchema = -2147217277
wbemErrProviderAlreadyRegistered = -2147217276
wbemErrProviderNotRegistered = -2147217275
wbemErrFatalTransportError = -2147217274
wbemErrEncryptedConnectionRequired = -2147217273
wbemErrRegistrationTooBroad = -2147213311
wbemErrRegistrationTooPrecise = -2147213310
wbemErrTimedout = -2147209215
wbemErrResetToDefault = -2147209214
WbemErrorEnum = c_int # enum
ISWbemSinkEvents._disp_methods_ = [
    DISPMETHOD([dispid(1), helpstring(u'Event triggered when an Object is available')], None, 'OnObjectReady',
               ( [], POINTER(ISWbemObject), 'objWbemObject' ),
               ( [], POINTER(ISWbemNamedValueSet), 'objWbemAsyncContext' )),
    DISPMETHOD([dispid(2), helpstring(u'Event triggered when an asynchronous operation is completed')], None, 'OnCompleted',
               ( [], WbemErrorEnum, 'iHResult' ),
               ( [], POINTER(ISWbemObject), 'objWbemErrorObject' ),
               ( [], POINTER(ISWbemNamedValueSet), 'objWbemAsyncContext' )),
    DISPMETHOD([dispid(3), helpstring(u'Event triggered to report the progress of an asynchronous operation')], None, 'OnProgress',
               ( [], c_int, 'iUpperBound' ),
               ( [], c_int, 'iCurrent' ),
               ( [], BSTR, 'strMessage' ),
               ( [], POINTER(ISWbemNamedValueSet), 'objWbemAsyncContext' )),
    DISPMETHOD([dispid(4), helpstring(u'Event triggered when an object path is available following a Put operation')], None, 'OnObjectPut',
               ( [], POINTER(ISWbemObjectPath), 'objWbemObjectPath' ),
               ( [], POINTER(ISWbemNamedValueSet), 'objWbemAsyncContext' )),
]
class SWbemEventSource(CoClass):
    u'An Event source'
    _reg_clsid_ = GUID('{04B83D58-21AE-11D2-8B33-00600806D9B6}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
SWbemEventSource._com_interfaces_ = [ISWbemEventSource]

class ISWbemQualifierSet(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A collection of Qualifiers'
    _iid_ = GUID('{9B16ED16-D3DF-11D1-8B08-00600806D9B6}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation', 'hidden']
class ISWbemQualifier(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A Qualifier'
    _iid_ = GUID('{79B05932-D3B7-11D1-8B06-00600806D9B6}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation', 'hidden']
ISWbemQualifierSet._methods_ = [
    COMMETHOD([dispid(-4), 'restricted', 'propget'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'pUnk' )),
    COMMETHOD([dispid(0), helpstring(u'Get a named Qualifier from this collection')], HRESULT, 'Item',
              ( ['in'], BSTR, 'Name' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemQualifier)), 'objWbemQualifier' )),
    COMMETHOD([dispid(1), helpstring(u'The number of items in this collection'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'iCount' )),
    COMMETHOD([dispid(2), helpstring(u'Add a Qualifier to this collection')], HRESULT, 'Add',
              ( ['in'], BSTR, 'strName' ),
              ( ['in'], POINTER(VARIANT), 'varVal' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bPropagatesToSubclass', True ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bPropagatesToInstance', True ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bIsOverridable', True ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemQualifier)), 'objWbemQualifier' )),
    COMMETHOD([dispid(3), helpstring(u'Remove a Qualifier from this collection')], HRESULT, 'Remove',
              ( ['in'], BSTR, 'strName' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 )),
]
################################################################
## code template for ISWbemQualifierSet implementation
##class ISWbemQualifierSet_Impl(object):
##    @property
##    def Count(self):
##        u'The number of items in this collection'
##        #return iCount
##
##    def Item(self, Name, iFlags):
##        u'Get a named Qualifier from this collection'
##        #return objWbemQualifier
##
##    def Add(self, strName, varVal, bPropagatesToSubclass, bPropagatesToInstance, bIsOverridable, iFlags):
##        u'Add a Qualifier to this collection'
##        #return objWbemQualifier
##
##    @property
##    def _NewEnum(self):
##        '-no docstring-'
##        #return pUnk
##
##    def Remove(self, strName, iFlags):
##        u'Remove a Qualifier from this collection'
##        #return 
##

class SWbemProperty(CoClass):
    u'A Property'
    _reg_clsid_ = GUID('{04B83D5D-21AE-11D2-8B33-00600806D9B6}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
class ISWbemProperty(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A Property'
    _iid_ = GUID('{1A388F98-D4BA-11D1-8B09-00600806D9B6}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
SWbemProperty._com_interfaces_ = [ISWbemProperty]

ISWbemRefreshableItem._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'The index of this item in the parent refresher'), 'propget'], HRESULT, 'Index',
              ( ['retval', 'out'], POINTER(c_int), 'iIndex' )),
    COMMETHOD([dispid(2), helpstring(u'The parent refresher'), 'propget'], HRESULT, 'Refresher',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemRefresher)), 'objWbemRefresher' )),
    COMMETHOD([dispid(3), helpstring(u'Whether this item represents a single object or an object set'), 'propget'], HRESULT, 'IsSet',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bIsSet' )),
    COMMETHOD([dispid(4), helpstring(u'The object'), 'propget'], HRESULT, 'Object',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObjectEx)), 'objWbemObject' )),
    COMMETHOD([dispid(5), helpstring(u'The object set'), 'propget'], HRESULT, 'ObjectSet',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObjectSet)), 'objWbemObjectSet' )),
    COMMETHOD([dispid(6), helpstring(u'Remove this item from the parent refresher')], HRESULT, 'Remove',
              ( ['in', 'optional'], c_int, 'iFlags', 0 )),
]
################################################################
## code template for ISWbemRefreshableItem implementation
##class ISWbemRefreshableItem_Impl(object):
##    @property
##    def Index(self):
##        u'The index of this item in the parent refresher'
##        #return iIndex
##
##    @property
##    def Refresher(self):
##        u'The parent refresher'
##        #return objWbemRefresher
##
##    @property
##    def Object(self):
##        u'The object'
##        #return objWbemObject
##
##    def Remove(self, iFlags):
##        u'Remove this item from the parent refresher'
##        #return 
##
##    @property
##    def ObjectSet(self):
##        u'The object set'
##        #return objWbemObjectSet
##
##    @property
##    def IsSet(self):
##        u'Whether this item represents a single object or an object set'
##        #return bIsSet
##

ISWbemEventSource._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Retrieve the next event within a specified time period. The timeout is specified in milliseconds.')], HRESULT, 'NextEvent',
              ( ['in', 'optional'], c_int, 'iTimeoutMs', -1 ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObject)), 'objWbemObject' )),
    COMMETHOD([dispid(2), helpstring(u'The Security Configurator for this Object'), 'propget'], HRESULT, 'Security_',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemSecurity)), 'objWbemSecurity' )),
]
################################################################
## code template for ISWbemEventSource implementation
##class ISWbemEventSource_Impl(object):
##    def NextEvent(self, iTimeoutMs):
##        u'Retrieve the next event within a specified time period. The timeout is specified in milliseconds.'
##        #return objWbemObject
##
##    @property
##    def Security_(self):
##        u'The Security Configurator for this Object'
##        #return objWbemSecurity
##


# values for enumeration 'WbemPrivilegeEnum'
wbemPrivilegeCreateToken = 1
wbemPrivilegePrimaryToken = 2
wbemPrivilegeLockMemory = 3
wbemPrivilegeIncreaseQuota = 4
wbemPrivilegeMachineAccount = 5
wbemPrivilegeTcb = 6
wbemPrivilegeSecurity = 7
wbemPrivilegeTakeOwnership = 8
wbemPrivilegeLoadDriver = 9
wbemPrivilegeSystemProfile = 10
wbemPrivilegeSystemtime = 11
wbemPrivilegeProfileSingleProcess = 12
wbemPrivilegeIncreaseBasePriority = 13
wbemPrivilegeCreatePagefile = 14
wbemPrivilegeCreatePermanent = 15
wbemPrivilegeBackup = 16
wbemPrivilegeRestore = 17
wbemPrivilegeShutdown = 18
wbemPrivilegeDebug = 19
wbemPrivilegeAudit = 20
wbemPrivilegeSystemEnvironment = 21
wbemPrivilegeChangeNotify = 22
wbemPrivilegeRemoteShutdown = 23
wbemPrivilegeUndock = 24
wbemPrivilegeSyncAgent = 25
wbemPrivilegeEnableDelegation = 26
wbemPrivilegeManageVolume = 27
WbemPrivilegeEnum = c_int # enum
class ISWbemPrivilege(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A Privilege Override'
    _iid_ = GUID('{26EE67BD-5804-11D2-8B4A-00600806D9B6}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation', 'hidden']
ISWbemPrivilegeSet._methods_ = [
    COMMETHOD([dispid(-4), 'restricted', 'propget'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'pUnk' )),
    COMMETHOD([dispid(0), helpstring(u'Get a named Privilege from this collection')], HRESULT, 'Item',
              ( ['in'], WbemPrivilegeEnum, 'iPrivilege' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemPrivilege)), 'objWbemPrivilege' )),
    COMMETHOD([dispid(1), helpstring(u'The number of items in this collection'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'iCount' )),
    COMMETHOD([dispid(2), helpstring(u'Add a Privilege to this collection')], HRESULT, 'Add',
              ( ['in'], WbemPrivilegeEnum, 'iPrivilege' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bIsEnabled', True ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemPrivilege)), 'objWbemPrivilege' )),
    COMMETHOD([dispid(3), helpstring(u'Remove a Privilege from this collection')], HRESULT, 'Remove',
              ( ['in'], WbemPrivilegeEnum, 'iPrivilege' )),
    COMMETHOD([dispid(4), helpstring(u'Delete all items in this collection')], HRESULT, 'DeleteAll'),
    COMMETHOD([dispid(5), helpstring(u'Add a named Privilege to this collection')], HRESULT, 'AddAsString',
              ( ['in'], BSTR, 'strPrivilege' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bIsEnabled', True ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemPrivilege)), 'objWbemPrivilege' )),
]
################################################################
## code template for ISWbemPrivilegeSet implementation
##class ISWbemPrivilegeSet_Impl(object):
##    @property
##    def Count(self):
##        u'The number of items in this collection'
##        #return iCount
##
##    @property
##    def _NewEnum(self):
##        '-no docstring-'
##        #return pUnk
##
##    def Remove(self, iPrivilege):
##        u'Remove a Privilege from this collection'
##        #return 
##
##    def Item(self, iPrivilege):
##        u'Get a named Privilege from this collection'
##        #return objWbemPrivilege
##
##    def Add(self, iPrivilege, bIsEnabled):
##        u'Add a Privilege to this collection'
##        #return objWbemPrivilege
##
##    def DeleteAll(self):
##        u'Delete all items in this collection'
##        #return 
##
##    def AddAsString(self, strPrivilege, bIsEnabled):
##        u'Add a named Privilege to this collection'
##        #return objWbemPrivilege
##

class ISWbemPropertySet(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A collection of Properties'
    _iid_ = GUID('{DEA0A7B2-D4BA-11D1-8B09-00600806D9B6}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
ISWbemObject._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'Save this Object')], HRESULT, 'Put_',
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObjectPath)), 'objWbemObjectPath' )),
    COMMETHOD([dispid(2), helpstring(u'Save this Object asynchronously')], HRESULT, 'PutAsync_',
              ( ['in'], POINTER(IDispatch), 'objWbemSink' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemAsyncContext' )),
    COMMETHOD([dispid(3), helpstring(u'Delete this Object')], HRESULT, 'Delete_',
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' )),
    COMMETHOD([dispid(4), helpstring(u'Delete this Object asynchronously')], HRESULT, 'DeleteAsync_',
              ( ['in'], POINTER(IDispatch), 'objWbemSink' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemAsyncContext' )),
    COMMETHOD([dispid(5), helpstring(u'Return all instances of this Class')], HRESULT, 'Instances_',
              ( ['in', 'optional'], c_int, 'iFlags', 16 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObjectSet)), 'objWbemObjectSet' )),
    COMMETHOD([dispid(6), helpstring(u'Return all instances of this Class asynchronously')], HRESULT, 'InstancesAsync_',
              ( ['in'], POINTER(IDispatch), 'objWbemSink' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemAsyncContext' )),
    COMMETHOD([dispid(7), helpstring(u'Enumerate subclasses of this Class')], HRESULT, 'Subclasses_',
              ( ['in', 'optional'], c_int, 'iFlags', 16 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObjectSet)), 'objWbemObjectSet' )),
    COMMETHOD([dispid(8), helpstring(u'Enumerate subclasses of this Class asynchronously')], HRESULT, 'SubclassesAsync_',
              ( ['in'], POINTER(IDispatch), 'objWbemSink' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemAsyncContext' )),
    COMMETHOD([dispid(9), helpstring(u'Get the Associators of this Object')], HRESULT, 'Associators_',
              ( ['in', 'optional'], BSTR, 'strAssocClass', u'' ),
              ( ['in', 'optional'], BSTR, 'strResultClass', u'' ),
              ( ['in', 'optional'], BSTR, 'strResultRole', u'' ),
              ( ['in', 'optional'], BSTR, 'strRole', u'' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bClassesOnly', False ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bSchemaOnly', False ),
              ( ['in', 'optional'], BSTR, 'strRequiredAssocQualifier', u'' ),
              ( ['in', 'optional'], BSTR, 'strRequiredQualifier', u'' ),
              ( ['in', 'optional'], c_int, 'iFlags', 16 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObjectSet)), 'objWbemObjectSet' )),
    COMMETHOD([dispid(10), helpstring(u'Get the Associators of this Object asynchronously')], HRESULT, 'AssociatorsAsync_',
              ( ['in'], POINTER(IDispatch), 'objWbemSink' ),
              ( ['in', 'optional'], BSTR, 'strAssocClass', u'' ),
              ( ['in', 'optional'], BSTR, 'strResultClass', u'' ),
              ( ['in', 'optional'], BSTR, 'strResultRole', u'' ),
              ( ['in', 'optional'], BSTR, 'strRole', u'' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bClassesOnly', False ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bSchemaOnly', False ),
              ( ['in', 'optional'], BSTR, 'strRequiredAssocQualifier', u'' ),
              ( ['in', 'optional'], BSTR, 'strRequiredQualifier', u'' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemAsyncContext' )),
    COMMETHOD([dispid(11), helpstring(u'Get the References to this Object')], HRESULT, 'References_',
              ( ['in', 'optional'], BSTR, 'strResultClass', u'' ),
              ( ['in', 'optional'], BSTR, 'strRole', u'' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bClassesOnly', False ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bSchemaOnly', False ),
              ( ['in', 'optional'], BSTR, 'strRequiredQualifier', u'' ),
              ( ['in', 'optional'], c_int, 'iFlags', 16 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObjectSet)), 'objWbemObjectSet' )),
    COMMETHOD([dispid(12), helpstring(u'Get the References to this Object asynchronously')], HRESULT, 'ReferencesAsync_',
              ( ['in'], POINTER(IDispatch), 'objWbemSink' ),
              ( ['in', 'optional'], BSTR, 'strResultClass', u'' ),
              ( ['in', 'optional'], BSTR, 'strRole', u'' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bClassesOnly', False ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bSchemaOnly', False ),
              ( ['in', 'optional'], BSTR, 'strRequiredQualifier', u'' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemAsyncContext' )),
    COMMETHOD([dispid(13), helpstring(u'Execute a Method of this Object')], HRESULT, 'ExecMethod_',
              ( ['in'], BSTR, 'strMethodName' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemInParameters' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObject)), 'objWbemOutParameters' )),
    COMMETHOD([dispid(14), helpstring(u'Execute a Method of this Object asynchronously')], HRESULT, 'ExecMethodAsync_',
              ( ['in'], POINTER(IDispatch), 'objWbemSink' ),
              ( ['in'], BSTR, 'strMethodName' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemInParameters' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemAsyncContext' )),
    COMMETHOD([dispid(15), helpstring(u'Clone this Object')], HRESULT, 'Clone_',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObject)), 'objWbemObject' )),
    COMMETHOD([dispid(16), helpstring(u'Get the MOF text of this Object')], HRESULT, 'GetObjectText_',
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['retval', 'out'], POINTER(BSTR), 'strObjectText' )),
    COMMETHOD([dispid(17), helpstring(u'Create a subclass of this Object')], HRESULT, 'SpawnDerivedClass_',
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObject)), 'objWbemObject' )),
    COMMETHOD([dispid(18), helpstring(u'Create an Instance of this Object')], HRESULT, 'SpawnInstance_',
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObject)), 'objWbemObject' )),
    COMMETHOD([dispid(19), helpstring(u'Compare this Object with another')], HRESULT, 'CompareTo_',
              ( ['in'], POINTER(IDispatch), 'objWbemObject' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bResult' )),
    COMMETHOD([dispid(20), helpstring(u'The collection of Qualifiers of this Object'), 'propget'], HRESULT, 'Qualifiers_',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemQualifierSet)), 'objWbemQualifierSet' )),
    COMMETHOD([dispid(21), helpstring(u'The collection of Properties of this Object'), 'propget'], HRESULT, 'Properties_',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemPropertySet)), 'objWbemPropertySet' )),
    COMMETHOD([dispid(22), helpstring(u'The collection of Methods of this Object'), 'propget'], HRESULT, 'Methods_',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemMethodSet)), 'objWbemMethodSet' )),
    COMMETHOD([dispid(23), helpstring(u'An array of strings describing the class derivation heirarchy, in most-derived-from order (the first element in the array defines the superclass and the last element defines the dynasty class).'), 'propget'], HRESULT, 'Derivation_',
              ( ['retval', 'out'], POINTER(VARIANT), 'strClassNameArray' )),
    COMMETHOD([dispid(24), helpstring(u'The path of this Object'), 'propget'], HRESULT, 'Path_',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObjectPath)), 'objWbemObjectPath' )),
    COMMETHOD([dispid(25), helpstring(u'The Security Configurator for this Object'), 'propget'], HRESULT, 'Security_',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemSecurity)), 'objWbemSecurity' )),
]
################################################################
## code template for ISWbemObject implementation
##class ISWbemObject_Impl(object):
##    def SpawnDerivedClass_(self, iFlags):
##        u'Create a subclass of this Object'
##        #return objWbemObject
##
##    def DeleteAsync_(self, objWbemSink, iFlags, objWbemNamedValueSet, objWbemAsyncContext):
##        u'Delete this Object asynchronously'
##        #return 
##
##    def CompareTo_(self, objWbemObject, iFlags):
##        u'Compare this Object with another'
##        #return bResult
##
##    def Delete_(self, iFlags, objWbemNamedValueSet):
##        u'Delete this Object'
##        #return 
##
##    def Clone_(self):
##        u'Clone this Object'
##        #return objWbemObject
##
##    def InstancesAsync_(self, objWbemSink, iFlags, objWbemNamedValueSet, objWbemAsyncContext):
##        u'Return all instances of this Class asynchronously'
##        #return 
##
##    @property
##    def Security_(self):
##        u'The Security Configurator for this Object'
##        #return objWbemSecurity
##
##    def AssociatorsAsync_(self, objWbemSink, strAssocClass, strResultClass, strResultRole, strRole, bClassesOnly, bSchemaOnly, strRequiredAssocQualifier, strRequiredQualifier, iFlags, objWbemNamedValueSet, objWbemAsyncContext):
##        u'Get the Associators of this Object asynchronously'
##        #return 
##
##    @property
##    def Qualifiers_(self):
##        u'The collection of Qualifiers of this Object'
##        #return objWbemQualifierSet
##
##    def Put_(self, iFlags, objWbemNamedValueSet):
##        u'Save this Object'
##        #return objWbemObjectPath
##
##    @property
##    def Path_(self):
##        u'The path of this Object'
##        #return objWbemObjectPath
##
##    def References_(self, strResultClass, strRole, bClassesOnly, bSchemaOnly, strRequiredQualifier, iFlags, objWbemNamedValueSet):
##        u'Get the References to this Object'
##        #return objWbemObjectSet
##
##    @property
##    def Properties_(self):
##        u'The collection of Properties of this Object'
##        #return objWbemPropertySet
##
##    def Instances_(self, iFlags, objWbemNamedValueSet):
##        u'Return all instances of this Class'
##        #return objWbemObjectSet
##
##    def ReferencesAsync_(self, objWbemSink, strResultClass, strRole, bClassesOnly, bSchemaOnly, strRequiredQualifier, iFlags, objWbemNamedValueSet, objWbemAsyncContext):
##        u'Get the References to this Object asynchronously'
##        #return 
##
##    def Subclasses_(self, iFlags, objWbemNamedValueSet):
##        u'Enumerate subclasses of this Class'
##        #return objWbemObjectSet
##
##    def PutAsync_(self, objWbemSink, iFlags, objWbemNamedValueSet, objWbemAsyncContext):
##        u'Save this Object asynchronously'
##        #return 
##
##    def Associators_(self, strAssocClass, strResultClass, strResultRole, strRole, bClassesOnly, bSchemaOnly, strRequiredAssocQualifier, strRequiredQualifier, iFlags, objWbemNamedValueSet):
##        u'Get the Associators of this Object'
##        #return objWbemObjectSet
##
##    def SubclassesAsync_(self, objWbemSink, iFlags, objWbemNamedValueSet, objWbemAsyncContext):
##        u'Enumerate subclasses of this Class asynchronously'
##        #return 
##
##    def SpawnInstance_(self, iFlags):
##        u'Create an Instance of this Object'
##        #return objWbemObject
##
##    def ExecMethodAsync_(self, objWbemSink, strMethodName, objWbemInParameters, iFlags, objWbemNamedValueSet, objWbemAsyncContext):
##        u'Execute a Method of this Object asynchronously'
##        #return 
##
##    @property
##    def Methods_(self):
##        u'The collection of Methods of this Object'
##        #return objWbemMethodSet
##
##    def ExecMethod_(self, strMethodName, objWbemInParameters, iFlags, objWbemNamedValueSet):
##        u'Execute a Method of this Object'
##        #return objWbemOutParameters
##
##    @property
##    def Derivation_(self):
##        u'An array of strings describing the class derivation heirarchy, in most-derived-from order (the first element in the array defines the superclass and the last element defines the dynasty class).'
##        #return strClassNameArray
##
##    def GetObjectText_(self, iFlags):
##        u'Get the MOF text of this Object'
##        #return strObjectText
##


# values for enumeration 'WbemObjectTextFormatEnum'
wbemObjectTextFormatCIMDTD20 = 1
wbemObjectTextFormatWMIDTD20 = 2
WbemObjectTextFormatEnum = c_int # enum
ISWbemObjectEx._methods_ = [
    COMMETHOD([dispid(26), helpstring(u'Refresh this Object')], HRESULT, 'Refresh_',
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' )),
    COMMETHOD([dispid(27), helpstring(u'The collection of System Properties of this Object'), 'propget'], HRESULT, 'SystemProperties_',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemPropertySet)), 'objWbemPropertySet' )),
    COMMETHOD([dispid(28), helpstring(u'Retrieve a textual representation of this Object')], HRESULT, 'GetText_',
              ( ['in'], WbemObjectTextFormatEnum, 'iObjectTextFormat' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' ),
              ( ['retval', 'out'], POINTER(BSTR), 'bsText' )),
    COMMETHOD([dispid(29), helpstring(u'Set this Object using the supplied textual representation')], HRESULT, 'SetFromText_',
              ( ['in'], BSTR, 'bsText' ),
              ( ['in'], WbemObjectTextFormatEnum, 'iObjectTextFormat' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['in', 'optional'], POINTER(IDispatch), 'objWbemNamedValueSet' )),
]
################################################################
## code template for ISWbemObjectEx implementation
##class ISWbemObjectEx_Impl(object):
##    def GetText_(self, iObjectTextFormat, iFlags, objWbemNamedValueSet):
##        u'Retrieve a textual representation of this Object'
##        #return bsText
##
##    def Refresh_(self, iFlags, objWbemNamedValueSet):
##        u'Refresh this Object'
##        #return 
##
##    def SetFromText_(self, bsText, iObjectTextFormat, iFlags, objWbemNamedValueSet):
##        u'Set this Object using the supplied textual representation'
##        #return 
##
##    @property
##    def SystemProperties_(self):
##        u'The collection of System Properties of this Object'
##        #return objWbemPropertySet
##


# values for enumeration 'WbemQueryFlagEnum'
wbemQueryFlagDeep = 0
wbemQueryFlagShallow = 1
wbemQueryFlagPrototype = 2
WbemQueryFlagEnum = c_int # enum
class SWbemRefresher(CoClass):
    u'Refresher'
    _reg_clsid_ = GUID('{D269BF5C-D9C1-11D3-B38F-00105A1F473A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
SWbemRefresher._com_interfaces_ = [ISWbemRefresher]

class SWbemPrivilege(CoClass):
    u'A Privilege Override'
    _reg_clsid_ = GUID('{26EE67BC-5804-11D2-8B4A-00600806D9B6}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
SWbemPrivilege._com_interfaces_ = [ISWbemPrivilege]

class SWbemLocator(CoClass):
    u'Used to obtain Namespace connections'
    _reg_clsid_ = GUID('{76A64158-CB41-11D1-8B02-00600806D9B6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
SWbemLocator._com_interfaces_ = [ISWbemLocator]

class SWbemObjectPath(CoClass):
    u'Object Path'
    _reg_clsid_ = GUID('{5791BC26-CE9C-11D1-97BF-0000F81E849C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
SWbemObjectPath._com_interfaces_ = [ISWbemObjectPath]

class ISWbemMethod(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A Method'
    _iid_ = GUID('{422E8E90-D955-11D1-8B09-00600806D9B6}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation', 'hidden']
ISWbemMethodSet._methods_ = [
    COMMETHOD([dispid(-4), 'restricted', 'propget'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'pUnk' )),
    COMMETHOD([dispid(0), helpstring(u'Get a named Method from this collection')], HRESULT, 'Item',
              ( ['in'], BSTR, 'strName' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemMethod)), 'objWbemMethod' )),
    COMMETHOD([dispid(1), helpstring(u'The number of items in this collection'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'iCount' )),
]
################################################################
## code template for ISWbemMethodSet implementation
##class ISWbemMethodSet_Impl(object):
##    @property
##    def Count(self):
##        u'The number of items in this collection'
##        #return iCount
##
##    def Item(self, strName, iFlags):
##        u'Get a named Method from this collection'
##        #return objWbemMethod
##
##    @property
##    def _NewEnum(self):
##        '-no docstring-'
##        #return pUnk
##

class SWbemSink(CoClass):
    u'A sink for events arising from asynchronous operations'
    _reg_clsid_ = GUID('{75718C9A-F029-11D1-A1AC-00C04FB6C223}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
SWbemSink._com_interfaces_ = [ISWbemSink]
SWbemSink._outgoing_interfaces_ = [ISWbemSinkEvents]

class ISWbemDateTime(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A Datetime'
    _iid_ = GUID('{5E97458A-CF77-11D3-B38F-00105A1F473A}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
ISWbemDateTime._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'The DMTF datetime'), 'propget'], HRESULT, 'Value',
              ( ['retval', 'out'], POINTER(BSTR), 'strValue' )),
    COMMETHOD([dispid(0), helpstring(u'The DMTF datetime'), 'propput'], HRESULT, 'Value',
              ( ['in'], BSTR, 'strValue' )),
    COMMETHOD([dispid(1), helpstring(u'The Year component of the value (must be in the range 0-9999)'), 'propget'], HRESULT, 'Year',
              ( ['retval', 'out'], POINTER(c_int), 'iYear' )),
    COMMETHOD([dispid(1), helpstring(u'The Year component of the value (must be in the range 0-9999)'), 'propput'], HRESULT, 'Year',
              ( ['in'], c_int, 'iYear' )),
    COMMETHOD([dispid(2), helpstring(u'Whether the Year component is specified'), 'propget'], HRESULT, 'YearSpecified',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bYearSpecified' )),
    COMMETHOD([dispid(2), helpstring(u'Whether the Year component is specified'), 'propput'], HRESULT, 'YearSpecified',
              ( ['in'], VARIANT_BOOL, 'bYearSpecified' )),
    COMMETHOD([dispid(3), helpstring(u'The Month component of the value (must be in the range 1-12)'), 'propget'], HRESULT, 'Month',
              ( ['retval', 'out'], POINTER(c_int), 'iMonth' )),
    COMMETHOD([dispid(3), helpstring(u'The Month component of the value (must be in the range 1-12)'), 'propput'], HRESULT, 'Month',
              ( ['in'], c_int, 'iMonth' )),
    COMMETHOD([dispid(4), helpstring(u'Whether the Month component is specified'), 'propget'], HRESULT, 'MonthSpecified',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bMonthSpecified' )),
    COMMETHOD([dispid(4), helpstring(u'Whether the Month component is specified'), 'propput'], HRESULT, 'MonthSpecified',
              ( ['in'], VARIANT_BOOL, 'bMonthSpecified' )),
    COMMETHOD([dispid(5), helpstring(u'The Day component of the value (must be in the range 1-31, or 0-999999 for interval values)'), 'propget'], HRESULT, 'Day',
              ( ['retval', 'out'], POINTER(c_int), 'iDay' )),
    COMMETHOD([dispid(5), helpstring(u'The Day component of the value (must be in the range 1-31, or 0-999999 for interval values)'), 'propput'], HRESULT, 'Day',
              ( ['in'], c_int, 'iDay' )),
    COMMETHOD([dispid(6), helpstring(u'Whether the Day component is specified'), 'propget'], HRESULT, 'DaySpecified',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bDaySpecified' )),
    COMMETHOD([dispid(6), helpstring(u'Whether the Day component is specified'), 'propput'], HRESULT, 'DaySpecified',
              ( ['in'], VARIANT_BOOL, 'bDaySpecified' )),
    COMMETHOD([dispid(7), helpstring(u'The Hours component of the value (must be in the range 0-23)'), 'propget'], HRESULT, 'Hours',
              ( ['retval', 'out'], POINTER(c_int), 'iHours' )),
    COMMETHOD([dispid(7), helpstring(u'The Hours component of the value (must be in the range 0-23)'), 'propput'], HRESULT, 'Hours',
              ( ['in'], c_int, 'iHours' )),
    COMMETHOD([dispid(8), helpstring(u'Whether the Hours component is specified'), 'propget'], HRESULT, 'HoursSpecified',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bHoursSpecified' )),
    COMMETHOD([dispid(8), helpstring(u'Whether the Hours component is specified'), 'propput'], HRESULT, 'HoursSpecified',
              ( ['in'], VARIANT_BOOL, 'bHoursSpecified' )),
    COMMETHOD([dispid(9), helpstring(u'The Minutes component of the value (must be in the range 0-59)'), 'propget'], HRESULT, 'Minutes',
              ( ['retval', 'out'], POINTER(c_int), 'iMinutes' )),
    COMMETHOD([dispid(9), helpstring(u'The Minutes component of the value (must be in the range 0-59)'), 'propput'], HRESULT, 'Minutes',
              ( ['in'], c_int, 'iMinutes' )),
    COMMETHOD([dispid(10), helpstring(u'Whether the Minutes component is specified'), 'propget'], HRESULT, 'MinutesSpecified',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bMinutesSpecified' )),
    COMMETHOD([dispid(10), helpstring(u'Whether the Minutes component is specified'), 'propput'], HRESULT, 'MinutesSpecified',
              ( ['in'], VARIANT_BOOL, 'bMinutesSpecified' )),
    COMMETHOD([dispid(11), helpstring(u'The Seconds component of the value (must be in the range 0-59)'), 'propget'], HRESULT, 'Seconds',
              ( ['retval', 'out'], POINTER(c_int), 'iSeconds' )),
    COMMETHOD([dispid(11), helpstring(u'The Seconds component of the value (must be in the range 0-59)'), 'propput'], HRESULT, 'Seconds',
              ( ['in'], c_int, 'iSeconds' )),
    COMMETHOD([dispid(12), helpstring(u'Whether the Seconds component is specified'), 'propget'], HRESULT, 'SecondsSpecified',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bSecondsSpecified' )),
    COMMETHOD([dispid(12), helpstring(u'Whether the Seconds component is specified'), 'propput'], HRESULT, 'SecondsSpecified',
              ( ['in'], VARIANT_BOOL, 'bSecondsSpecified' )),
    COMMETHOD([dispid(13), helpstring(u'The Microseconds component of the value (must be in the range 0-999999)'), 'propget'], HRESULT, 'Microseconds',
              ( ['retval', 'out'], POINTER(c_int), 'iMicroseconds' )),
    COMMETHOD([dispid(13), helpstring(u'The Microseconds component of the value (must be in the range 0-999999)'), 'propput'], HRESULT, 'Microseconds',
              ( ['in'], c_int, 'iMicroseconds' )),
    COMMETHOD([dispid(14), helpstring(u'Whether the Microseconds component is specified'), 'propget'], HRESULT, 'MicrosecondsSpecified',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bMicrosecondsSpecified' )),
    COMMETHOD([dispid(14), helpstring(u'Whether the Microseconds component is specified'), 'propput'], HRESULT, 'MicrosecondsSpecified',
              ( ['in'], VARIANT_BOOL, 'bMicrosecondsSpecified' )),
    COMMETHOD([dispid(15), helpstring(u'The UTC component of the value (must be in the range -720 to 720)'), 'propget'], HRESULT, 'UTC',
              ( ['retval', 'out'], POINTER(c_int), 'iUTC' )),
    COMMETHOD([dispid(15), helpstring(u'The UTC component of the value (must be in the range -720 to 720)'), 'propput'], HRESULT, 'UTC',
              ( ['in'], c_int, 'iUTC' )),
    COMMETHOD([dispid(16), helpstring(u'Whether the UTC component is specified'), 'propget'], HRESULT, 'UTCSpecified',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bUTCSpecified' )),
    COMMETHOD([dispid(16), helpstring(u'Whether the UTC component is specified'), 'propput'], HRESULT, 'UTCSpecified',
              ( ['in'], VARIANT_BOOL, 'bUTCSpecified' )),
    COMMETHOD([dispid(17), helpstring(u'Indicates whether this value describes an absolute date and time or is an interval'), 'propget'], HRESULT, 'IsInterval',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bIsInterval' )),
    COMMETHOD([dispid(17), helpstring(u'Indicates whether this value describes an absolute date and time or is an interval'), 'propput'], HRESULT, 'IsInterval',
              ( ['in'], VARIANT_BOOL, 'bIsInterval' )),
    COMMETHOD([dispid(18), helpstring(u'Retrieve value in Variant compatible (VT_DATE) format')], HRESULT, 'GetVarDate',
              ( ['in', 'optional'], VARIANT_BOOL, 'bIsLocal', True ),
              ( ['retval', 'out'], POINTER(c_double), 'dVarDate' )),
    COMMETHOD([dispid(19), helpstring(u'Set the value using Variant compatible (VT_DATE) format')], HRESULT, 'SetVarDate',
              ( ['in'], c_double, 'dVarDate' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bIsLocal', True )),
    COMMETHOD([dispid(20), helpstring(u'Retrieve value in FILETIME compatible string representation')], HRESULT, 'GetFileTime',
              ( ['in', 'optional'], VARIANT_BOOL, 'bIsLocal', True ),
              ( ['retval', 'out'], POINTER(BSTR), 'strFileTime' )),
    COMMETHOD([dispid(21), helpstring(u'Set the value using FILETIME compatible string representation')], HRESULT, 'SetFileTime',
              ( ['in'], BSTR, 'strFileTime' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bIsLocal', True )),
]
################################################################
## code template for ISWbemDateTime implementation
##class ISWbemDateTime_Impl(object):
##    def _get(self):
##        u'Whether the Microseconds component is specified'
##        #return bMicrosecondsSpecified
##    def _set(self, bMicrosecondsSpecified):
##        u'Whether the Microseconds component is specified'
##    MicrosecondsSpecified = property(_get, _set, doc = _set.__doc__)
##
##    def SetVarDate(self, dVarDate, bIsLocal):
##        u'Set the value using Variant compatible (VT_DATE) format'
##        #return 
##
##    def _get(self):
##        u'Whether the Minutes component is specified'
##        #return bMinutesSpecified
##    def _set(self, bMinutesSpecified):
##        u'Whether the Minutes component is specified'
##    MinutesSpecified = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Whether the UTC component is specified'
##        #return bUTCSpecified
##    def _set(self, bUTCSpecified):
##        u'Whether the UTC component is specified'
##    UTCSpecified = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Whether the Seconds component is specified'
##        #return bSecondsSpecified
##    def _set(self, bSecondsSpecified):
##        u'Whether the Seconds component is specified'
##    SecondsSpecified = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Whether the Hours component is specified'
##        #return bHoursSpecified
##    def _set(self, bHoursSpecified):
##        u'Whether the Hours component is specified'
##    HoursSpecified = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Seconds component of the value (must be in the range 0-59)'
##        #return iSeconds
##    def _set(self, iSeconds):
##        u'The Seconds component of the value (must be in the range 0-59)'
##    Seconds = property(_get, _set, doc = _set.__doc__)
##
##    def SetFileTime(self, strFileTime, bIsLocal):
##        u'Set the value using FILETIME compatible string representation'
##        #return 
##
##    def _get(self):
##        u'The Hours component of the value (must be in the range 0-23)'
##        #return iHours
##    def _set(self, iHours):
##        u'The Hours component of the value (must be in the range 0-23)'
##    Hours = property(_get, _set, doc = _set.__doc__)
##
##    def GetVarDate(self, bIsLocal):
##        u'Retrieve value in Variant compatible (VT_DATE) format'
##        #return dVarDate
##
##    def _get(self):
##        u'Whether the Month component is specified'
##        #return bMonthSpecified
##    def _set(self, bMonthSpecified):
##        u'Whether the Month component is specified'
##    MonthSpecified = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Day component of the value (must be in the range 1-31, or 0-999999 for interval values)'
##        #return iDay
##    def _set(self, iDay):
##        u'The Day component of the value (must be in the range 1-31, or 0-999999 for interval values)'
##    Day = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The UTC component of the value (must be in the range -720 to 720)'
##        #return iUTC
##    def _set(self, iUTC):
##        u'The UTC component of the value (must be in the range -720 to 720)'
##    UTC = property(_get, _set, doc = _set.__doc__)
##
##    def GetFileTime(self, bIsLocal):
##        u'Retrieve value in FILETIME compatible string representation'
##        #return strFileTime
##
##    def _get(self):
##        u'The DMTF datetime'
##        #return strValue
##    def _set(self, strValue):
##        u'The DMTF datetime'
##    Value = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Whether the Year component is specified'
##        #return bYearSpecified
##    def _set(self, bYearSpecified):
##        u'Whether the Year component is specified'
##    YearSpecified = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Microseconds component of the value (must be in the range 0-999999)'
##        #return iMicroseconds
##    def _set(self, iMicroseconds):
##        u'The Microseconds component of the value (must be in the range 0-999999)'
##    Microseconds = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Minutes component of the value (must be in the range 0-59)'
##        #return iMinutes
##    def _set(self, iMinutes):
##        u'The Minutes component of the value (must be in the range 0-59)'
##    Minutes = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Whether the Day component is specified'
##        #return bDaySpecified
##    def _set(self, bDaySpecified):
##        u'Whether the Day component is specified'
##    DaySpecified = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Month component of the value (must be in the range 1-12)'
##        #return iMonth
##    def _set(self, iMonth):
##        u'The Month component of the value (must be in the range 1-12)'
##    Month = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Indicates whether this value describes an absolute date and time or is an interval'
##        #return bIsInterval
##    def _set(self, bIsInterval):
##        u'Indicates whether this value describes an absolute date and time or is an interval'
##    IsInterval = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Year component of the value (must be in the range 0-9999)'
##        #return iYear
##    def _set(self, iYear):
##        u'The Year component of the value (must be in the range 0-9999)'
##    Year = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'WbemCimtypeEnum'
wbemCimtypeSint8 = 16
wbemCimtypeUint8 = 17
wbemCimtypeSint16 = 2
wbemCimtypeUint16 = 18
wbemCimtypeSint32 = 3
wbemCimtypeUint32 = 19
wbemCimtypeSint64 = 20
wbemCimtypeUint64 = 21
wbemCimtypeReal32 = 4
wbemCimtypeReal64 = 5
wbemCimtypeBoolean = 11
wbemCimtypeString = 8
wbemCimtypeDatetime = 101
wbemCimtypeReference = 102
wbemCimtypeChar16 = 103
wbemCimtypeObject = 13
WbemCimtypeEnum = c_int # enum
ISWbemPropertySet._methods_ = [
    COMMETHOD([dispid(-4), 'restricted', 'propget'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'pUnk' )),
    COMMETHOD([dispid(0), helpstring(u'Get a named Property from this collection')], HRESULT, 'Item',
              ( ['in'], BSTR, 'strName' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemProperty)), 'objWbemProperty' )),
    COMMETHOD([dispid(1), helpstring(u'The number of items in this collection'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'iCount' )),
    COMMETHOD([dispid(2), helpstring(u'Add a Property to this collection')], HRESULT, 'Add',
              ( ['in'], BSTR, 'strName' ),
              ( ['in'], WbemCimtypeEnum, 'iCimType' ),
              ( ['in', 'optional'], VARIANT_BOOL, 'bIsArray', False ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemProperty)), 'objWbemProperty' )),
    COMMETHOD([dispid(3), helpstring(u'Remove a Property from this collection')], HRESULT, 'Remove',
              ( ['in'], BSTR, 'strName' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 )),
]
################################################################
## code template for ISWbemPropertySet implementation
##class ISWbemPropertySet_Impl(object):
##    @property
##    def Count(self):
##        u'The number of items in this collection'
##        #return iCount
##
##    def Item(self, strName, iFlags):
##        u'Get a named Property from this collection'
##        #return objWbemProperty
##
##    def Add(self, strName, iCimType, bIsArray, iFlags):
##        u'Add a Property to this collection'
##        #return objWbemProperty
##
##    @property
##    def _NewEnum(self):
##        '-no docstring-'
##        #return pUnk
##
##    def Remove(self, strName, iFlags):
##        u'Remove a Property from this collection'
##        #return 
##

class SWbemDateTime(CoClass):
    u'Date & Time'
    _reg_clsid_ = GUID('{47DFBE54-CF76-11D3-B38F-00105A1F473A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
SWbemDateTime._com_interfaces_ = [ISWbemDateTime]

class SWbemObject(CoClass):
    u'A Class or Instance'
    _reg_clsid_ = GUID('{04B83D62-21AE-11D2-8B33-00600806D9B6}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
SWbemObject._com_interfaces_ = [ISWbemObject]

ISWbemObjectPath._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'The full path'), 'propget'], HRESULT, 'Path',
              ( ['retval', 'out'], POINTER(BSTR), 'strPath' )),
    COMMETHOD([dispid(0), helpstring(u'The full path'), 'propput'], HRESULT, 'Path',
              ( ['in'], BSTR, 'strPath' )),
    COMMETHOD([dispid(1), helpstring(u'The relative path'), 'propget'], HRESULT, 'RelPath',
              ( ['retval', 'out'], POINTER(BSTR), 'strRelPath' )),
    COMMETHOD([dispid(1), helpstring(u'The relative path'), 'propput'], HRESULT, 'RelPath',
              ( ['in'], BSTR, 'strRelPath' )),
    COMMETHOD([dispid(2), helpstring(u'The name of the Server'), 'propget'], HRESULT, 'Server',
              ( ['retval', 'out'], POINTER(BSTR), 'strServer' )),
    COMMETHOD([dispid(2), helpstring(u'The name of the Server'), 'propput'], HRESULT, 'Server',
              ( ['in'], BSTR, 'strServer' )),
    COMMETHOD([dispid(3), helpstring(u'The Namespace path'), 'propget'], HRESULT, 'Namespace',
              ( ['retval', 'out'], POINTER(BSTR), 'strNamespace' )),
    COMMETHOD([dispid(3), helpstring(u'The Namespace path'), 'propput'], HRESULT, 'Namespace',
              ( ['in'], BSTR, 'strNamespace' )),
    COMMETHOD([dispid(4), helpstring(u'The parent Namespace path'), 'propget'], HRESULT, 'ParentNamespace',
              ( ['retval', 'out'], POINTER(BSTR), 'strParentNamespace' )),
    COMMETHOD([dispid(5), helpstring(u'The Display Name for this path'), 'propget'], HRESULT, 'DisplayName',
              ( ['retval', 'out'], POINTER(BSTR), 'strDisplayName' )),
    COMMETHOD([dispid(5), helpstring(u'The Display Name for this path'), 'propput'], HRESULT, 'DisplayName',
              ( ['in'], BSTR, 'strDisplayName' )),
    COMMETHOD([dispid(6), helpstring(u'The Class name'), 'propget'], HRESULT, 'Class',
              ( ['retval', 'out'], POINTER(BSTR), 'strClass' )),
    COMMETHOD([dispid(6), helpstring(u'The Class name'), 'propput'], HRESULT, 'Class',
              ( ['in'], BSTR, 'strClass' )),
    COMMETHOD([dispid(7), helpstring(u'Indicates whether this path addresses a Class'), 'propget'], HRESULT, 'IsClass',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bIsClass' )),
    COMMETHOD([dispid(8), helpstring(u'Coerce this path to address a Class')], HRESULT, 'SetAsClass'),
    COMMETHOD([dispid(9), helpstring(u'Indicates whether this path addresses a Singleton Instance'), 'propget'], HRESULT, 'IsSingleton',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bIsSingleton' )),
    COMMETHOD([dispid(10), helpstring(u'Coerce this path to address a Singleton Instance')], HRESULT, 'SetAsSingleton'),
    COMMETHOD([dispid(11), helpstring(u'The collection of Key value bindings for this path'), 'propget'], HRESULT, 'Keys',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemNamedValueSet)), 'objWbemNamedValueSet' )),
    COMMETHOD([dispid(12), helpstring(u'Defines the security components of this path'), 'propget'], HRESULT, 'Security_',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemSecurity)), 'objWbemSecurity' )),
    COMMETHOD([dispid(13), helpstring(u'Defines locale component of this path'), 'propget'], HRESULT, 'Locale',
              ( ['retval', 'out'], POINTER(BSTR), 'strLocale' )),
    COMMETHOD([dispid(13), helpstring(u'Defines locale component of this path'), 'propput'], HRESULT, 'Locale',
              ( ['in'], BSTR, 'strLocale' )),
    COMMETHOD([dispid(14), helpstring(u'Defines authentication authority component of this path'), 'propget'], HRESULT, 'Authority',
              ( ['retval', 'out'], POINTER(BSTR), 'strAuthority' )),
    COMMETHOD([dispid(14), helpstring(u'Defines authentication authority component of this path'), 'propput'], HRESULT, 'Authority',
              ( ['in'], BSTR, 'strAuthority' )),
]
################################################################
## code template for ISWbemObjectPath implementation
##class ISWbemObjectPath_Impl(object):
##    @property
##    def Security_(self):
##        u'Defines the security components of this path'
##        #return objWbemSecurity
##
##    def SetAsClass(self):
##        u'Coerce this path to address a Class'
##        #return 
##
##    def _get(self):
##        u'The Display Name for this path'
##        #return strDisplayName
##    def _set(self, strDisplayName):
##        u'The Display Name for this path'
##    DisplayName = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def IsClass(self):
##        u'Indicates whether this path addresses a Class'
##        #return bIsClass
##
##    @property
##    def Keys(self):
##        u'The collection of Key value bindings for this path'
##        #return objWbemNamedValueSet
##
##    @property
##    def ParentNamespace(self):
##        u'The parent Namespace path'
##        #return strParentNamespace
##
##    def _get(self):
##        u'The Namespace path'
##        #return strNamespace
##    def _set(self, strNamespace):
##        u'The Namespace path'
##    Namespace = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Defines authentication authority component of this path'
##        #return strAuthority
##    def _set(self, strAuthority):
##        u'Defines authentication authority component of this path'
##    Authority = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The name of the Server'
##        #return strServer
##    def _set(self, strServer):
##        u'The name of the Server'
##    Server = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Defines locale component of this path'
##        #return strLocale
##    def _set(self, strLocale):
##        u'Defines locale component of this path'
##    Locale = property(_get, _set, doc = _set.__doc__)
##
##    def SetAsSingleton(self):
##        u'Coerce this path to address a Singleton Instance'
##        #return 
##
##    @property
##    def IsSingleton(self):
##        u'Indicates whether this path addresses a Singleton Instance'
##        #return bIsSingleton
##
##    def _get(self):
##        u'The full path'
##        #return strPath
##    def _set(self, strPath):
##        u'The full path'
##    Path = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The Class name'
##        #return strClass
##    def _set(self, strClass):
##        u'The Class name'
##    Class = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The relative path'
##        #return strRelPath
##    def _set(self, strRelPath):
##        u'The relative path'
##    RelPath = property(_get, _set, doc = _set.__doc__)
##

class SWbemSecurity(CoClass):
    u'A Security Configurator'
    _reg_clsid_ = GUID('{B54D66E9-2287-11D2-8B33-00600806D9B6}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
SWbemSecurity._com_interfaces_ = [ISWbemSecurity]

class SWbemPropertySet(CoClass):
    u'A collection of Properties'
    _reg_clsid_ = GUID('{04B83D5C-21AE-11D2-8B33-00600806D9B6}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
SWbemPropertySet._com_interfaces_ = [ISWbemPropertySet]

class SWbemServices(CoClass):
    u'A connection to a Namespace'
    _reg_clsid_ = GUID('{04B83D63-21AE-11D2-8B33-00600806D9B6}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
SWbemServices._com_interfaces_ = [ISWbemServices]

class SWbemLastError(CoClass):
    u'The last error on the current thread'
    _reg_clsid_ = GUID('{C2FEEEAC-CFCD-11D1-8B05-00600806D9B6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
class ISWbemLastError(ISWbemObject):
    _case_insensitive_ = True
    u'The last error on the current thread'
    _iid_ = GUID('{D962DB84-D4BB-11D1-8B09-00600806D9B6}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
SWbemLastError._com_interfaces_ = [ISWbemLastError]


# values for enumeration 'WbemTimeout'
wbemTimeoutInfinite = -1
WbemTimeout = c_int # enum
ISWbemMethod._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'The name of this Method'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'strName' )),
    COMMETHOD([dispid(2), helpstring(u'The originating class of this Method'), 'propget'], HRESULT, 'Origin',
              ( ['retval', 'out'], POINTER(BSTR), 'strOrigin' )),
    COMMETHOD([dispid(3), helpstring(u'The in parameters for this Method.'), 'propget'], HRESULT, 'InParameters',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObject)), 'objWbemInParameters' )),
    COMMETHOD([dispid(4), helpstring(u'The out parameters for this Method.'), 'propget'], HRESULT, 'OutParameters',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObject)), 'objWbemOutParameters' )),
    COMMETHOD([dispid(5), helpstring(u'The collection of Qualifiers of this Method.'), 'propget'], HRESULT, 'Qualifiers_',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemQualifierSet)), 'objWbemQualifierSet' )),
]
################################################################
## code template for ISWbemMethod implementation
##class ISWbemMethod_Impl(object):
##    @property
##    def Origin(self):
##        u'The originating class of this Method'
##        #return strOrigin
##
##    @property
##    def InParameters(self):
##        u'The in parameters for this Method.'
##        #return objWbemInParameters
##
##    @property
##    def Qualifiers_(self):
##        u'The collection of Qualifiers of this Method.'
##        #return objWbemQualifierSet
##
##    @property
##    def Name(self):
##        u'The name of this Method'
##        #return strName
##
##    @property
##    def OutParameters(self):
##        u'The out parameters for this Method.'
##        #return objWbemOutParameters
##

class SWbemServicesEx(CoClass):
    u'A connection to a Namespace'
    _reg_clsid_ = GUID('{62E522DC-8CF3-40A8-8B2E-37D595651E40}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
SWbemServicesEx._com_interfaces_ = [ISWbemServicesEx]

class SWbemObjectEx(CoClass):
    u'A Class or Instance'
    _reg_clsid_ = GUID('{D6BDAFB2-9435-491F-BB87-6AA0F0BC31A2}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
SWbemObjectEx._com_interfaces_ = [ISWbemObjectEx]


# values for enumeration 'WbemFlagEnum'
wbemFlagReturnImmediately = 16
wbemFlagReturnWhenComplete = 0
wbemFlagBidirectional = 0
wbemFlagForwardOnly = 32
wbemFlagNoErrorObject = 64
wbemFlagReturnErrorObject = 0
wbemFlagSendStatus = 128
wbemFlagDontSendStatus = 0
wbemFlagEnsureLocatable = 256
wbemFlagDirectRead = 512
wbemFlagSendOnlySelected = 0
wbemFlagUseAmendedQualifiers = 131072
wbemFlagGetDefault = 0
wbemFlagSpawnInstance = 1
wbemFlagUseCurrentTime = 1
WbemFlagEnum = c_int # enum
ISWbemQualifier._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'The value of this Qualifier'), 'propget'], HRESULT, 'Value',
              ( ['retval', 'out'], POINTER(VARIANT), 'varValue' )),
    COMMETHOD([dispid(0), helpstring(u'The value of this Qualifier'), 'propput'], HRESULT, 'Value',
              ( ['in'], POINTER(VARIANT), 'varValue' )),
    COMMETHOD([dispid(1), helpstring(u'The name of this Qualifier'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'strName' )),
    COMMETHOD([dispid(2), helpstring(u'Indicates whether this Qualifier is local or propagated'), 'propget'], HRESULT, 'IsLocal',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bIsLocal' )),
    COMMETHOD([dispid(3), helpstring(u'Determines whether this Qualifier can propagate to subclasses'), 'propget'], HRESULT, 'PropagatesToSubclass',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bPropagatesToSubclass' )),
    COMMETHOD([dispid(3), helpstring(u'Determines whether this Qualifier can propagate to subclasses'), 'propput'], HRESULT, 'PropagatesToSubclass',
              ( ['in'], VARIANT_BOOL, 'bPropagatesToSubclass' )),
    COMMETHOD([dispid(4), helpstring(u'Determines whether this Qualifier can propagate to instances'), 'propget'], HRESULT, 'PropagatesToInstance',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bPropagatesToInstance' )),
    COMMETHOD([dispid(4), helpstring(u'Determines whether this Qualifier can propagate to instances'), 'propput'], HRESULT, 'PropagatesToInstance',
              ( ['in'], VARIANT_BOOL, 'bPropagatesToInstance' )),
    COMMETHOD([dispid(5), helpstring(u'Determines whether this Qualifier can be overridden where propagated'), 'propget'], HRESULT, 'IsOverridable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bIsOverridable' )),
    COMMETHOD([dispid(5), helpstring(u'Determines whether this Qualifier can be overridden where propagated'), 'propput'], HRESULT, 'IsOverridable',
              ( ['in'], VARIANT_BOOL, 'bIsOverridable' )),
    COMMETHOD([dispid(6), helpstring(u'Determines whether the value of this Qualifier has been amended'), 'propget'], HRESULT, 'IsAmended',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bIsAmended' )),
]
################################################################
## code template for ISWbemQualifier implementation
##class ISWbemQualifier_Impl(object):
##    def _get(self):
##        u'Determines whether this Qualifier can propagate to subclasses'
##        #return bPropagatesToSubclass
##    def _set(self, bPropagatesToSubclass):
##        u'Determines whether this Qualifier can propagate to subclasses'
##    PropagatesToSubclass = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Determines whether this Qualifier can be overridden where propagated'
##        #return bIsOverridable
##    def _set(self, bIsOverridable):
##        u'Determines whether this Qualifier can be overridden where propagated'
##    IsOverridable = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Name(self):
##        u'The name of this Qualifier'
##        #return strName
##
##    @property
##    def IsLocal(self):
##        u'Indicates whether this Qualifier is local or propagated'
##        #return bIsLocal
##
##    def _get(self):
##        u'The value of this Qualifier'
##        #return varValue
##    def _set(self, varValue):
##        u'The value of this Qualifier'
##    Value = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'Determines whether this Qualifier can propagate to instances'
##        #return bPropagatesToInstance
##    def _set(self, bPropagatesToInstance):
##        u'Determines whether this Qualifier can propagate to instances'
##    PropagatesToInstance = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def IsAmended(self):
##        u'Determines whether the value of this Qualifier has been amended'
##        #return bIsAmended
##

ISWbemObjectSet._methods_ = [
    COMMETHOD([dispid(-4), 'restricted', 'propget'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'pUnk' )),
    COMMETHOD([dispid(0), helpstring(u'Get an Object with a specific path from this collection')], HRESULT, 'Item',
              ( ['in'], BSTR, 'strObjectPath' ),
              ( ['in', 'optional'], c_int, 'iFlags', 0 ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObject)), 'objWbemObject' )),
    COMMETHOD([dispid(1), helpstring(u'The number of items in this collection'), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'iCount' )),
    COMMETHOD([dispid(4), helpstring(u'The Security Configurator for this Object'), 'propget'], HRESULT, 'Security_',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemSecurity)), 'objWbemSecurity' )),
    COMMETHOD([dispid(5), helpstring(u'Get an Object with a specific index from this collection')], HRESULT, 'ItemIndex',
              ( ['in'], c_int, 'lIndex' ),
              ( ['retval', 'out'], POINTER(POINTER(ISWbemObject)), 'objWbemObject' )),
]
################################################################
## code template for ISWbemObjectSet implementation
##class ISWbemObjectSet_Impl(object):
##    @property
##    def Count(self):
##        u'The number of items in this collection'
##        #return iCount
##
##    def Item(self, strObjectPath, iFlags):
##        u'Get an Object with a specific path from this collection'
##        #return objWbemObject
##
##    @property
##    def Security_(self):
##        u'The Security Configurator for this Object'
##        #return objWbemSecurity
##
##    @property
##    def _NewEnum(self):
##        '-no docstring-'
##        #return pUnk
##
##    def ItemIndex(self, lIndex):
##        u'Get an Object with a specific index from this collection'
##        #return objWbemObject
##

class SWbemQualifier(CoClass):
    u'A Qualifier'
    _reg_clsid_ = GUID('{04B83D5F-21AE-11D2-8B33-00600806D9B6}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
SWbemQualifier._com_interfaces_ = [ISWbemQualifier]

ISWbemProperty._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'The value of this Property'), 'propget'], HRESULT, 'Value',
              ( ['retval', 'out'], POINTER(VARIANT), 'varValue' )),
    COMMETHOD([dispid(0), helpstring(u'The value of this Property'), 'propput'], HRESULT, 'Value',
              ( ['in'], POINTER(VARIANT), 'varValue' )),
    COMMETHOD([dispid(1), helpstring(u'The name of this Property'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'strName' )),
    COMMETHOD([dispid(2), helpstring(u'Indicates whether this Property is local or propagated'), 'propget'], HRESULT, 'IsLocal',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bIsLocal' )),
    COMMETHOD([dispid(3), helpstring(u'The originating class of this Property'), 'propget'], HRESULT, 'Origin',
              ( ['retval', 'out'], POINTER(BSTR), 'strOrigin' )),
    COMMETHOD([dispid(4), helpstring(u'The CIM Type of this Property'), 'propget'], HRESULT, 'CIMType',
              ( ['retval', 'out'], POINTER(WbemCimtypeEnum), 'iCimType' )),
    COMMETHOD([dispid(5), helpstring(u'The collection of Qualifiers of this Property'), 'propget'], HRESULT, 'Qualifiers_',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemQualifierSet)), 'objWbemQualifierSet' )),
    COMMETHOD([dispid(6), helpstring(u'Indicates whether this Property is an array type'), 'propget'], HRESULT, 'IsArray',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bIsArray' )),
]
################################################################
## code template for ISWbemProperty implementation
##class ISWbemProperty_Impl(object):
##    @property
##    def Origin(self):
##        u'The originating class of this Property'
##        #return strOrigin
##
##    @property
##    def IsArray(self):
##        u'Indicates whether this Property is an array type'
##        #return bIsArray
##
##    @property
##    def Name(self):
##        u'The name of this Property'
##        #return strName
##
##    @property
##    def IsLocal(self):
##        u'Indicates whether this Property is local or propagated'
##        #return bIsLocal
##
##    def _get(self):
##        u'The value of this Property'
##        #return varValue
##    def _set(self, varValue):
##        u'The value of this Property'
##    Value = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Qualifiers_(self):
##        u'The collection of Qualifiers of this Property'
##        #return objWbemQualifierSet
##
##    @property
##    def CIMType(self):
##        u'The CIM Type of this Property'
##        #return iCimType
##


# values for enumeration 'WbemConnectOptionsEnum'
wbemConnectFlagUseMaxWait = 128
WbemConnectOptionsEnum = c_int # enum
ISWbemPrivilege._methods_ = [
    COMMETHOD([dispid(0), helpstring(u'Whether the Privilege is to be enabled or disabled'), 'propget'], HRESULT, 'IsEnabled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'bIsEnabled' )),
    COMMETHOD([dispid(0), helpstring(u'Whether the Privilege is to be enabled or disabled'), 'propput'], HRESULT, 'IsEnabled',
              ( ['in'], VARIANT_BOOL, 'bIsEnabled' )),
    COMMETHOD([dispid(1), helpstring(u'The name of the Privilege'), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'strDisplayName' )),
    COMMETHOD([dispid(2), helpstring(u'The display name of the Privilege'), 'propget'], HRESULT, 'DisplayName',
              ( ['retval', 'out'], POINTER(BSTR), 'strDisplayName' )),
    COMMETHOD([dispid(3), helpstring(u'The Privilege identifier'), 'propget'], HRESULT, 'Identifier',
              ( ['retval', 'out'], POINTER(WbemPrivilegeEnum), 'iPrivilege' )),
]
################################################################
## code template for ISWbemPrivilege implementation
##class ISWbemPrivilege_Impl(object):
##    def _get(self):
##        u'Whether the Privilege is to be enabled or disabled'
##        #return bIsEnabled
##    def _set(self, bIsEnabled):
##        u'Whether the Privilege is to be enabled or disabled'
##    IsEnabled = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Identifier(self):
##        u'The Privilege identifier'
##        #return iPrivilege
##
##    @property
##    def DisplayName(self):
##        u'The display name of the Privilege'
##        #return strDisplayName
##
##    @property
##    def Name(self):
##        u'The name of the Privilege'
##        #return strDisplayName
##

ISWbemSecurity._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'The security impersonation level'), 'propget'], HRESULT, 'ImpersonationLevel',
              ( ['retval', 'out'], POINTER(WbemImpersonationLevelEnum), 'iImpersonationLevel' )),
    COMMETHOD([dispid(1), helpstring(u'The security impersonation level'), 'propput'], HRESULT, 'ImpersonationLevel',
              ( ['in'], WbemImpersonationLevelEnum, 'iImpersonationLevel' )),
    COMMETHOD([dispid(2), helpstring(u'The security authentication level'), 'propget'], HRESULT, 'AuthenticationLevel',
              ( ['retval', 'out'], POINTER(WbemAuthenticationLevelEnum), 'iAuthenticationLevel' )),
    COMMETHOD([dispid(2), helpstring(u'The security authentication level'), 'propput'], HRESULT, 'AuthenticationLevel',
              ( ['in'], WbemAuthenticationLevelEnum, 'iAuthenticationLevel' )),
    COMMETHOD([dispid(3), helpstring(u'The collection of privileges for this object'), 'propget'], HRESULT, 'Privileges',
              ( ['retval', 'out'], POINTER(POINTER(ISWbemPrivilegeSet)), 'objWbemPrivilegeSet' )),
]
################################################################
## code template for ISWbemSecurity implementation
##class ISWbemSecurity_Impl(object):
##    @property
##    def Privileges(self):
##        u'The collection of privileges for this object'
##        #return objWbemPrivilegeSet
##
##    def _get(self):
##        u'The security impersonation level'
##        #return iImpersonationLevel
##    def _set(self, iImpersonationLevel):
##        u'The security impersonation level'
##    ImpersonationLevel = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        u'The security authentication level'
##        #return iAuthenticationLevel
##    def _set(self, iAuthenticationLevel):
##        u'The security authentication level'
##    AuthenticationLevel = property(_get, _set, doc = _set.__doc__)
##

class SWbemMethod(CoClass):
    u'A Method'
    _reg_clsid_ = GUID('{04B83D5B-21AE-11D2-8B33-00600806D9B6}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
SWbemMethod._com_interfaces_ = [ISWbemMethod]

ISWbemLastError._methods_ = [
]
################################################################
## code template for ISWbemLastError implementation
##class ISWbemLastError_Impl(object):

class SWbemQualifierSet(CoClass):
    u'A collection of Qualifiers'
    _reg_clsid_ = GUID('{04B83D5E-21AE-11D2-8B33-00600806D9B6}')
    _idlflags_ = ['noncreatable']
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{565783C6-CB41-11D1-8B02-00600806D9B6}', 1, 2)
SWbemQualifierSet._com_interfaces_ = [ISWbemQualifierSet]

__all__ = ['wbemPrivilegeShutdown', 'wbemErrProviderNotCapable',
           'wbemErrMissingGroupWithin', 'wbemErrInvalidQualifier',
           'wbemErrTimeout', 'SWbemQualifierSet', 'ISWbemServicesEx',
           'wbemErrUpdateTypeMismatch', 'wbemErrResetToDefault',
           'wbemErrRegistrationTooBroad', 'SWbemLocator',
           'wbemChangeFlagAdvisory', 'wbemErrQueueOverflow',
           'wbemErrCriticalError', 'wbemPrivilegeSystemProfile',
           'wbemErrInvalidNamespace', 'wbemPrivilegeCreateToken',
           'wbemErrTransactionConflict', 'SWbemObjectPath',
           'ISWbemPropertySet', 'ISWbemLastError',
           'ISWbemNamedValueSet', 'SWbemNamedValue', 'ISWbemObject',
           'wbemErrInvalidHandleRequest', 'wbemPrivilegeAudit',
           'wbemErrTooManyProperties', 'wbemErrProviderFailure',
           'wbemErrUninterpretableProviderQuery',
           'wbemErrInvalidQuery', 'wbemErrProviderLoadFailure',
           'wbemErrMethodDisabled', 'wbemQueryFlagDeep',
           'WbemImpersonationLevelEnum', 'wbemErrAlreadyExists',
           'wbemPrivilegeEnableDelegation', 'wbemFlagEnsureLocatable',
           'wbemCimtypeString', 'wbemErrFailed',
           'SWbemRefreshableItem', 'WbemObjectTextFormatEnum',
           'ISWbemDateTime', 'wbemErrInvalidAssociation',
           'wbemCimtypeReal32', 'wbemErrDatabaseVerMismatch',
           'wbemErrUpdatePropagatedMethod', 'wbemErrNotSupported',
           'wbemErrMethodNameTooWide', 'SWbemQualifier',
           'wbemPrivilegeTcb', 'wbemObjectTextFormatCIMDTD20',
           'wbemCimtypeSint8', 'ISWbemObjectPath',
           'wbemFlagUseCurrentTime', 'wbemErrCannotBeSingleton',
           'ISWbemEventSource', 'wbemAuthenticationLevelCall',
           'wbemTextFlagNoFlavors', 'wbemConnectFlagUseMaxWait',
           'wbemErrClassNameTooWide', 'wbemErrVetoPut',
           'WbemAuthenticationLevelEnum', 'wbemPrivilegeLockMemory',
           'wbemErrProviderNotRegistered', 'wbemPrivilegeSecurity',
           'wbemCimtypeUint16', 'wbemCimtypeSint64',
           'wbemComparisonFlagIgnoreFlavor', 'wbemErrServerTooBusy',
           'SWbemObjectEx', 'wbemErrConnectionFailed',
           'wbemPrivilegeBackup', 'wbemErrInvalidLocale',
           'wbemErrUnexpected', 'wbemErrCallCancelled',
           'wbemErrInvalidSuperclass', 'wbemPrivilegeRemoteShutdown',
           'WbemChangeFlagEnum', 'wbemCimtypeUint8',
           'wbemPrivilegeIncreaseBasePriority', 'WbemTextFlagEnum',
           'ISWbemRefreshableItem',
           'wbemComparisonFlagIgnoreQualifiers',
           'wbemErrMissingParameter',
           'wbemChangeFlagStrongValidation', 'SWbemObjectSet',
           'wbemErrTransportFailure', 'wbemPrivilegeSyncAgent',
           'wbemErrInvalidContext', 'wbemErrAccessDenied',
           'wbemErrQualifierNameTooWide', 'wbemErrLocalCredentials',
           'wbemErrHandleOutOfDate',
           'wbemErrBackupRestoreWinmgmtRunning',
           'wbemErrUnsupportedPutExtension',
           'wbemErrUnknownObjectType', 'wbemPrivilegeCreatePagefile',
           'wbemErrInvalidDuplicateParameter',
           'wbemAuthenticationLevelDefault', 'SWbemServices',
           'wbemErrNoSchema', 'wbemErrQuotaViolation',
           'wbemObjectTextFormatWMIDTD20', 'wbemCimtypeUint64',
           'wbemErrInvalidQueryType', 'wbemQueryFlagShallow',
           'SWbemMethodSet', 'wbemFlagReturnErrorObject',
           'wbemPrivilegeChangeNotify', 'wbemErrInvalidMethod',
           'wbemQueryFlagPrototype', 'SWbemPrivilegeSet',
           'wbemErrAmbiguousOperation',
           'wbemComparisonFlagIncludeAll', 'wbemCimtypeDatetime',
           'SWbemPropertySet', 'wbemErrNullSecurityDescriptor',
           'wbemErrShuttingDown', 'wbemErrInvalidCimType',
           'wbemErrInvalidSyntax', 'wbemErrMarshalInvalidSignature',
           'wbemComparisonFlagIgnoreObjectSource',
           'wbemCimtypeBoolean', 'SWbemPrivilege',
           'WbemConnectOptionsEnum', 'wbemErrValueOutOfRange',
           'wbemErrClientTooSlow', 'wbemPrivilegeMachineAccount',
           'ISWbemServices', 'wbemErrUnknownPacketType',
           'WbemCimtypeEnum', 'wbemErrSynchronizationRequired',
           'wbemPrivilegeManageVolume', 'wbemChangeFlagCreateOnly',
           'wbemPrivilegeSystemEnvironment',
           'wbemErrPropertyNameTooWide', 'wbemPrivilegeSystemtime',
           'wbemErrForcedRollback', 'SWbemSecurity',
           'wbemImpersonationLevelDelegate',
           'wbemFlagReturnImmediately', 'wbemErrTimedout',
           'wbemErrProviderNotFound', 'WbemQueryFlagEnum',
           'wbemImpersonationLevelImpersonate', 'wbemFlagForwardOnly',
           'SWbemRefresher', 'wbemErrTooMuchData', 'wbemNoErr',
           'wbemErrRerunCommand', 'wbemErrBufferTooSmall',
           'wbemErrInvalidFlavor', 'wbemCimtypeReal64',
           'wbemErrClassHasInstances', 'wbemErrOutOfMemory',
           'wbemPrivilegeTakeOwnership', 'wbemErrInvalidOperation',
           'SWbemServicesEx', 'wbemErrReadOnly', 'ISWbemLocator',
           'WbemTimeout', 'wbemCimtypeChar16', 'ISWbemProperty',
           'wbemPrivilegeRestore', 'wbemChangeFlagCreateOrUpdate',
           'wbemErrQueryNotImplemented',
           'wbemComparisonFlagIgnoreCase', 'wbemCimtypeSint16',
           'wbemErrCannotChangeKeyInheritance',
           'WbemComparisonFlagEnum', 'ISWbemObjectSet',
           'wbemErrNonConsecutiveParameterIds',
           'wbemErrFatalTransportError',
           'wbemImpersonationLevelIdentify',
           'wbemErrCannotChangeIndexInheritance',
           'wbemErrInvalidProviderRegistration', 'ISWbemNamedValue',
           'WbemPrivilegeEnum', 'ISWbemMethod', 'ISWbemPrivilegeSet',
           'wbemFlagSendOnlySelected', 'ISWbemSink',
           'wbemErrPropagatedProperty', 'wbemErrOverrideNotAllowed',
           'wbemPrivilegeUndock', 'wbemErrNotAvailable',
           'wbemErrRefresherBusy', 'wbemErrMarshalVersionMismatch',
           'wbemChangeFlagUpdateOnly', 'wbemPrivilegeLoadDriver',
           'wbemAuthenticationLevelPktIntegrity',
           'wbemErrProviderAlreadyRegistered', 'ISWbemQualifier',
           'wbemFlagGetDefault', 'wbemFlagReturnWhenComplete',
           'wbemChangeFlagUpdateCompatible', 'wbemFlagBidirectional',
           'wbemErrInvalidParameter', 'wbemErrInvalidParameterId',
           'wbemErrUnsupportedClassUpdate', 'wbemFlagNoErrorObject',
           'wbemErrUpdateOverrideNotAllowed',
           'wbemFlagDontSendStatus', 'wbemChangeFlagUpdateForceMode',
           'wbemErrMissingAggregationList', 'ISWbemRefresher',
           'wbemFlagUseAmendedQualifiers', 'wbemErrCircularReference',
           'ISWbemSecurity', 'wbemErrInvalidObject',
           'wbemErrUnsupportedLocale', 'wbemErrNotEventClass',
           'wbemErrMethodNotImplemented', 'wbemErrProviderSuspended',
           'wbemErrRegistrationTooPrecise', 'wbemCimtypeObject',
           'wbemErrUnparsableQuery', 'wbemErrClassHasChildren',
           'wbemErrPrivilegeNotHeld', 'wbemErrPropagatedMethod',
           'SWbemSink', 'wbemErrPropagatedQualifier',
           'wbemAuthenticationLevelPkt',
           'wbemPrivilegeProfileSingleProcess', 'wbemErrVetoDelete',
           'wbemComparisonFlagIgnoreClass',
           'wbemPrivilegeCreatePermanent',
           'wbemErrPropertyNotAnObject', 'wbemErrInvalidStream',
           'wbemFlagSpawnInstance',
           'wbemErrEncryptedConnectionRequired', 'ISWbemMethodSet',
           'WbemFlagEnum', 'wbemAuthenticationLevelConnect',
           'SWbemMethod', 'wbemErrNondecoratedObject',
           'wbemErrInitializationFailure', 'wbemErrTypeMismatch',
           'wbemErrAggregatingByObject',
           'wbemAuthenticationLevelPktPrivacy', 'wbemFlagDirectRead',
           'ISWbemObjectEx', 'wbemPrivilegeDebug',
           'wbemErrInvalidProperty', 'ISWbemQualifierSet',
           'SWbemProperty', 'wbemErrCannotBeAbstract',
           'ISWbemSinkEvents', 'wbemErrInvalidClass',
           'wbemPrivilegePrimaryToken', 'wbemCimtypeReference',
           'wbemErrInvalidQualifierType', 'SWbemDateTime',
           'wbemPrivilegeIncreaseQuota',
           'wbemErrInvalidMethodParameters', 'wbemErrIllegalNull',
           'wbemErrAmendedObject', 'wbemTimeoutInfinite',
           'wbemErrSystemProperty', 'wbemErrOutOfDiskSpace',
           'wbemErrIllegalOperation', 'wbemErrUnsupportedParameter',
           'wbemAuthenticationLevelNone',
           'wbemComparisonFlagIgnoreDefaultValues', 'SWbemObject',
           'ISWbemPrivilege', 'wbemErrInvalidObjectPath',
           'SWbemNamedValueSet', 'wbemImpersonationLevelAnonymous',
           'WbemErrorEnum', 'wbemCimtypeUint32', 'wbemFlagSendStatus',
           'wbemChangeFlagUpdateSafeMode',
           'wbemErrParameterIdOnRetval', 'wbemErrIncompleteClass',
           'wbemErrCannotBeKey', 'wbemErrInvalidOperator',
           'wbemErrInvalidPropertyType', 'SWbemLastError',
           'wbemErrNotFound', 'SWbemEventSource', 'wbemCimtypeSint32']
from comtypes import _check_version; _check_version('')

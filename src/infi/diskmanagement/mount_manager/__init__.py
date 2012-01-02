
from ..ioctl import DeviceIoControl, generate_signature, generate_guid, structures, constants
from ..ioctl.constants import PARTITION_STYLE_MBR, PARTITION_STYLE_GPT, PARTITION_STYLE_RAW
from infi.diskmanagement.ioctl import GUID_ZERO, _sizeof
from infi.instruct import Struct, BitFields, BitField, BitPadding, ULInt32
from string import ascii_uppercase
import ctypes

class AVAILABLE_DRIVE_LETTERS(Struct):
    _fields_ = BitFields(*([BitField(letter, 1) for letter in ascii_uppercase] + [BitPadding(6), ]))

def _slice_unicode_string_from_buffer(buffer, offset, length):
    return ctypes.wstring_at(ctypes.addressof(buffer) + offset, length / ctypes.sizeof(ctypes.c_wchar))

class MountManager(object):
    def __init__(self):
        super(MountManager, self).__init__()
        self._path = r"\\.\MountPointManager"
        self._io = DeviceIoControl(self._path, True)

    def __repr__(self):
        return "MountManager <{}>".format(self._path)

    def get_avaialable_drive_letters(self):
        import ctypes
        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        struct = AVAILABLE_DRIVE_LETTERS.create_from_string(ULInt32.write_to_string(bitmask))
        return filter(lambda letter: getattr(struct, letter) == 0,
                      [field.name for field in struct._fields_.fields[0:26]])

    def _create_input_buffer_for_query_points_ioctl(self, volume):
        device_name = r"\Device\{}".format(volume._path.split('\\')[-1])
        unicode_buffer = ctypes.create_unicode_buffer(device_name)
        from os.path import sep
        buffer_string = ctypes.string_at(ctypes.addressof(unicode_buffer),
                                         len(unicode_buffer) * ctypes.sizeof(ctypes.c_wchar))
        triplet = structures.MOUNTMGR_MOUNT_POINT(SymbolicLinkNameOffset=0, SymbolicLinkNameLength=0,
                                                  UniqueIdOffset=0, UniqueIdLength=0,
                                                  DeviceNameOffset=_sizeof(structures.MOUNTMGR_MOUNT_POINT),
                                                  DeviceNameLength=len(buffer_string) - ctypes.sizeof(ctypes.c_wchar))
        triplet_string = structures.MOUNTMGR_MOUNT_POINT.write_to_string(triplet)
        input_buffer = ctypes.c_buffer(triplet_string + buffer_string, len(triplet_string) + len(buffer_string))
        return input_buffer

    def get_volume_guid(self, volume):
        input_buffer = self._create_input_buffer_for_query_points_ioctl(volume)
        output_buffer = self._io.ioctl_mountmgr_query_points(input_buffer, len(input_buffer) + 1)
        struct = structures.MOUNTMGR_MOUNT_POINTS.create_from_string(output_buffer)
        offset, length = struct.MountPoints[0].SymbolicLinkNameOffset, struct.MountPoints[0].SymbolicLinkNameLength
        return _slice_unicode_string_from_buffer(output_buffer, offset, length).replace(r"\?", r"\\")

    def get_volume_drive_letter(self, volume):
        input_buffer = self._create_input_buffer_for_query_points_ioctl(volume)
        output_buffer = self._io.ioctl_mountmgr_query_points(input_buffer, len(input_buffer) + 1)
        struct = structures.MOUNTMGR_MOUNT_POINTS.create_from_string(output_buffer)
        if len(struct.MountPoints) != 2:
            return None
        offset, length = struct.MountPoints[1].SymbolicLinkNameOffset, struct.MountPoints[1].SymbolicLinkNameLength
        return _slice_unicode_string_from_buffer(output_buffer, offset, length).split('\\')[-1][0]

    def get_volume_mount_points(self, volume):
        volume_guid = u"{}\\".format(self.get_volume_guid(volume))
        volumePathNames = create_unicode_buffer(MAX_PATH_NAMES)
        returnLength = DWORD(0)
        GetVolumePathNamesForVolumeNameW(volumeName=volume_guid, volumePathNames=volumePathNames,
                                         returnLength=returnLength)
        return ctypes.wstring_at(ctypes.addressof(volumePathNames),
                                 returnLength.value).split(u"\x00"*ctypes.sizeof(ctypes.c_wchar))

class PartitionManager(object):
    def __init__(self):
        super(MountManager, self).__init__()
        self._path = r"\\.\PartmgrControl"
        self._io = DeviceIoControl(self._path, True)

    def __repr__(self):
        return "PartitionManager <{}>".format(self._path)

    def get_san_policy(self):
        return self._io.ioctl_disk_get_san_settings().SanPolicy

    def set_san_policy(self, san_policy):
        settings = structures.DISK_SAN_SETTINGS(SanPolicy=san_policy)
        return self._io.ioctl_disk_set_san_settings(settings)

import infi.wioctl
from infi.crap import WrappedFunction, IN, IN_OUT, OUT
from ctypes import c_wchar_p as LPCWSTR
from ctypes import c_wchar_p as LPWSTR
from ctypes import c_ulong as DWORD
from ctypes import POINTER, create_unicode_buffer

MAX_PATH_NAMES = 32767

class GetVolumePathNamesForVolumeNameW(WrappedFunction):
    return_value = infi.wioctl.api.BOOL

    @classmethod
    def get_errcheck(cls):
        return infi.wioctl.api.errcheck_bool()

    @classmethod
    def get_library_name(cls):
        return 'kernel32'

    @classmethod
    def get_parameters(cls):
        return ((LPCWSTR, IN, "volumeName"),
                (LPWSTR, IN_OUT, "volumePathNames"),
                (DWORD, IN, "bufferLength", DWORD(MAX_PATH_NAMES)),
                (POINTER(DWORD), IN_OUT, "returnLength"))

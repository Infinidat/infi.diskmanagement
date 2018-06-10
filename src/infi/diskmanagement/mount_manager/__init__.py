
from ..ioctl import DeviceIoControl, generate_signature, generate_guid, structures, constants
from ..ioctl.constants import PARTITION_STYLE_MBR, PARTITION_STYLE_GPT, PARTITION_STYLE_RAW
from ..ioctl.constants import MOUNTMGR_AUTO_MOUNT_STATE_DISABLED, MOUNTMGR_AUTO_MOUNT_STATE_ENABLED
from infi.pyutils.lazy import cached_method
from infi.diskmanagement.ioctl import GUID_ZERO, _sizeof
from infi.instruct import Struct, BitFields, BitField, BitPadding, ULInt32
from string import ascii_uppercase
import ctypes

MAX_PATH_NAMES = 32767


class AVAILABLE_DRIVE_LETTERS(Struct):
    _fields_ = BitFields(*([BitField(letter, 1) for letter in ascii_uppercase] + [BitPadding(6), ]))


def _slice_unicode_string_from_buffer(buffer, offset, length):
    return ctypes.wstring_at(ctypes.addressof(buffer) + offset, length / ctypes.sizeof(ctypes.c_wchar))


def _rstrip(string):
    return string.rstrip(u'\\')


def _get_unicode_buffer(size=MAX_PATH_NAMES):
    buffer = create_unicode_buffer(size)
    return buffer, size


class MountManager(object):
    def __init__(self):
        super(MountManager, self).__init__()
        self._path = r"\\.\MountPointManager"
        self._io = DeviceIoControl(self._path, True)

    def __repr__(self):
        return "MountManager <{}>".format(self._path)

    def get_avaialable_drive_letters(self):
        bitmask = ctypes.windll.kernel32.GetLogicalDrives()
        struct = AVAILABLE_DRIVE_LETTERS.create_from_string(ULInt32.write_to_string(bitmask))
        return [u"{}:\\".format(letter) for letter in
                [letter for letter in
                    [field.name for field in struct._fields_.fields[2:26]]
                    if getattr(struct, letter) == 0]
               ]

    def _create_input_buffer_for_query_points_ioctl(self, volume):
        volume_partition_number = getattr(volume, "_partition_number", volume)
        device_name = r"\Device\HarddiskVolume{}".format(volume_partition_number)
        unicode_buffer = ctypes.create_unicode_buffer(device_name)
        buffer_string = ctypes.string_at(ctypes.addressof(unicode_buffer),
                                         len(unicode_buffer) * ctypes.sizeof(ctypes.c_wchar))
        triplet = structures.MOUNTMGR_MOUNT_POINT(SymbolicLinkNameOffset=0, SymbolicLinkNameLength=0,
                                                  UniqueIdOffset=0, UniqueIdLength=0,
                                                  DeviceNameOffset=_sizeof(structures.MOUNTMGR_MOUNT_POINT),
                                                  DeviceNameLength=len(buffer_string) - ctypes.sizeof(ctypes.c_wchar))
        triplet_string = structures.MOUNTMGR_MOUNT_POINT.write_to_string(triplet)
        input_buffer = ctypes.c_buffer(triplet_string + buffer_string, len(triplet_string) + len(buffer_string))
        return input_buffer

    def _iter_volume_mount_points(self, volume):
        input_buffer = self._create_input_buffer_for_query_points_ioctl(volume)
        output_buffer = self._io.ioctl_mountmgr_query_points(input_buffer, len(input_buffer) + 1)
        struct = structures.MOUNTMGR_MOUNT_POINTS.create_from_string(output_buffer)
        for item in struct.MountPoints:
            offset, length = item.SymbolicLinkNameOffset, item.SymbolicLinkNameLength
            yield _slice_unicode_string_from_buffer(output_buffer, offset, length)

    def get_volume_drive_letter(self, volume):
        for item in self._iter_volume_mount_points(volume):
            if "DosDevices\\" in item:
                return item.split('\\')[-1][0]

    def get_volume_mount_points(self, volume_guid):
        if not volume_guid.endswith('\\'):
            volume_guid = u"{}\\".format(volume_guid)
        volumePathNames = create_unicode_buffer(MAX_PATH_NAMES)
        returnLength = DWORD(0)
        GetVolumePathNamesForVolumeNameW(volumeName=volume_guid, volumePathNames=volumePathNames,
                                         returnLength=returnLength)
        return [string for string in
                ctypes.wstring_at(ctypes.addressof(volumePathNames), returnLength.value).split(u"\x00")
                if string != u'']

    def add_volume_mount_point(self, volume_guid, mount_point):
        if not volume_guid.endswith('\\'):
            volume_guid = u"{}\\".format(volume_guid)
        SetVolumeMountPointW(create_unicode_buffer(mount_point), create_unicode_buffer(volume_guid))

    def remove_mount_point(self, volume_guid, mount_point):
        if not mount_point.endswith('\\'):
            mount_point = u"{}\\".format(mount_point)
        mount_points = self.get_volume_mount_points(volume_guid)
        assert mount_point in mount_points, "{} is not a mount point".format(mount_point)
        DeleteVolumeMountPointW(create_unicode_buffer(mount_point))

    def get_volume_label(self, mount_point):
        if not mount_point.endswith('\\'):
            mount_point = u"{}\\".format(mount_point)
        volume_name = create_unicode_buffer(MAX_PATH_NAMES)
        volume_name_size = DWORD(MAX_PATH_NAMES)
        GetVolumeInformationW(rootPathName=mount_point,
                              volumeNameBuffer=volume_name, volumeNameSize=volume_name_size,
                              volumeSerialNumber=None, maximumComponentLength=None, fileSystemFlags=None,
                              fileSystemNameBuffer=None, fileSystemNameSize=DWORD(0))
        return ctypes.wstring_at(ctypes.addressof(volume_name))

    def set_volume_label(self, mount_point, label):
        """:raises: `OverflowError if the label is too big"""
        if not mount_point.endswith('\\'):
            mount_point = u"{}\\".format(mount_point)
        try:
            SetVolumeLabelW(rootPathName=create_unicode_buffer(mount_point),
                            volumeName=create_unicode_buffer(label))
        except WindowsException as e:
            raise

    def is_auto_mount(self):
        return self._io.ioctl_mountmgr_query_auto_mount() == MOUNTMGR_AUTO_MOUNT_STATE_ENABLED

    def enable_auto_mount(self):
        return self._io.ioctl_mountmgr_set_auto_mount(MOUNTMGR_AUTO_MOUNT_STATE_ENABLED)

    def disable_auto_mount(self):
        return self._io.ioctl_mountmgr_set_auto_mount(MOUNTMGR_AUTO_MOUNT_STATE_DISABLED)

    @cached_method
    def get_volume_extents(self, volume_guid):
        return DeviceIoControl(volume_guid, False).ioctl_volume_get_volume_disk_extents().Extents

    @cached_method
    def get_volume_guids(self):
        return list(self.iter_volume_guids())

    def iter_volume_guids(self):
        buffer, length = _get_unicode_buffer()
        search_handle = None
        try:
            search_handle = FindFirstVolumeW(buffer, length)
            while True:
                if buffer.value:
                    yield buffer.value
                FindNextVolumeW(search_handle, buffer, length)
        except WindowsException as e:
            if e.winerror != ERROR_NO_MORE_FILES:
                raise
        finally:
            if search_handle is not None:
                FindVolumeClose(search_handle)

    def get_mounts_of_all_volumes(self):
        """:returns: a dictionary with volume GUIDs as keys and list of mount points as values"""
        return {_rstrip(volume_guid): self.get_volume_mount_points(volume_guid) \
                for volume_guid in self.iter_volume_guids()}

class PartitionManager(object):
    def __init__(self):
        super(PartitionManager, self).__init__()
        self._path = r"\\.\PartmgrControl"
        self._io = DeviceIoControl(self._path, True)

    def __repr__(self):
        return "PartitionManager <{}>".format(self._path)

    def get_san_policy(self):
        return self._io.ioctl_disk_get_san_settings().SanPolicy

    def set_san_policy(self, san_policy):
        version = self._io.ioctl_disk_get_san_settings().Version
        settings = structures.DISK_SAN_SETTINGS(Version=version, SanPolicy=san_policy)
        return self._io.ioctl_disk_set_san_settings(settings)

import infi.wioctl
from infi.cwrap import WrappedFunction, IN, IN_OUT, OUT
from ctypes import c_wchar_p as LPCWSTR
from ctypes import c_wchar_p as LPWSTR
from ctypes import c_ulong as DWORD
from ctypes import POINTER, create_unicode_buffer

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


class SetVolumeMountPointW(WrappedFunction):
    return_value = infi.wioctl.api.BOOL

    @classmethod
    def get_errcheck(cls):
        return infi.wioctl.api.errcheck_bool()

    @classmethod
    def get_library_name(cls):
        return 'kernel32'

    @classmethod
    def get_parameters(cls):
        return ((LPCWSTR, IN, "volumeMountPoint"),
                (LPCWSTR, IN, "volumeName"))


class DeleteVolumeMountPointW(WrappedFunction):
    return_value = infi.wioctl.api.BOOL

    @classmethod
    def get_errcheck(cls):
        return infi.wioctl.api.errcheck_bool()

    @classmethod
    def get_library_name(cls):
        return 'kernel32'

    @classmethod
    def get_parameters(cls):
        return ((LPCWSTR, IN, "volumeMountPoint"),)


from infi.wioctl.api import HANDLE, errcheck_invalid_handle, WindowsException


class FindFirstVolumeW(WrappedFunction):
    return_value = HANDLE

    @classmethod
    def get_errcheck(cls):
        return errcheck_invalid_handle()

    @classmethod
    def get_library_name(cls):
        return 'kernel32'

    @classmethod
    def get_parameters(cls):
        return ((LPCWSTR, IN_OUT, "volumeName"),
                (DWORD, IN, "bufferLength"))


class FindVolumeClose(WrappedFunction):
    return_value = HANDLE

    @classmethod
    def get_errcheck(cls):
        return errcheck_invalid_handle()

    @classmethod
    def get_library_name(cls):
        return 'kernel32'

    @classmethod
    def get_parameters(cls):
        return ((HANDLE, IN, "findVolume"),)


class FindNextVolumeW(WrappedFunction):
    return_value = infi.wioctl.api.BOOL

    @classmethod
    def get_errcheck(cls):
        return infi.wioctl.api.errcheck_bool()

    @classmethod
    def get_library_name(cls):
        return 'kernel32'

    @classmethod
    def get_parameters(cls):
        return ((HANDLE, IN, "findVolume"),
                (LPWSTR, IN_OUT, "volumeName"),
                (DWORD, IN, "bufferLength"))

ERROR_NO_MORE_FILES = 18


class FindFirstVolumeMountPointW(WrappedFunction):
    return_value = HANDLE

    @classmethod
    def get_errcheck(cls):
        return errcheck_invalid_handle()

    @classmethod
    def get_library_name(cls):
        return 'kernel32'

    @classmethod
    def get_parameters(cls):
        return ((LPWSTR, IN, "rootPathName"),
                (LPWSTR, IN_OUT, "volumeMountPoint"),
                (DWORD, IN, "bufferLength"))


class FindVolumeMountPointClose(WrappedFunction):
    return_value = HANDLE

    @classmethod
    def get_errcheck(cls):
        return errcheck_invalid_handle()

    @classmethod
    def get_library_name(cls):
        return 'kernel32'

    @classmethod
    def get_parameters(cls):
        return ((HANDLE, IN, "findVolumeMountPoint"),)


class FindNextVolumeMountPointW(WrappedFunction):
    return_value = infi.wioctl.api.BOOL

    @classmethod
    def get_errcheck(cls):
        return infi.wioctl.api.errcheck_bool()

    @classmethod
    def get_library_name(cls):
        return 'kernel32'

    @classmethod
    def get_parameters(cls):
        return ((HANDLE, IN, "findVolumeMountPoint"),
                (LPWSTR, IN_OUT, "volumeMountPoint"),
                (DWORD, IN, "bufferLength"))


class GetVolumeInformationW(WrappedFunction):
    return_value = infi.wioctl.api.BOOL

    @classmethod
    def get_errcheck(cls):
        return errcheck_invalid_handle()

    @classmethod
    def get_library_name(cls):
        return 'kernel32'

    @classmethod
    def get_parameters(cls):
        return ((LPWSTR, IN, "rootPathName"),
                (LPWSTR, IN_OUT, "volumeNameBuffer"),
                (DWORD, IN, "volumeNameSize"),
                (POINTER(DWORD), IN_OUT, "volumeSerialNumber"),
                (POINTER(DWORD), IN_OUT, "maximumComponentLength"),
                (POINTER(DWORD), IN_OUT, "fileSystemFlags"),
                (LPWSTR, IN_OUT, "fileSystemNameBuffer"),
                (DWORD, IN, "fileSystemNameSize"))


class SetVolumeLabelW(WrappedFunction):
    return_value = infi.wioctl.api.BOOL

    @classmethod
    def get_errcheck(cls):
        return infi.wioctl.api.errcheck_bool()

    @classmethod
    def get_library_name(cls):
        return 'kernel32'

    @classmethod
    def get_parameters(cls):
        return ((HANDLE, IN, "rootPathName"),
                (LPWSTR, IN, "volumeName"),)

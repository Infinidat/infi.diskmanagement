
from ..ioctl import DeviceIoControl, generate_signature, generate_guid, structures, constants
from ..ioctl.constants import PARTITION_STYLE_MBR, PARTITION_STYLE_GPT, PARTITION_STYLE_RAW
from infi.diskmanagement.ioctl import GUID_ZERO
from infi.instruct import Struct, BitFields, BitField, BitPadding, ULInt32
from string import ascii_uppercase

class AVAILABLE_DRIVE_LETTERS(Struct):
    _fields_ = BitFields(*([BitField(letter, 1) for letter in ascii_uppercase] + [BitPadding(6), ]))

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


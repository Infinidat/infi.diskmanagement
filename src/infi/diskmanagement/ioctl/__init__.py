
import ctypes
import infi.wioctl
from . import constants
from . import structures

def _sizeof(struct):
    return struct.min_max_sizeof().max

def _extract_whole_structure_from_drive_layout_buffer(string):
    instance = structures.DRIVE_LAYOUT_INFORMATION_EX.create_from_string(string)
    return instance

class CoCreateGuid(infi.wioctl.api.WrappedFunction):
    return_value = infi.wioctl.api.BOOL

    @classmethod
    def get_errcheck(cls):
        return infi.wioctl.api.errcheck_bool()

    @classmethod
    def get_library_name(cls):
        return 'ole32'

    @classmethod
    def get_parameters(cls):
        return ((infi.wioctl.api.c_void_p, infi.wioctl.api.IN_OUT, "guid"),
                )

def generate_guid():
    size = _sizeof(infi.wioctl.structures.GUID)
    buffer = ctypes.c_buffer('\x00' * size)
    ctypes.windll.LoadLibrary("ole32.dll").CoCreateGuid(buffer)
    return infi.wioctl.structures.GUID.create_from_string(buffer)

def generate_signature():
    import random
    return random.randint(0, 2 ** 32 - 1)

GUID_ZERO = infi.wioctl.structures.GUID.create_from_string(ctypes.c_buffer('\x00' * 16))

class DeviceIoControl(infi.wioctl.DeviceIoControl):
    def _partial_ioctl_diks_get_drive_layout_ex(self, size=24):
        """:returns: a `ctypes.c_buffer` object"""
        # http://msdn.microsoft.com/en-us/library/windows/hardware/ff560364(v=VS.85).aspx
        # To determine the size of output buffer that is required, 
        # caller should send this IOCTL request in a loop. 
        # Every time the storage stack rejects the IOCTL with an error message indicating that the buffer was too small,
        # caller should double the buffer size.
        buffer = ctypes.c_buffer('\x00' * size, size)
        try:
            self.ioctl(infi.wioctl.constants.IOCTL_DISK_GET_DRIVE_LAYOUT_EX, 0, 0, buffer, size)
        except infi.wioctl.api.WindowsException, e:
            if e.winerror != infi.wioctl.constants.ERROR_INSUFFICIENT_BUFFER:
                raise
            return self._partial_ioctl_diks_get_drive_layout_ex(size * 2)
        return buffer

    def ioctl_disk_get_drive_layout_ex(self):
        buffer = self._partial_ioctl_diks_get_drive_layout_ex()
        return _extract_whole_structure_from_drive_layout_buffer(buffer)

    def ioctl_disk_set_drive_layout_ex(self, layout):
        size = layout.sizeof(layout)
        input_buffer = ctypes.c_buffer(layout.write_to_string(layout))
        output_buffer = ctypes.c_buffer('\x00' * size, size)
        self.ioctl(infi.wioctl.constants.IOCTL_DISK_SET_DRIVE_LAYOUT_EX, input_buffer, size, output_buffer, size)

    def ioctl_disk_delete_drive_layout(self):
        self.ioctl(infi.wioctl.constants.IOCTL_DISK_DELETE_DRIVE_LAYOUT, 0, 0, 0, 0)

    def ioctl_disk_create_disk(self, partition_style):
        """:param partition_style: int
        :param signature: int
        :param disk_id: 16-byte string
        :param max_partition_count: int"""
        struct = structures.CREATE_DISK()
        struct.PartitionStyle = partition_style
        if struct.PartitionStyle == constants.PARTITION_STYLE_MBR:
            klass = structures.CREATE_DISK_MBR
            union = klass()
            union.Signature = generate_signature()
        else:
            klass = structures.CREATE_DISK_GPT
            union = klass()
            union.DiskId = generate_guid()
            union.MaxPartitionCount = 128
        struct.union = union
        size = _sizeof(struct)
        buffer = ctypes.c_buffer(structures.CREATE_DISK.write_to_string(struct), size)
        self.ioctl(infi.wioctl.constants.IOCTL_DISK_CREATE_DISK, buffer, size, 0, 0)

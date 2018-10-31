
import ctypes
import infi.wioctl
import infi.cwrap
from . import constants
from . import structures

# pylint: disable=W0622

def _sizeof(struct):
    return struct.min_max_sizeof().max

def _extract_whole_structure_from_drive_layout_buffer(string):
    instance = structures.DRIVE_LAYOUT_INFORMATION_EX.create_from_string(string)
    return instance


class CoCreateGuid(infi.wioctl.api.WrappedFunction):
    return_value = infi.wioctl.api.BOOL

    @classmethod
    def get_errcheck(cls):
        return infi.cwrap.errcheck_nonzero()

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
    CoCreateGuid(buffer)
    return infi.wioctl.structures.GUID.create_from_string(buffer)

def generate_signature():
    import random
    return random.randint(0, 2 ** 32 - 1)

GUID_ZERO = infi.wioctl.structures.GUID.create_from_string(b'\x00' * 16)


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
        except infi.wioctl.api.WindowsException as e:
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

    def _bool_ioctl(self, ioctl_number):
        try:
            self.ioctl(ioctl_number, 0, 0, 0, 0)
        except infi.wioctl.api.WindowsException as e:
            if e.winerror != 1:
                raise
            return False
        return True

    def ioctl_volume_is_partition(self):
        return self._bool_ioctl(infi.wioctl.constants.IOCTL_VOLUME_IS_PARTITION)

    def ioctl_volume_is_offline(self):
        return self._bool_ioctl(infi.wioctl.constants.IOCTL_VOLUME_IS_OFFLINE)

    def ioctl_volume_supports_online_offline(self):
        return self._bool_ioctl(infi.wioctl.constants.IOCTL_VOLUME_SUPPORTS_ONLINE_OFFLINE)

    def ioctl_volume_is_io_capable(self):
        return self._bool_ioctl(infi.wioctl.constants.IOCTL_VOLUME_IS_IO_CAPABLE)

    def ioctl_volume_online(self):
        return self._bool_ioctl(infi.wioctl.constants.IOCTL_VOLUME_ONLINE)

    def ioctl_volume_offline(self):
        return self._bool_ioctl(infi.wioctl.constants.IOCTL_VOLUME_OFFLINE)

    def ioctl_disk_get_disk_attributes(self):
        klass = structures.GET_DISK_ATTRIBUTES
        size = _sizeof(klass)
        buffer = ctypes.c_buffer('\x00' * size, size)
        self.ioctl(infi.wioctl.constants.IOCTL_DISK_GET_DISK_ATTRIBUTES, 0, 0, buffer, size)
        return klass.create_from_string(buffer)

    def ioctl_disk_set_disk_attributes(self, attributes):
        size = attributes.sizeof(attributes)
        input_buffer = ctypes.c_buffer(attributes.write_to_string(attributes))
        self.ioctl(infi.wioctl.constants.IOCTL_DISK_SET_DISK_ATTRIBUTES, input_buffer, size, 0, 0)

    def ioctl_disk_get_san_settings(self):
        klass = structures.DISK_SAN_SETTINGS
        size = _sizeof(klass)
        buffer = ctypes.c_buffer('\x00' * size, size)
        self.ioctl(infi.wioctl.constants.IOCTL_DISK_GET_SAN_SETTINGS, 0, 0, buffer, size)
        return klass.create_from_string(buffer)

    def ioctl_disk_set_san_settings(self, settings):
        klass = structures.DISK_SAN_SETTINGS
        size = _sizeof(klass)
        buffer = ctypes.c_buffer(settings.write_to_string(settings))
        self.ioctl(infi.wioctl.constants.IOCTL_DISK_SET_SAN_SETTINGS, buffer, size, 0, 0)

    def ioctl_volume_query_volume_number(self):
        klass = structures.VOLUME_NUMBER
        size = _sizeof(klass)
        buffer = ctypes.c_buffer('\x00' * size, size)
        self.ioctl(infi.wioctl.constants.IOCTL_VOLUME_QUERY_VOLUME_NUMBER, 0, 0, buffer, size)
        return klass.create_from_string(buffer)

    def _partial_ioctl_volume_get_volume_disk_extents(self, size):
        klass = structures.VOLUME_DISK_EXTENTS
        buffer = ctypes.c_buffer('\x00' * size, size)
        try:
            self.ioctl(infi.wioctl.constants.IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS, 0, 0, buffer, size)
        except infi.wioctl.api.WindowsException as e:
            if e.winerror != infi.wioctl.constants.ERROR_MORE_DATA:
                raise
            return self._partial_ioctl_volume_get_volume_disk_extents(size + _sizeof(structures.DISK_EXTENT))
        return klass.create_from_string(buffer)

    def ioctl_volume_get_volume_disk_extents(self):
        size = _sizeof(structures.DISK_EXTENT) + ctypes.sizeof(ctypes.c_ulong) + 4
        return self._partial_ioctl_volume_get_volume_disk_extents(size)

    def _partial_ioctl_mountmgr_query_points(self, input_buffer, input_buffer_size, size=256):
        """:returns: a `ctypes.c_buffer` object"""
        buffer = ctypes.c_buffer('\x00' * size, size)
        try:
            self.ioctl(infi.wioctl.constants.IOCTL_MOUNTMGR_QUERY_POINTS, input_buffer, input_buffer_size, buffer, size)
        except infi.wioctl.api.WindowsException as e:
            if e.winerror != infi.wioctl.constants.ERROR_MORE_DATA:
                raise
            return self._partial_ioctl_mountmgr_query_points(input_buffer, input_buffer_size, size * 2)
        return buffer

    def ioctl_mountmgr_query_points(self, input_buffer, input_buffer_size):
        return self._partial_ioctl_mountmgr_query_points(input_buffer, input_buffer_size)

    def ioctl_mountmgr_query_auto_mount(self):
        klass = structures.MOUNTMGR_QUERY_AUTO_MOUNT
        size = _sizeof(klass)
        buffer = ctypes.c_buffer('\x00' * size, size)
        self.ioctl(infi.wioctl.constants.IOCTL_MOUNTMGR_QUERY_AUTO_MOUNT, 0, 0, buffer, size)
        return klass.create_from_string(buffer).CurrentState

    def ioctl_mountmgr_set_auto_mount(self, state):
        klass = structures.MOUNTMGR_SET_AUTO_MOUNT
        size = _sizeof(klass)
        buffer = ctypes.c_buffer(klass.write_to_string(klass(NewState=state)))
        self.ioctl(infi.wioctl.constants.IOCTL_MOUNTMGR_SET_AUTO_MOUNT, buffer, size, 0, 0)

    def ioctl_disk_grow_partition(self, grow_struct):
        size = grow_struct.sizeof(grow_struct)
        input_buffer = ctypes.c_buffer(structures.DISK_GROW_PARTITION.write_to_string(grow_struct))
        self.ioctl(infi.wioctl.constants.IOCTL_DISK_GROW_PARTITION, input_buffer, size, 0, 0)

    def ioctl_extend_volume(self, new_size):
        size_in_sectors = ctypes.c_longlong(new_size / 512)
        self.ioctl(infi.wioctl.constants.FSCTL_EXTEND_VOLUME,
                   ctypes.byref(size_in_sectors),
                   ctypes.sizeof(size_in_sectors), 0, 0)

    def ioctl_disk_update_drive_size(self):
        size = _sizeof(structures.DISK_GEOMETRY)
        buffer = ctypes.c_buffer('\x00' * size, size)
        try:
            self.ioctl(infi.wioctl.constants.IOCTL_DISK_UPDATE_DRIVE_SIZE, 0, 0, buffer, size)
        except infi.wioctl.api.WindowsException as e:
            if e.winerror == infi.wioctl.constants.ERROR_INSUFFICIENT_BUFFER:
                return
            raise

    def ioctl_disk_update_properties(self):
        self.ioctl(infi.wioctl.constants.IOCTL_DISK_UPDATE_PROPERTIES, 0, 0, 0, 0)

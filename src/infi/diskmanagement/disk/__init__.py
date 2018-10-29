from capacity import byte, MiB
from infi.pyutils.lazy import cached_method, clear_cache
from infi.pyutils.decorators import wraps
from ..ioctl import DeviceIoControl, generate_signature, generate_guid, structures, constants
from ..ioctl.constants import PARTITION_STYLE_MBR, PARTITION_STYLE_GPT, PARTITION_STYLE_RAW
from infi.diskmanagement.ioctl import GUID_ZERO
from infi.wioctl.structures import is_64bit, GUID
from ..mount_manager import MountManager
from infi.devicemanager import DeviceManager
from logging import getLogger

logger = getLogger(__name__)

def is_zero(large_integer):
    """:returns: if the value of LARGE_INTEGER is zero"""
    if len(large_integer._fields_) == 1:
        return large_integer.QuadPart == 0
    return large_integer.LowPart == 0 and large_integer.HighPart == 0

# http://msdn.microsoft.com/en-us/windows/hardware/gg463525
PARTITION_BASIC_DATA_GUID = GUID(Data1=0xEBD0A0A2, Data2=0xB9E5, Data3=0x4433,
                                 Data4=[0x87, 0xC0, 0x68, 0xB6, 0xB7, 0x26, 0x99, 0xC7])
PARTITION_MSFT_RESERVED_GUID = GUID(Data1=0xE3C9E316, Data2=0x0B5C, Data3=0x4DB8,
                                    Data4=[0x81, 0x7D, 0xF9, 0x2D, 0xF0, 0x02, 0x15, 0xAE])
# https://docs.microsoft.com/en-us/previous-versions/windows/hardware/design/dn640535(v=vs.85)#what-about-dynamic-disks
LDM_GUID = GUID(Data1=0xAF9B60A0, Data2=0x1431, Data3=0x4F62, Data4=[0xBC, 0x68, 0x33, 0x11, 0x71, 0x4A, 0x69, 0xAD])
PARTITION_MSFT_RESERVED_STARTING_OFFSET = 17408
PARTITION_MSFT_RESERVED_SIZE_MIN = 32 * 1024 * 1024
PARTITION_MSFT_RESERVED_SIZE_MAX = 128 * 1024 * 1024
PARTITION_MSFT_RESERVED_BAR = 16 * 1024 * 1024 * 1024
ERROR_INVALID_PARAMETER = 87
FIRST_PRIMARY_PARTITION_OFFSET = 1024 * 1024
GPT_PARTITION_OFFSET = 1024 * 1024

# Windows returns empty partition entries from the partition table.
# This lambda-function that returns True if the partition is not empty, i.e. in use
partitions_in_use_lambda = lambda partition: not is_zero(partition.PartitionLength)


def is_guid_partition(partition):
    return partition.union.PartitionType.Data1 == PARTITION_MSFT_RESERVED_GUID.Data1 and \
           partition.union.PartitionType.Data2 == PARTITION_MSFT_RESERVED_GUID.Data2 and \
           partition.union.PartitionType.Data3 == PARTITION_MSFT_RESERVED_GUID.Data3 and \
           partition.union.PartitionType.Data4 == PARTITION_MSFT_RESERVED_GUID.Data4


def to_large_integer(number):
    kwargs = {}
    if is_64bit():
        kwargs['QuadPart'] = number
    else:
        kwargs['HighPart'] = (number & 0xFFFFFFFF00000000) >> 32
        kwargs['LowPart'] = number & 0xFFFFFFFF
    instance = structures.LARGE_INTEGER(**kwargs)
    return instance

def from_large_integer(instance):
    return instance.QuadPart if is_64bit() else ((instance.HighPart << 32) + instance.LowPart)

def partition_type_specific(func):
    @wraps(func)
    def callee(*args, **kwargs):
        _name = func.__name__
        _self, args = args[0], args[1:]
        _type = _self._get_named_type()
        return getattr(_self, '_{}_{}'.format(_name, _type))(*args, **kwargs)
    return callee

class Volume(object):
    def __init__(self, disk, partition, mount_manager=None):
        super(Volume, self).__init__()
        self._disk = disk
        self._partition = partition
        self._mount_manager = mount_manager or MountManager()
        self._io = DeviceIoControl(self._path, False)

    @property
    @cached_method
    def _path(self):
        return self.get_volume_guid()

    @property
    def _device_number(self):
        return self._get_device_and_partition_number()[0]

    @property
    def _partition_number(self):
        return self._get_device_and_partition_number()[1]

    def __repr__(self):
        try:
            return "Volume <{}>".format(self._path)
        except:
            return "<Volume <?>"

    @classmethod
    def get_from_disk_and_partition(cls, disk, partition, mount_manager=None):
        return Volume(disk, partition, mount_manager=mount_manager)

    @cached_method
    def _get_device_and_partition_number(self):
        from infi.devicemanager.ioctl import DeviceIoControl
        return DeviceIoControl(self._path).storage_get_device_and_partition_number()

    @cached_method
    def _get_wmi_object(self):
        from ..wmi import WmiClient, iter_volumes
        from infi.devicemanager.ioctl import DeviceIoControl
        from infi.wioctl.errors import WindowsException
        client = WmiClient()
        expected = self._get_device_and_partition_number()
        def _filter(volume):
            try:
                actual = DeviceIoControl(volume.DeviceID.rstrip(r'\\')).storage_get_device_and_partition_number()
            except WindowsException as e:
                if e.winerror == 1:    # Floppy/CD/..
                    return False
            return actual == expected
        return filter(_filter, iter_volumes(client))[0]

    def format(self, quick=True, file_system="NTFS", cluster_size=0):
        # TODO the idea is to do only the formatting through wmi
        # next step is to figure out to quickly get from the setuapi and ioctl information to the wmi object
        self.online()
        wmi_object = self._get_wmi_object()
        wmi_object.Format(QuickFormat=quick, FileSystem=file_system, ClusterSize=cluster_size)

    def get_volume_guid(self):
        from infi.wioctl.errors import WindowsException

        _struct = self._partition._struct
        partition_info = from_large_integer(_struct.StartingOffset), from_large_integer(_struct.PartitionLength)

        for volume_guid in self._mount_manager.get_volume_guids():
            volume_guid = volume_guid.rstrip("\\")
            try:
                extents = self._mount_manager.get_volume_extents(volume_guid)
            except WindowsException as e:
                if e.winerror == 1: # Floppy/CD/..
                    continue
                raise
            for extent in extents:
                extent_info = from_large_integer(extent.StartingUsableOffset), from_large_integer(extent.ExtentLength)
                if extent.DiskNumber != self._disk._number:
                    continue
                # extent needs to be contained inside the partition
                if extent_info[0] >= partition_info[0] and sum(extent_info) <= sum(partition_info):
                    return volume_guid

    def get_mount_points(self):
        return self._mount_manager.get_volume_mount_points(self.get_volume_guid())

    def add_mount_point(self, mount_point):
        return self._mount_manager.add_volume_mount_point(self.get_volume_guid(), mount_point)

    def remove_mount_point(self, mount_point):
        return self._mount_manager.remove_volume_mount_point(mount_point)

    def has_drive_letter(self):
        return self._mount_manager.get_volume_drive_letter(self) is not None

    def get_available_drive_letters(self):
        return self._mount_manager.get_avaialable_drive_letters()

    def assign_first_available_drive_letter(self):
        return self.add_mount_point(self.get_available_drive_letters()[0])

    def online(self):
        return DeviceIoControl(self._path, True, False).ioctl_volume_online()

    def offline(self):
        return DeviceIoControl(self._path, True, False).ioctl_volume_offline()

    def resize(self, size_in_bytes):
        return DeviceIoControl(self._path, True, True).ioctl_extend_volume(size_in_bytes)


class Partition(object):
    def __init__(self, disk, struct):
        super(Partition, self).__init__()
        self._struct = struct
        self._disk = disk

    def __repr__(self):
        start, size = byte * self.get_start_offset_in_bytes(), byte * self.get_size_in_bytes()
        return "Partition <start={}, capacity={}> on {!r}".format(start, size, self._disk)

    def is_gpt(self):
        return self._get_layout().PartitionStyle == PARTITION_STYLE_GPT

    def is_mbr(self):
        return self._get_layout().PartitionStyle == PARTITION_STYLE_MBR

    def is_raw(self):
        return self._get_layout().PartitionStyle == PARTITION_STYLE_RAW

    def is_ldm(self):
        partition_type = self._struct.union.PartitionType
        return partition_type == LDM_GUID

    def is_empty(self):
        return is_zero(self._struct.PartitionLength)

    def get_size_in_bytes(self):
        return from_large_integer(self._struct.PartitionLength)

    def get_start_offset_in_bytes(self):
        return from_large_integer(self._struct.StartingOffset)

    @classmethod
    def _create(cls, disk, index, number, start_offset, length):
        partition = structures.PARTITION_INFORMATION_EX()
        layout = disk._get_layout()
        partition.StartingOffset = start_offset
        partition.PartitionStyle = layout.PartitionStyle
        partition.PartitionLength = length
        partition.PartitionNumber = number
        partition.RewritePartition = 1
        if partition.PartitionStyle == constants.PARTITION_STYLE_GPT:
            partition.union = structures.PARTITION_INFORMATION_GPT()
        else:
            partition.union = structures.PARTITION_INFORMATION_MBR()
        try:
            layout.PartitionEntry[index] = partition
        except IndexError:
            layout.PartitionEntry = [p for p in layout.PartitionEntry] + [partition, ]
        layout.PartitionCount = len(layout.PartitionEntry)
        return partition

    @classmethod
    def create_primary(cls, disk, index=0, boot=False, start_offset_in_bytes=FIRST_PRIMARY_PARTITION_OFFSET, size_in_bytes=None):
        """:param size: if size_in_bytes is None, the partition will be for the entire disk
        :param offset: either a number or Capacity
        :param size_in_bytes: """
        # I did not get this information from any official documentation, just by doing what the Disk Management does
        partition = cls._create(disk, index, index + 1,
                                to_large_integer(start_offset_in_bytes),
                                to_large_integer(disk.get_size_in_bytes() - 4 * 1024 * 1024 \
                                                 if size_in_bytes is None else size_in_bytes))
        partition.union.PartitionType = constants.PARTITION_HUGE
        partition.union.BootIndicator = constants.TRUE if boot else 0
        partition.union.RecognizedPartition = constants.TRUE
        partition.union.HiddenSectors = 0
        disk._update_layout()

    @classmethod
    def create_guid(cls, disk, index, partition_type_guid, start_offset_in_bytes, size_in_bytes):
        """:param size: if size_in_bytes is None, the partition will be for the entire disk
        :param offset: either a number or Capacity
        :param size_in_bytes: """
        # I did not get this information from any official documentation, just by doing what the Disk Management
        partition = cls._create(disk, index, index,
                                to_large_integer(start_offset_in_bytes),
                                to_large_integer(disk.get_size_in_bytes() - 65 * 1024 * 1024 \
                                                 if size_in_bytes is None else size_in_bytes))
        partition.union.PartitionType = partition_type_guid
        partition.union.PartitionId = generate_guid()
        partition.union.Attributes = 0
        partition.union.Name = [0, ]*36
        disk._update_layout()

    @cached_method
    def get_volume(self):
        return Volume.get_from_disk_and_partition(self._disk, self)

    def resize(self, size_in_bytes):
        import infi.wioctl
        self._disk._io.ioctl_disk_update_properties()
        self._disk._io.ioctl_disk_update_drive_size()

        _struct = structures.DISK_GROW_PARTITION()
        _struct.PartitionNumber = self._struct.PartitionNumber
        _struct.BytesToGrow = to_large_integer(size_in_bytes - self.get_size_in_bytes())
        try:
            self._disk._io.ioctl_disk_grow_partition(_struct)
        except infi.wioctl.api.WindowsException as e:
            if e.winerror != ERROR_INVALID_PARAMETER:
                raise
            _struct.BytesToGrow = to_large_integer(size_in_bytes - self.get_size_in_bytes() - 32000)
            self._disk._io.ioctl_disk_grow_partition(_struct)
        self._struct.PartitionLength = to_large_integer(size_in_bytes)  # we get_size_in_bytes will return the new size


class Disk(object):
    def __init__(self, disk_number):
        super(Disk, self).__init__()
        self._number = disk_number
        self._path = r"\\.\PHYSICALDRIVE{}".format(self._number)
        if not self._is_path_valid(self._path):
            raise RuntimeError("Invalid disk number: {0}".format(self._number))
        self._io = DeviceIoControl(self._path, True)

    def __repr__(self):
        return "Disk <{}>".format(self._path)

    @cached_method
    def _get_layout(self):
        """:returns: a DRIVE_LAYOUT_INFORMATION_EX Structure"""
        return self._io.ioctl_disk_get_drive_layout_ex()

    def _set_layout(self, layout):
        self._io.ioctl_disk_set_drive_layout_ex(layout)
        self.wait_for_all_volumes()
        self.clear_cached_properties()

    def _get_disk_drives(self):
        from infi.diskmanagement import wmi
        client = wmi.WmiClient()
        drives = wmi.get_disk_drives(client)
        return drives

    def _get_volumes_cluster_sizes(self):
        from infi.diskmanagement import wmi
        client = wmi.WmiClient()
        sizes = wmi.get_volumes_cluster_sizes(client)
        return sizes

    def _is_path_valid(self, path):
        return path in self._get_disk_drives()

    def wait_for_all_volumes(self):
        from time import sleep
        from waiting import wait
        def predicate():
            try:
                _ = [partition.get_volume().get_volume_guid() for partition in self.get_partitions()]
                return True
            except:
                logger.exception("Exception in wait_for_all_volumes")
                return False
        wait(predicate, timeout_seconds=30)

    def _update_layout(self):
        self._set_layout(self._get_layout())

    @cached_method
    def get_size_in_bytes(self):
        import infi.devicemanager.ioctl
        return infi.devicemanager.ioctl.DeviceIoControl(self._path).disk_get_drive_geometry_ex()

    def _get_named_type(self):
        if self.is_gpt():
            return 'gpt'
        elif self.is_mbr():
            return 'mbr'
        else:
            return 'raw'

    def is_gpt(self):
        return self._get_layout().PartitionStyle == PARTITION_STYLE_GPT

    def is_mbr(self):
        return self._get_layout().PartitionStyle == PARTITION_STYLE_MBR

    def is_raw(self):
        return self._get_layout().PartitionStyle == PARTITION_STYLE_RAW

    def is_dynamic(self):
        all_partitions = [Partition(self, struct) for struct in self._get_layout().PartitionEntry]
        return any(partition.is_ldm() for partition in all_partitions)

    def clear_cached_properties(self):
        clear_cache(self)

    def _has_extended_partition(self):
        return len(self._get_layout().PartitionEntry) >= 3 and \
               not is_zero(self._get_layout().PartitionEntry[3].PartitionLength)

    def _iter_partitions_mbr(self):
        for struct in self._get_layout().PartitionEntry[0:3]:
            # The first three MBR partitions are always primary (can be empty entries)
            partition = Partition(self, struct)
            if partition.is_empty():
                continue
            yield partition
        if not self._has_extended_partition():
            return
        for struct in self._get_layout().PartitionEntry[4::4]:
            partition = Partition(self, struct)
            if partition.is_empty():
                continue
            yield partition

    def _iter_partitions_raw(self):
        pass

    def _iter_partitions_gpt(self):
        # When creating a GPT drive in Windows, the first partition is a hidden partition
        # When creating a VSS snapshot, Windows moves the reseved partition and creates another one before it
        # This method needs to return the non-hidden partitions
        # The only logic I see that fits is to yield those after the reserved parititon:
        # the reserved partition has a known GUID, I can't find a known guid for the VSS partition
        key_lambda = lambda item: from_large_integer(item.StartingOffset)
        sorted_by_offset = sorted(self._get_layout().PartitionEntry, key=key_lambda)
        reserved_partition = [item for item in sorted_by_offset if is_guid_partition(item)]
        starting_index = 0
        if reserved_partition:
            starting_index = sorted_by_offset.index(reserved_partition[0])
        for struct in sorted_by_offset[starting_index+1:]:
            partition = Partition(self, struct)
            yield partition

    def get_partitions(self):
        return [partition for partition in self.iter_partitions()]

    def iter_partitions(self):
        for partition in getattr(self, "_iter_partitions_{}".format(self._get_named_type()))():
            yield partition

    def destroy_partition_table(self):
        self._io.ioctl_disk_delete_drive_layout()
        self.clear_cached_properties()

    def _create_partition_table_mbr(self, alignment_in_bytes=None):
        signature = generate_signature()
        self._io.ioctl_disk_create_disk(partition_style=PARTITION_STYLE_MBR)

    def _create_partition_table_gpt(self, alignment_in_bytes=None):
        guid = generate_guid()
        self._io.ioctl_disk_create_disk(partition_style=PARTITION_STYLE_GPT)
        minimum_required_size_in_bytes = PARTITION_MSFT_RESERVED_SIZE_MIN \
                                         if self.get_size_in_bytes() < PARTITION_MSFT_RESERVED_BAR \
                                         else PARTITION_MSFT_RESERVED_SIZE_MAX
        size_in_bytes = minimum_required_size_in_bytes
        if alignment_in_bytes:
            size_alignment = size_in_bytes % alignment_in_bytes
            offset_alignment = PARTITION_MSFT_RESERVED_STARTING_OFFSET % alignment_in_bytes
            if size_in_bytes % alignment_in_bytes:
                size_in_bytes += (alignment_in_bytes - size_in_bytes % alignment_in_bytes)
            if offset_alignment:
                size_in_bytes += (alignment_in_bytes - offset_alignment)
        Partition.create_guid(self, 1, PARTITION_MSFT_RESERVED_GUID,
                              PARTITION_MSFT_RESERVED_STARTING_OFFSET, size_in_bytes)

    def create_partition_table(self, type_name, alignment_in_bytes=None):
        """:param type_name: either 'gpt' or 'mbr'"""
        getattr(self, "_create_partition_table_{}".format(type_name))(alignment_in_bytes)
        self.clear_cached_properties()

    def create_first_partition(self, alignment_in_bytes=None):
        if self.is_mbr():
            offset_in_bytes = FIRST_PRIMARY_PARTITION_OFFSET
            if alignment_in_bytes:
                offset_alignment = FIRST_PRIMARY_PARTITION_OFFSET % alignment_in_bytes
                if offset_alignment:
                    offset_in_bytes += FIRST_PRIMARY_PARTITION_OFFSET - offset_alignment
            Partition.create_primary(self, start_offset_in_bytes=offset_in_bytes)
        elif self.is_gpt():
            reserved_partition = self._get_layout().PartitionEntry[0]
            offset_in_bytes = from_large_integer(reserved_partition.StartingOffset) + from_large_integer(reserved_partition.PartitionLength)
            offset_in_bytes += GPT_PARTITION_OFFSET
            if alignment_in_bytes:
                offset_alignment = GPT_PARTITION_OFFSET % alignment_in_bytes
                if offset_alignment:
                    offset_in_bytes += GPT_PARTITION_OFFSET - offset_alignment
            size_in_bytes = self.get_size_in_bytes() - offset_in_bytes - GPT_PARTITION_OFFSET
            Partition.create_guid(self, 2, PARTITION_BASIC_DATA_GUID, offset_in_bytes, size_in_bytes)

    def is_offline(self):
        return self._io.ioctl_disk_get_disk_attributes().Attributes & constants.DISK_ATTRIBUTE_OFFLINE

    def is_online(self):
        return not self.is_offline()

    def is_read_only(self):
        return self._io.ioctl_disk_get_disk_attributes().Attributes & constants.DISK_ATTRIBUTE_READ_ONLY

    def _set_disk_attrttributes(self, attributes, mask):
        set_struct = structures.SET_DISK_ATTRIBUTES(Version=0x28, Persist=constants.TRUE,
                                                    RelinquishOwnership=0, Attributes=attributes,
                                                    AttributesMask=mask,
                                                    Caller=GUID_ZERO)
        io = DeviceIoControl(self._path, True)
        io.ioctl_disk_set_disk_attributes(set_struct)

    def online(self):
        self._set_disk_attrttributes(0, constants.DISK_ATTRIBUTE_OFFLINE)

    def offline(self):
        self._set_disk_attrttributes(constants.DISK_ATTRIBUTE_OFFLINE, constants.DISK_ATTRIBUTE_OFFLINE)

    def read_only(self):
        self._set_disk_attrttributes(constants.DISK_ATTRIBUTE_READ_ONLY, constants.DISK_ATTRIBUTE_READ_ONLY)

    def read_write(self):
        self._set_disk_attrttributes(0, constants.DISK_ATTRIBUTE_READ_ONLY)

    def get_volume_number(self):
        self._io.ioctl_volume_query_volume_number()

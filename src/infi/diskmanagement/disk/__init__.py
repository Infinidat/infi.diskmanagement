
from infi.pyutils.lazy import cached_method, clear_cache
from infi.pyutils.decorators import wraps
from ..ioctl import DeviceIoControl, generate_signature, generate_guid
from ..ioctl.constants import PARTITION_STYLE_MBR, PARTITION_STYLE_GPT, PARTITION_STYLE_RAW

def is_zero(large_integer):
    """:returns: if the value of LARGE_INTEGER is zero"""
    if len(large_integer._fields_) == 1:
        return large_integer.QuadPart == 0
    return large_integer.LowPart == 0 and large_integer.HighPart == 0

# Windows returns empty partition entries from the partition table.
# This lambda-function that returns True if the partition is not empty, i.e. in use
partitions_in_use_lambda = lambda partition: not is_zero(partition.PartitionLength)

def partition_type_specific(func):
    @wraps(func)
    def callee(*args, **kwargs):
        _name = func.func_name
        _self, args = args[0], args[1:]
        _type = _self._get_named_type()
        return getattr(_self, '_{}_{}'.format(_name, _type))(*args, **kwargs)
    return callee

class Partition(object):
    def __init__(self, struct):
        super(Partition, self).__init__()
        self._struct = struct

    def is_gpt(self):
        return self._get_layout().PartitionStyle == PARTITION_STYLE_GPT

    def is_mbr(self):
        return self._get_layout().PartitionStyle == PARTITION_STYLE_MBR

    def is_raw(self):
        return self._get_layout().PartitionStyle == PARTITION_STYLE_RAW

    def is_empty(self):
        return is_zero(self._struct.PartitionLength)

class Disk(object):
    def __init__(self, disk_number):
        super(Disk, self).__init__()
        self._number = disk_number
        self._path = r"\\.\PHYSICALDRIVE{}".format(self._number)
        self._io = DeviceIoControl(self._path)

    @cached_method
    def _get_layout(self):
        """:returns: a DRIVE_LAYOUT_INFORMATION_EX Structure"""
        return self._io.ioctl_disk_get_drive_layout_ex()

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

    def clear_cached_properties(self):
        clear_cache(self)

    def _has_extended_partition(self):
        return len(self._get_layout().PartitionEntry) >= 3 and not is_zero(self._get_layout().PartitionEntry[3].PartitionLength)

    def _iter_partitions_mbr(self):
        for struct in self._get_layout().PartitionEntry[0:3]:
            # The first three MBR partitions are always primary (can be empty entries)
            partition = Partition(struct)
            if partition.is_empty():
                continue
            yield partition
        if not self._has_extended_partition():
            return
        for struct in self._get_layout().PartitionEntry[4::4]:
            partition = Partition(struct)
            if partition.is_empty():
                continue
            yield partition

    def _iter_partitions_raw(self):
        pass

    def _iter_partitions_gpt(self):
        for struct in self._get_layout().PartitionEntry[1:]:
            partition = Partition(struct)
            yield partition

    def get_partitions(self):
        return [partition for partition in self.iter_partitions()]

    def iter_partitions(self):
        for partition in getattr(self, "_iter_partitions_{}".format(self._get_named_type()))():
            yield partition

    def destroy_partition_table(self):
        self._io.ioctl_disk_delete_drive_layout()

    def _create_partition_table_mbr(self):
        signature = generate_signature()
        self._io.ioctl_disk_create_disk(partition_style=PARTITION_STYLE_MBR)

    def _create_partition_table_gpt(self):
        guid = generate_guid()
        self._io.ioctl_disk_create_disk(partition_style=PARTITION_STYLE_GPT)

    def create_partition_table(self, type_name):
        """:param type_name: either 'gpt' or 'mbr'"""
        getattr(self, "_create_partition_table_{}".format(type_name))()

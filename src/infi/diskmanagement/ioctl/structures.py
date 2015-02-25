
from infi.wioctl.structures import ULInt32, ULInt64, Struct, UCHAR, BOOLEAN, ULONG, Field, FixedSizeArray
from infi.wioctl.structures import ULONG64, GUID, WCHAR, LARGE_INTEGER, ULInt16, DWORD

from infi.instruct import  SelectStructByFunc, VarSizeArray, ReadPointer, Padding

# pylint: disable=C0103,W0212,W0201

PARTITION_STYLE = ULInt32
ULONGLONG = ULInt64

def _sizeof(struct):
    return struct.min_max_sizeof().max

def _max_size_struct(a, b):
    size_a, size_b = _sizeof(a), _sizeof(b)
    return size_a if size_a > size_b else size_b

def _extract_partition_style_from_header(header, stream, context):
    return context.get("struct", None).PartitionStyle

# PARTITION_INFORMATION

class PARTITION_INFORMATION_MBR(Struct):
    _fields_ = [UCHAR("PartitionType"),
                BOOLEAN("BootIndicator"),
                BOOLEAN("RecognizedPartition"), Padding(1),
                ULONG("HiddenSectors"), Padding(104)]

class PARTITION_INFORMATION_GPT(Struct):
    _fields_ = [Field("PartitionType", GUID), Field("PartitionId", GUID), ULONG64("Attributes"),
                FixedSizeArray("Name", 36, WCHAR), ]

class PARTITION_INFORMATION_EX__HEADER(Struct):
    _fields_ = [PARTITION_STYLE("PartitionStyle"), Padding(4),
                Field("StartingOffset", LARGE_INTEGER), Field("PartitionLength", LARGE_INTEGER),
                ULONG("PartitionNumber"), BOOLEAN("RewritePartition"), Padding(3), ]

class PARTITION_INFORMATION_EX(Struct):
    def _determine_union_type(self, stream, context=None):
        from .constants import PARTITION_STYLE_GPT
        style = _extract_partition_style_from_header(PARTITION_INFORMATION_EX__HEADER, stream, context)
        if style == PARTITION_STYLE_GPT:
            return PARTITION_INFORMATION_GPT
        return PARTITION_INFORMATION_MBR

    _fields_ = PARTITION_INFORMATION_EX__HEADER._fields_ + \
                [SelectStructByFunc("union", _determine_union_type, (0, 112)), ]

# DRIVE_LAYOUT

class DRIVE_LAYOUT_INFORMATION_MBR(Struct):
    _fields_ = [ULONG("Signature"), Padding(36), ]

class DRIVE_LAYOUT_INFORMATION_GPT(Struct):
    _fields_ = [Field("DiskId", GUID),
                Field("StartingUsableOffset", LARGE_INTEGER), Field("UsableLength", LARGE_INTEGER),
                ULONG("MaxPartitionCount"), Padding(4), ]

class DRIVE_LAYOUT_INFORMATION_EX__HEADER(Struct):
    _fields_ = [ULONG("PartitionStyle"), ULONG("PartitionCount"), ]

class DRIVE_LAYOUT_INFORMATION_EX(Struct):
    def _determine_union_type(self, stream, context=None):
        from .constants import PARTITION_STYLE_GPT
        style = _extract_partition_style_from_header(DRIVE_LAYOUT_INFORMATION_EX__HEADER, stream, context)
        if style == PARTITION_STYLE_GPT:
            return DRIVE_LAYOUT_INFORMATION_GPT
        return DRIVE_LAYOUT_INFORMATION_MBR

    _fields_ = DRIVE_LAYOUT_INFORMATION_EX__HEADER._fields_ + \
                [SelectStructByFunc("union", _determine_union_type, (0, 40)),
                 VarSizeArray("PartitionEntry", ReadPointer("PartitionCount"), PARTITION_INFORMATION_EX), ]

# CREATE_DISK

class CREATE_DISK_GPT(Struct):
    _fields_ = [Field("DiskId", GUID), ULONG("MaxPartitionCount"), ]

class CREATE_DISK_MBR(Struct):
    _fields_ = [ULONG("Signature"), Padding(16), ]

class CREATE_DISK__HEADER(Struct):
    _fields_ = [PARTITION_STYLE("PartitionStyle"), ]

class CREATE_DISK(Struct):
    def _determine_union_type(self, stream, context=None):
        from .constants import PARTITION_STYLE_GPT
        style = _extract_partition_style_from_header(CREATE_DISK__HEADER, stream, context)
        if style == PARTITION_STYLE_GPT:
            return CREATE_DISK_GPT
        return CREATE_DISK_MBR

    _fields_ = CREATE_DISK__HEADER._fields_ + \
                [SelectStructByFunc("union", _determine_union_type, (0, 20)), ]

class GET_DISK_ATTRIBUTES(Struct):
    _fields_ = [ULONG("Version"), ULONG("Reserved"), ULONGLONG("Attributes")]

class SET_DISK_ATTRIBUTES(Struct):
    _fields_ = [ULONG("Version"), BOOLEAN("Persist"), BOOLEAN("RelinquishOwnership"),
                Padding(2), ULONGLONG("Attributes"), ULONGLONG("AttributesMask"),
                Field("Caller", GUID)]

DISK_SAN_POLICY = ULInt32

class DISK_SAN_SETTINGS(Struct):
    _fields_ = [ULONG("Version"), DISK_SAN_POLICY("SanPolicy"), ]

class VOLUME_NUMBER(Struct):
    _fields_ = [ULONG("VolumeNumber"), FixedSizeArray("VolumeManagerName", 8, WCHAR), ]

class DISK_EXTENT(Struct):
    _fields_ = [DWORD("DiskNumber"), Padding(4),
                Field("StartingUsableOffset", LARGE_INTEGER), Field("ExtentLength", LARGE_INTEGER),]

class VOLUME_DISK_EXTENTS(Struct):
    _fields_ = [DWORD("NumberOfDiskExtents"), Padding(4),
                VarSizeArray("Extents", ReadPointer("NumberOfDiskExtents"), DISK_EXTENT),]

USHORT = ULInt16

class MOUNTMGR_MOUNT_POINT(Struct):
    _fields_ = [ULONG("SymbolicLinkNameOffset"), USHORT("SymbolicLinkNameLength"), Padding(2),
                ULONG("UniqueIdOffset"), USHORT("UniqueIdLength"), Padding(2),
                ULONG("DeviceNameOffset"), USHORT("DeviceNameLength"), Padding(2)]

class MOUNTMGR_MOUNT_POINTS(Struct):
    _fields_ = [ULONG("Size"), VarSizeArray("MountPoints", ULONG, MOUNTMGR_MOUNT_POINT)]

MOUNTMGR_AUTO_MOUNT_STATE = ULInt32

class MOUNTMGR_QUERY_AUTO_MOUNT(Struct):
    _fields_ = [MOUNTMGR_AUTO_MOUNT_STATE("CurrentState"), ]

class MOUNTMGR_SET_AUTO_MOUNT(Struct):
    _fields_ = [MOUNTMGR_AUTO_MOUNT_STATE("NewState"), ]

class DISK_GROW_PARTITION(Struct):
    _fields_ = [ULONG("PartitionNumber"), Padding(4), Field("BytesToGrow", LARGE_INTEGER)]

MEDIA_TYPE = ULONG

class DISK_GEOMETRY(Struct):
    _fields_ = [Field("Cylinders", LARGE_INTEGER), MEDIA_TYPE("MediaType"),
                ULInt32("TracksPerCylinder"), ULInt32("SectorsPerTrack"), ULInt32("BytesPerSector")]

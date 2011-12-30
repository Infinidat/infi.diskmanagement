
from infi.wioctl.structures import *
from infi.instruct import  StructFunc, SelectStructByFunc, VarSizeArray, ReadPointer, Padding, BitPadding

PARTITION_STYLE = ULInt32

def _sizeof(struct):
    return struct.min_max_sizeof().max

def _max_size_struct(a, b):
    size_a, size_b = _sizeof(a), _sizeof(b)
    return size_a if size_a > size_b else size_b

def _extract_partition_style_from_header(header, stream, context):
    return header.create_from_stream(stream, context).PartitionStyle

# PARTITION_INFORMATION

class PARTITION_INFORMATION_MBR(Struct):
    _fields_ = [UCHAR("PartitionType"), BitPadding(3),
                BOOLEAN("BootIndicator"), BitPadding(3),
                BOOLEAN("RecognizedPartition"), BitPadding(3),
                ULONG("HiddenSectors"), Padding(96)]

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

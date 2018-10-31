import unittest
import ctypes

# pylint: disable=W0614,R0904,W0401,W0622
from .structures import *
from .constants import PARTITION_STYLE_MBR, PARTITION_STYLE_GPT

def _sizeof(struct):
    return struct.min_max_sizeof().max

class CreateDiskTestCase(unittest.TestCase):
    def _get_mbr(self):
        struct = CREATE_DISK_MBR()
        struct.Signature = 1
        return struct

    def test_create_disk__mbr(self):
        struct = self._get_mbr()
        CREATE_DISK_MBR.write_to_string(struct)

    def _get_guid(self):
        struct = GUID.create_from_string(b'1' * 16)
        return struct

    def test_guid(self):
        struct = self._get_guid()
        GUID.write_to_string(struct)

    def _get_gpt(self):
        struct = CREATE_DISK_GPT()
        struct.DiskId = self._get_guid()
        struct.MaxPartitionCount = 1
        return struct

    def test_create_disk__gpt(self):
        struct = self._get_gpt()
        CREATE_DISK_GPT.write_to_string(struct)

    def test_create_disk(self):
        struct = CREATE_DISK()
        struct.PartitionStyle = 1
        struct.union = self._get_mbr()
        CREATE_DISK.write_to_string(struct)

class StructuresTestCase(unittest.TestCase):
    def test_partition_information__mbr(self):
        struct = PARTITION_INFORMATION_EX.create_from_string(b"\x00" * 137)

    def test_create_disk__mbr(self):
        """:param partition_style: int
        :param signature: int
        :param disk_id: 16-byte string
        :param max_partition_count: int"""
        struct = CREATE_DISK()
        struct.PartitionStyle = 1
        if struct.PartitionStyle == PARTITION_STYLE_MBR:
            klass = CREATE_DISK_MBR
            union = klass()
            union.Signature = 1
        else:
            klass = CREATE_DISK_GPT
            union = klass()
            union.DiskId = GUID.create_from_string(b"\x00"*16)
            union.MaxPartitionCount = 128
        struct.union = union
        size = struct.min_max_sizeof().max
        buffer = ctypes.c_buffer(CREATE_DISK.write_to_string(struct), size)

    def test_sizes(self):
        self.assertEqual(_sizeof(DRIVE_LAYOUT_INFORMATION_GPT), 40)
        self.assertEqual(_sizeof(DRIVE_LAYOUT_INFORMATION_MBR), 40)
        self.assertEqual(_sizeof(PARTITION_INFORMATION_GPT), 112)
        self.assertEqual(_sizeof(PARTITION_INFORMATION_MBR), 112)
        self.assertEqual(_sizeof(PARTITION_INFORMATION_EX), 144)
        self.assertEqual(_sizeof(DRIVE_LAYOUT_INFORMATION_EX), 48)


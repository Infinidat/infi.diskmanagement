import socket
from infi import unittest

from infi.diskmanagement import Disk, MountManager, PartitionManager

class SixthDriveTestCase(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self._disk = Disk(7)

    @classmethod
    def setUpClass(cls):
        super(SixthDriveTestCase, cls).setUpClass()
        if socket.gethostname() != 'host-ci38':
            raise unittest.SkipTest("This test case should run only on host-ci38")

    def test_uber(self):
        self._disk.destroy_partition_table()
        self._disk.create_partition_table('mbr')
        self._disk.create_first_partition()
        volume = self._disk.get_partitions()[0].get_volume()
        volume.format()
        self.assertFalse(volume.has_drive_letter())
        volume.assign_first_available_drive_letter()
        self.assertTrue(volume.has_drive_letter())


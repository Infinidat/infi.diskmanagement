
from infi import unittest
from infi.pyutils.contexts import contextmanager
import os
import mock
from infi.diskmanagement.disk import Disk

@contextmanager
def chdir_tests():
    curdir = os.path.abspath(os.path.curdir)
    os.chdir(os.path.join(curdir, "tests"))
    try:
        yield
    finally:
        os.chdir(curdir)

EXPECTED_NUMBERS_OF_PARTITIONS = [4, 4, 1, 12, 4, 4, 4]

class Base(unittest.TestCase):
    def setUp(self):
        self._chdir = chdir_tests()
        self._chdir.__enter__()
        self._set_patches()

    def _set_patches(self):
        from infi.diskmanagement.ioctl import DeviceIoControl
        self._ioctl_disk_get_drive_layout_ex = mock.patch.object(DeviceIoControl, "ioctl_disk_get_drive_layout_ex")

    def tearDown(self):
        self._chdir.__exit__(None, None, None)

class GetLayoutTestCase(Base):
    @unittest.parameters.iterate("disk_number", [index for index in range(6)])
    def test_get_layout(self, disk_number):
        from infi.diskmanagement.ioctl.structures import DRIVE_LAYOUT_INFORMATION_EX
        with self._ioctl_disk_get_drive_layout_ex as mock:
            with open("drive_layout_{}".format(disk_number), 'rb') as fd:
                mock.return_value = DRIVE_LAYOUT_INFORMATION_EX.create_from_string(fd.read())
                io = Disk(1)
                layout = io._get_layout()
                self.assertEqual(len(layout.PartitionEntry), EXPECTED_NUMBERS_OF_PARTITIONS[disk_number])

class GetPartitionsTestCase(Base):
    @unittest.parameters.iterate("disk_number", [index for index in range(6)])
    def test_get_partitions(self, disk_number):
        from infi.diskmanagement.ioctl.structures import DRIVE_LAYOUT_INFORMATION_EX
        with self._ioctl_disk_get_drive_layout_ex as mock:
            with open("drive_layout_{}".format(disk_number), 'rb') as fd:
                mock.return_value = DRIVE_LAYOUT_INFORMATION_EX.create_from_string(fd.read())
                io = Disk(1)
                partitions = io.get_partitions()
                for partition in partitions:
                    self.assertIn(partition._struct.PartitionStyle, [0, 1, ])

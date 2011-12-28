import unittest
import os
import socket

from infi.diskmanagement.ioctl import DeviceIoControl, constants, structures

class FirstDriveLayoutTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(FirstDriveLayoutTestCase, cls).setUpClass()
        if socket.gethostname() != 'host-ci38':
            raise unittest.SkipTest("This test case should run only on host-ci38")

    def setUp(self):
        unittest.TestCase.setUp(self)
        self._io = DeviceIoControl(r"\\.\PHYSICALDRIVE0")

    def test_get_layout(self):
        actual = self._io.ioctl_disk_get_drive_layout_ex()

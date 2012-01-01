import unittest
import os
import socket

from infi.diskmanagement.disk import Disk

class FirstDriveLayoutTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(FirstDriveLayoutTestCase, cls).setUpClass()
        if socket.gethostname() != 'host-ci38':
            raise unittest.SkipTest("This test case should run only on host-ci38")

    def setUp(self):
        unittest.TestCase.setUp(self)
        self._disk = Disk(0)

    def test_get_partitions(self):
        actual = self._disk.get_partitions()
        self.assertEqual(len(actual), 1)

    def test_type(self):
        self.assertTrue(self._disk.is_mbr())

class SecondDriveLayoutTestCase(FirstDriveLayoutTestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self._disk = Disk(1)

    def test_get_partitions(self):
        actual = self._disk.get_partitions()
        self.assertEqual(len(actual), 7)

    def test_type(self):
        self.assertTrue(self._disk.is_mbr())

class ThirdDriveLayoutTestCase(FirstDriveLayoutTestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self._disk = Disk(2)

    def test_get_partitions(self):
        actual = self._disk.get_partitions()
        self.assertEqual(len(actual), 1)

    def test_type(self):
        self.assertTrue(self._disk.is_gpt())

class EighthDriveLayoutTestCase(FirstDriveLayoutTestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self._disk = Disk(7)

    def test_set_layout(self):
        layout = self._disk._get_layout()
        self._disk._set_layout(layout)

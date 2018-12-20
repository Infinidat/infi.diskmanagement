
from infi import unittest
import os
from ... import wmi

class WmiTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(WmiTestCase, cls).setUpClass()
        if os.name != 'nt':
            raise unittest.SkipTest("This test case should run only on Windows")

    def test_get_drives(self):
        client = wmi.WmiClient()
        drives = wmi.get_disk_drives(client)
        self.assertGreater(len(drives), 0)

    def test_get_partitions(self):
        client = wmi.WmiClient()
        drives = wmi.get_disk_drives(client)
        self.assertGreater(len(drives), 0)
        partitions_by_drive = {drive.Name:wmi.get_paritions_of_disk_drive(client, drive) for drive in drives.values() }
        self.assertGreater(len(partitions_by_drive), 0)
        self.assertGreater(len(partitions_by_drive[u"\\\\.\\PHYSICALDRIVE0"]), 0)

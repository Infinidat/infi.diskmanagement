from infi import unittest
from ..mount_manager import MountManager
import ctypes

class MockVolume(object):
    def __init__(self):
        super(MockVolume, self).__init__()
        self._path = u'\\\\?\\GLOBALROOT\\Device\\HarddiskVolume35'

class InputBufferTestCase(unittest.TestCase):
    def test_create_input_buffer(self):
        size = ctypes.sizeof(ctypes.c_wchar)
        m = MountManager()
        buffer = m._create_input_buffer_for_query_points_ioctl(MockVolume())
        self.assertEqual(buffer.raw[0 - size - 1:], b'\x00' * (size + 1))

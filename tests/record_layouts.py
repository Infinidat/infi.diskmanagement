from __future__ import print_function
from infi.diskmanagement.ioctl import DeviceIoControl
import os

def record():
    for number in range(6):
        path = r"\\.\PHYSICALDRIVE{}".format(number)
        print(number, path)
        dev = DeviceIoControl(path)
        string = dev._partial_ioctl_diks_get_drive_layout_ex()
        filepath = os.path.join('tests', "drive_layout_{}".format(number))
        with open(filepath, 'wb') as fd:
            fd.write(string.raw)

if __name__ == "__main__":
    record()

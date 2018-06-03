
from .. import WmiObject
from infi.pyutils.lazy import cached_method

DISKDRIVES_QUERY = "SELECT * FROM Win32_DiskDrive"
VOLUME_QUERY = "SELECT * FROM Win32_Volume"
VOLUME_CLUSTER_SIZE_QUERY = "SELECT Name, Blocksize FROM Win32_Volume WHERE FileSystem='NTFS'"
DISKDRIVE_TO_DISKPARTITIONS_QUERY = r'SELECT * FROM Win32_DiskDriveToDiskPartition WHERE Antecedent="{}"'
DISKPARTITION_QUERY = r'SELECT * FROM Win32_DiskPartition WHERE DeviceID={}'

class DiskPartition(WmiObject):
    @property
    def Name(self):
        return self.get_wmi_attribute("Name")

    def __repr__(self):
        return "DiskPartition <{}>".format(self.Name)

class DiskDrive(WmiObject):
    @property
    def Name(self):
        return self.get_wmi_attribute("Name")

    @property
    def SerialNumber(self):
        return self.get_wmi_attribute("SerialNumber")

    def __repr__(self):
        return "DiskDrive <{}>".format(self.Name)

class Volume(WmiObject):
    @property
    def DeviceID(self):
        return self.get_wmi_attribute("DeviceID")

    @property
    def Name(self):
        return self.get_wmi_attribute("Name")

    @property
    def Blocksize(self):
        return self.get_wmi_attribute("Blocksize")

    def Format(self, ClusterSize=0, EnableCompression=False, FileSystem="NTFS", QuickFormat=True):
        method = self._object.Methods_("Format")
        parameters = method.InParameters.SpawnInstance_()
        parameters.Properties_.Item("ClusterSize").Value = ClusterSize
        parameters.Properties_.Item("EnableCompression").Value = EnableCompression
        parameters.Properties_.Item("FileSystem").Value = FileSystem
        parameters.Properties_.Item("QuickFormat").Value = QuickFormat
        _ = self._object.ExecMethod_(method.Name, parameters)


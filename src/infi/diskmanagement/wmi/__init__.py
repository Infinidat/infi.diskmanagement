__import__("pkg_resources").declare_namespace(__name__)

import re
from infi.wmi import WmiClient, WmiObject
from .model import DiskDrive, DiskPartition, DISKDRIVES_QUERY, DISKPARTITION_QUERY
from .model import DISKDRIVE_TO_DISKPARTITIONS_QUERY, VOLUME_CLUSTER_SIZE_QUERY, Volume

def escape_string(string):
    return re.sub("[\\\\'\"]", '\\\\\\g<0>', string)

def get_disk_drives(wmi_client):
    """:returns: a dictionary of (DiskDrive.Name, DiskDrive) items"""
    devices = dict()
    for result in wmi_client.execute_query(DISKDRIVES_QUERY):
        device = DiskDrive(result)
        devices[device.Name] = device
    return devices

def get_paritions_of_disk_drive(wmi_client, disk_drive):
    """:returns: a list of DiskPartition objects"""
    mapping_query = DISKDRIVE_TO_DISKPARTITIONS_QUERY.format(escape_string(disk_drive.get_path()))
    devices = []
    for mapping in wmi_client.execute_query(mapping_query):
        _, device_id = WmiObject(mapping).get_wmi_attribute("Dependent").split("=")
        partition_query = DISKPARTITION_QUERY.format(device_id)
        for result in wmi_client.execute_query(partition_query):
            devices.append(DiskPartition(result))
    return devices

def iter_volumes(wmi_client):
    from .model import Volume, VOLUME_QUERY
    for item in wmi_client.execute_query(VOLUME_QUERY):
        yield Volume(item)

def get_volumes_cluster_sizes(wmi_client):
    volumes = dict()
    for result in wmi_client.execute_query(VOLUME_CLUSTER_SIZE_QUERY):
        volume = Volume(result)
        volumes[volume.DeviceID] = int(volume.Blocksize)
    return volumes

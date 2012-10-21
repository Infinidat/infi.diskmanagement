Overview
========

A Python client for Windows Disk Management operations.

Usage
-----

In this example we destroy PHYSICALDRIVE1 and create a new volume inside it:

```python
from infi.diskmanagement import Disk
disk = Disk(1)
disk.online() if disk.is_offline() else None
disk.read_write() if disk.is_read_only() else None
disk.destroy_partition_table()
disk.create_partition_table('gpt')
volume = disk.get_partitions()[0].get_volume()
volume.format()
volume.assign_first_available_drive_letter() if not volume.has_drive_letter() else None
```

Checking out the code
=====================

This project uses buildout and infi-projector, and git to generate setup.py and __version__.py.
In order to generate these, first get infi-projector:

    easy_install infi.projector

    and then run in the project directory:

        projector devenv build

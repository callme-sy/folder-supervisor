import errno
import os
from stat import S_ISDIR
from watchdog.utils import platform
from watchdog.utils import stat as default_stat


[docs]class DirectorySnapshotDiff(object):
    """
    Compares two directory snapshots and creates an object that represents
    the difference between the two snapshots.

    :param ref:
        The reference directory snapshot.
    :type ref:
        :class:`DirectorySnapshot`
    :param snapshot:
        The directory snapshot which will be compared
        with the reference snapshot.
    :type snapshot:
        :class:`DirectorySnapshot`
    """
    
    def __init__(self, ref, snapshot):
        created = snapshot.paths - ref.paths
        deleted = ref.paths - snapshot.paths
        
        # check that all unchanged paths have the same inode
        for path in ref.paths & snapshot.paths:
            if ref.inode(path) != snapshot.inode(path):
                created.add(path)
                deleted.add(path)
        
        # find moved paths
        moved = set()
        for path in set(deleted):
            inode = ref.inode(path)
            new_path = snapshot.path(inode)
            if new_path:
                # file is not deleted but moved
                deleted.remove(path)
                moved.add((path, new_path))
        
        for path in set(created):
            inode = snapshot.inode(path)
            old_path = ref.path(inode)
            if old_path:
                created.remove(path)
                moved.add((old_path, path))
        

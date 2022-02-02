"""Manage symbolic links"""


def rmlink_safe(linkpath):
    """Remove the linkpath only if it is a symbolic link"""
    if linkpath.is_symlink():
        linkpath.unlink()
    if linkpath.exists():
        print(f"'{linkpath}' is not a symbolic link; it will not be replaced.")
        return False
    return True


def mklink(target, linkpath):
    """Create or replace a symbolic link to the path safely"""
    if rmlink_safe(linkpath):
        linkpath.symlink_to(target)

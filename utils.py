"""Manage symbolic links"""

from pathlib import Path

SCRIPTPATH = Path(__file__).resolve().parent.parent
HOME = Path.home()


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


def mklink_repo(username, repository, path, linkpath):
    """Create or replace a symbolic link to the path safely"""
    try:
        tmp = linkpath.relative_to(SCRIPTPATH)
        base = Path("../" * (len(tmp.parents) - 1))
    except ValueError:
        try:
            base = SCRIPTPATH.relative_to(linkpath.parent)
        except ValueError:
            base = SCRIPTPATH
    path = base.joinpath("repos", username, repository, path)
    mklink(path, linkpath)


def getlinkpath(module):
    """Get the linkpath for the module"""
    if module == "dircolors":
        return HOME.joinpath(".dircolors")
    if module == "tmux":
        return SCRIPTPATH.joinpath("tmux/.colors.tmux.conf")
    if module == "vim":
        return SCRIPTPATH.joinpath("vim/.colors.vim")
    return None

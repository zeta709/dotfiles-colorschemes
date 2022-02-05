"""define paths used by the color scheme selector"""

from pathlib import Path

SCRIPTPATH = Path(__file__).resolve().parent
LINKPATH = {
    "dircolors": Path.home().joinpath(".dircolors"),
    "tmux": SCRIPTPATH.joinpath("tmux/.colors.tmux.conf"),
    "vim": SCRIPTPATH.joinpath("vim/.colors.vim")
}


def gettargetpath(username, repository, path, linkpath):
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
    return path


def getlinkpath(app):
    """Get the linkpath for the app"""
    return LINKPATH[app]

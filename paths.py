"""Define paths used by the color scheme selector."""

from pathlib import Path

SCRIPTDIR = Path(__file__).resolve().parent
LINKPATH = {
    "dircolors": Path.home().joinpath(".dircolors"),
    "mutt": SCRIPTDIR.joinpath("mutt/.colors.muttrc"),
    "tmux": SCRIPTDIR.joinpath("tmux/.colors.tmux.conf"),
    "vim": SCRIPTDIR.joinpath("vim/.colors.vim")
}


def gettargetpath(username, repository, path, linkpath):
    """Returns the targetpath defined by username, repository, and path.

    Returns a relative path if either the linkpath is relative to the SCRIPTDIR
    or the SCRIPTDIR is relative to the linkpath's parent.
    Otherwise, returns an absolute path.
    """
    try:
        tmp = linkpath.relative_to(SCRIPTDIR)
        base = Path("../" * (len(tmp.parents) - 1))
    except ValueError:
        try:
            base = SCRIPTDIR.relative_to(linkpath.parent)
        except ValueError:
            base = SCRIPTDIR
    path = base.joinpath("repos", username, repository, path)
    return path


def getlinkpath(app):
    """Get the linkpath for the app."""
    return LINKPATH[app]

#!/usr/bin/env python3
# pylint: disable=W0511

"""Colorscheme"""

# TODO: split utility functions and theme functions into two files
# TODO: vim, mutt, etc.
# TODO: clone/fetch repositories

import curses
import sys
from pathlib import Path

SCRIPTPATH = Path(__file__).resolve().parent
HOME = Path.home()

curses.setupterm()
NUMCOLORS = curses.tigetnum("colors")


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


def default():
    """Default"""
    # dircolors
    rmlink_safe(getlinkpath("dircolors"))
    # tmux
    rmlink_safe(getlinkpath("tmux"))
    # vim
    mklink("/dev/null", getlinkpath("vim"))


def selenized(variant):
    """Selenized dark/light"""
    # dircolors
    rmlink_safe(getlinkpath("dircolors"))
    # tmux
    rmlink_safe(getlinkpath("tmux"))
    # vim
    filename = f"selenized-{variant}.vim"
    mklink(filename, getlinkpath("vim"))


def solarized(variant):
    """Solarized dark/light"""
    # dircolors
    linkpath = getlinkpath("dircolors")
    filename = ("dircolors.256dark" if NUMCOLORS >= 256
                else f"dircolors.ansi-{variant}")
    mklink_repo("seebi", "dircolors-solarized", filename, linkpath)
    # tmux
    linkpath = getlinkpath("tmux")
    filename = ("tmuxcolors-256.conf" if NUMCOLORS >= 256
                else f"tmuxcolors-{variant}.conf")
    mklink_repo("seebi", "tmux-colors-solarized", filename, linkpath)
    # vim
    linkpath = getlinkpath("vim")
    filename = (f"solarized-{variant}-256.vim" if NUMCOLORS >= 256
                else f"solarized-{variant}-16.vim")
    mklink(filename, linkpath)


THEMES = [
    ("Default", default),
    ("Selenized dark (24-bit)", lambda: selenized(variant="dark")),
    ("Selenized light (24-bit)", lambda: selenized(variant="light")),
    ("Solarized dark", lambda: solarized(variant="dark")),
    ("Solarized light", lambda: solarized(variant="light")),
]


def main():
    """main"""
    print("Choose your option:")
    for idx, theme in enumerate(THEMES):
        print(f"{idx}) {theme[0]}")

    try:
        ans = int(input("#? "))
    except EOFError:
        sys.exit(0)
    except ValueError:
        print("Invalid input")
        sys.exit(1)
    if ans < 0 or ans >= len(THEMES):
        print("Invalid input")
        sys.exit(1)
    if not callable(THEMES[ans][1]):
        print("Error")
        sys.exit(1)

    THEMES[ans][1]()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# pylint: disable=W0511

"""Colorscheme"""

# TODO: split utility functions and theme functions into two files
# TODO: vim, mutt, etc.
# TODO: clone/fetch repositories

import curses
import sys
from pathlib import Path

# TODO: use relpath if SCRIPTPATH is under HOME
SCRIPTPATH = Path(__file__).resolve().parent
HOME = Path.home()

curses.setupterm()
NUMCOLORS = curses.tigetnum("colors")


def rmlink_safe(linkpath):
    """Remove the linkpath only if it is a symbolic link"""
    if linkpath.is_symlink():
        linkpath.unlink()
    if linkpath.exists():
        print("'{}' is not a symbolic link; "
              "it will not be replaced.".format(str(linkpath)))
        return False
    return True


def mklink(fullpath, linkpath):
    """Create a symbolic link to the path safely"""
    if rmlink_safe(linkpath):
        linkpath.symlink_to(fullpath)


def mklink_repo(username, repository, path, linkpath):
    """Create a symbolic link to the path safely"""
    fullpath = SCRIPTPATH.joinpath("repos", username, repository, path)
    mklink(fullpath, linkpath)


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
    linkpath = getlinkpath("dircolors")
    rmlink_safe(linkpath)
    # tmux
    linkpath = getlinkpath("tmux")
    rmlink_safe(linkpath)
    # vim
    linkpath = getlinkpath("vim")
    mklink("/dev/null", linkpath)


def selenized_dark():
    """Selenized dark"""
    # dircolors
    linkpath = getlinkpath("dircolors")
    rmlink_safe(linkpath)
    # tmux
    linkpath = getlinkpath("tmux")
    rmlink_safe(linkpath)
    # vim
    linkpath = getlinkpath("vim")
    fullpath = SCRIPTPATH.joinpath("vim/selenized-dark.vim")
    mklink(fullpath, linkpath)


def selenized_light():
    """Selenized light"""
    # dircolors
    linkpath = getlinkpath("dircolors")
    rmlink_safe(linkpath)
    # tmux
    linkpath = getlinkpath("tmux")
    rmlink_safe(linkpath)
    # vim
    linkpath = getlinkpath("vim")
    fullpath = SCRIPTPATH.joinpath("vim/selenized-light.vim")
    mklink(fullpath, linkpath)


def solarized_dark():
    """Solarized dark"""
    # dircolors
    linkpath = getlinkpath("dircolors")
    filename = ("dircolors.256dark" if NUMCOLORS >= 256
                else "dircolors.ansi-dark")
    mklink_repo("seebi", "dircolors-solarized", filename, linkpath)
    # tmux
    linkpath = getlinkpath("tmux")
    filename = ("tmuxcolors-256.conf" if NUMCOLORS >= 256
                else "tmuxcolors-dark.conf")
    mklink_repo("seebi", "tmux-colors-solarized", filename, linkpath)
    # vim
    linkpath = getlinkpath("vim")
    filename = ("vim/solarized-dark-256.vim" if NUMCOLORS >= 256
                else "vim/solarized-dark-16.vim")
    mklink(SCRIPTPATH.joinpath(filename), linkpath)


def solarized_light():
    """Solarized light"""
    # dircolors
    linkpath = getlinkpath("dircolors")
    filename = ("dircolors.ansi-universal" if NUMCOLORS >= 256
                else "dircolors.ansi-light")
    mklink_repo("seebi", "dircolors-solarized", filename, linkpath)
    # tmux
    linkpath = getlinkpath("tmux")
    filename = ("tmuxcolors-256.conf" if NUMCOLORS >= 256
                else "tmuxcolors-light.conf")
    mklink_repo("seebi", "tmux-colors-solarized", filename, linkpath)
    # vim
    linkpath = getlinkpath("vim")
    filename = ("vim/solarized-light-256.vim" if NUMCOLORS >= 256
                else "vim/solarized-light-16.vim")
    mklink(SCRIPTPATH.joinpath(filename), linkpath)


THEMES = [
    ("Default", default),
    ("Selenized dark (24-bit)", selenized_dark),
    ("Selenized light (24-bit)", selenized_light),
    ("Solarized dark", solarized_dark),
    ("Solarized light", solarized_light),
]

print("Choose your option:")
for idx, theme in enumerate(THEMES):
    print("{idx}) {name}".format(idx=idx, name=theme[0]))

try:
    ANS = int(input("#? "))
except EOFError:
    sys.exit(0)
except ValueError:
    print("Invalid input")
    sys.exit(1)
if ANS < 0 or ANS >= len(THEMES):
    print("Invalid input")
    sys.exit(1)
elif not callable(THEMES[ANS][1]):
    print("Error")
    sys.exit(1)

THEMES[ANS][1]()

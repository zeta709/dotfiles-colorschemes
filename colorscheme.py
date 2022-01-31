#!/usr/bin/env python3
# pylint: disable=W0511

"""Colorscheme"""

# TODO: split utility functions and theme functions into two files
# TODO: vim, mutt, etc.
# TODO: clone/fetch repositories

import curses
import os
import sys
from pathlib import Path

# TODO: use relpath if SCRIPTPATH is under HOME
SCRIPTPATH = os.path.dirname(os.path.realpath(__file__))
HOME = str(Path.home())

curses.setupterm()
NUMCOLORS = curses.tigetnum("colors")


def rmlink_safe(linkname):
    """Remove the linkname only if it is a symbolic link"""
    if os.path.exists(linkname):
        if not os.path.islink(linkname):
            print("'{}' is not a symbolic link; "
                  "it will not be replaced.".format(linkname))
            return False
        os.remove(linkname)
    return True


def mklink(username, repository, path, linkname):
    """Create a symbolic link to the path safely"""
    fullpath = "/".join([SCRIPTPATH, "repos", username, repository, path])
    if rmlink_safe(linkname):
        os.symlink(fullpath, linkname)


def getlinkname(module):
    """Get the linkname for the module"""
    if module == "dircolors":
        return HOME + "/.dircolors"
    elif module == "tmux":
        return SCRIPTPATH + "/tmux/.colors.tmux.conf"
    return None


def default():
    """Default"""
    # dircolors
    linkname = getlinkname("dircolors")
    rmlink_safe(linkname)
    # tmux
    linkname = getlinkname("tmux")
    rmlink_safe(linkname)


def solarized_dark():
    """Solarized dark"""
    # dircolors
    linkname = getlinkname("dircolors")
    # filename = ("dircolors.256dark" if NUMCOLORS >= 256
    #             else "dircolors.ansi-dark")
    filename = "dircolors.ansi-dark"
    mklink("seebi", "dircolors-solarized", filename, linkname)
    # tmux
    linkname = getlinkname("tmux")
    # filename = ("tmuxcolors-256.conf" if NUMCOLORS >= 256
    #             else "tmuxcolors-dark.conf")
    filename = "tmuxcolors-dark.conf"
    mklink("seebi", "tmux-colors-solarized", filename, linkname)


def solarized_light():
    """Solarized light"""
    # dircolors
    linkname = getlinkname("dircolors")
    # filename = ("dircolors.ansi-universal" if NUMCOLORS >= 256
    #             else "dircolors.ansi-light")
    filename = "dircolors.ansi-light"
    mklink("seebi", "dircolors-solarized", filename, linkname)
    # tmux
    linkname = getlinkname("tmux")
    # filename = ("tmuxcolors-256.conf" if NUMCOLORS >= 256
    #             else "tmuxcolors-light.conf")
    filename = "tmuxcolors-light.conf"
    mklink("seebi", "tmux-colors-solarized", filename, linkname)


THEMES = [
    ("Default", default),
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

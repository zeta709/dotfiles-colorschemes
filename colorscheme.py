#!/usr/bin/env python3
# pylint: disable=W0511

"""Colorscheme"""

# TODO: split utility functions and theme functions into two files
# TODO: dircolors, tmux, vim, mutt, etc.
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


def default():
    """Default"""


def solarized_dark():
    """Solarized dark"""


def solarized_light():
    """Solarized light"""


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

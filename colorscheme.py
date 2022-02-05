#!/usr/bin/env python3

"""Color scheme selector"""

import curses
import sys
from functools import partial

from utils import rmlink_safe, mklink
from paths import gettargetpath, getlinkpath


def default():
    """Default"""
    for app in ["dircolors", "tmux"]:
        rmlink_safe(getlinkpath(app))
    for app in ["mutt", "vim"]:
        mklink("/dev/null", getlinkpath(app))


def selenized(variant):
    """Selenized"""
    default()
    # vim
    mklink(f"selenized-{variant}.vim", getlinkpath("vim"))


def solarized(variant):
    """Solarized"""
    curses.setupterm()
    numcolors = curses.tigetnum("colors")
    # dircolors
    linkpath = getlinkpath("dircolors")
    filename = ("dircolors.256dark" if numcolors >= 256
                else f"dircolors.ansi-{variant}")
    target = gettargetpath("seebi", "dircolors-solarized", filename, linkpath)
    mklink(target, linkpath)
    # mutt
    linkpath = getlinkpath("mutt")
    filename = (f"mutt-colors-solarized-{variant}-"
                + ("256.muttrc" if numcolors >= 256 else "16.muttrc"))
    target = gettargetpath("altercation", "mutt-colors-solarized", filename,
                           linkpath)
    mklink(target, linkpath)
    # tmux
    linkpath = getlinkpath("tmux")
    filename = ("tmuxcolors-256.conf" if numcolors >= 256
                else f"tmuxcolors-{variant}.conf")
    target = gettargetpath("seebi", "tmux-colors-solarized", filename,
                           linkpath)
    mklink(target, linkpath)
    # vim
    linkpath = getlinkpath("vim")
    filename = (f"solarized-{variant}-256.vim" if numcolors >= 256
                else f"solarized-{variant}-16.vim")
    mklink(filename, linkpath)


def main():
    """main"""
    themes = [("Default", default)]
    themes.extend([(f"Selenized {var} (24-bit)", partial(selenized, var))
                   for var in ["dark", "light", "black", "white"]])
    themes.extend([(f"Solarized {var}", partial(solarized, var))
                   for var in ["dark", "light"]])

    print("Choose your option:")
    for idx, theme in enumerate(themes):
        print(f"{idx}) {theme[0]}")

    try:
        ans = int(input("#? "))
    except EOFError:
        return 0
    except ValueError:
        print("Invalid input")
        return 1
    if ans < 0 or ans >= len(themes):
        print("Invalid input")
        return 1
    func = themes[ans][1]
    if not callable(func):
        print("Error")
        return 1
    func()
    return 0


if __name__ == '__main__':
    sys.exit(main())

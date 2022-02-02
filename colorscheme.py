#!/usr/bin/env python3

"""Color scheme selector"""

import curses
import sys
from functools import partial
from pathlib import Path

from utils import rmlink_safe, mklink

SCRIPTPATH = Path(__file__).resolve().parent


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


def getlinkpath(app):
    """Get the linkpath for the app"""
    if app == "dircolors":
        return Path.home().joinpath(".dircolors")
    if app == "tmux":
        return SCRIPTPATH.joinpath("tmux/.colors.tmux.conf")
    if app == "vim":
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
    """Selenized"""
    # dircolors
    rmlink_safe(getlinkpath("dircolors"))
    # tmux
    rmlink_safe(getlinkpath("tmux"))
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
    mklink_repo("seebi", "dircolors-solarized", filename, linkpath)
    # tmux
    linkpath = getlinkpath("tmux")
    filename = ("tmuxcolors-256.conf" if numcolors >= 256
                else f"tmuxcolors-{variant}.conf")
    mklink_repo("seebi", "tmux-colors-solarized", filename, linkpath)
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
        sys.exit(0)
    except ValueError:
        print("Invalid input")
        sys.exit(1)
    if ans < 0 or ans >= len(themes):
        print("Invalid input")
        sys.exit(1)
    func = themes[ans][1]
    if not callable(func):
        print("Error")
        sys.exit(1)
    func()


if __name__ == '__main__':
    main()

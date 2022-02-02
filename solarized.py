"""Solarized theme"""

import curses

from default import Default
from utils import mklink, mklink_repo, getlinkpath

curses.setupterm()
NUMCOLORS = curses.tigetnum("colors")


class Solarized(Default):
    """Solarized dark/light"""

    @staticmethod
    def get_variants():
        return ["dark", "light"]

    def __init__(self, variant):
        self.variant = variant

    def dircolors(self):
        linkpath = getlinkpath("dircolors")
        filename = ("dircolors.256dark" if NUMCOLORS >= 256
                    else f"dircolors.ansi-{self.variant}")
        mklink_repo("seebi", "dircolors-solarized", filename, linkpath)

    def tmux(self):
        linkpath = getlinkpath("tmux")
        filename = ("tmuxcolors-256.conf" if NUMCOLORS >= 256
                    else f"tmuxcolors-{self.variant}.conf")
        mklink_repo("seebi", "tmux-colors-solarized", filename, linkpath)

    def vim(self):
        linkpath = getlinkpath("vim")
        filename = (f"solarized-{self.variant}-256.vim" if NUMCOLORS >= 256
                    else f"solarized-{self.variant}-16.vim")
        mklink(filename, linkpath)

    def get_themes(self):
        # pylint: disable=unnecessary-lambda
        return [(f"Solarized {self.variant}", lambda: self.setup())]

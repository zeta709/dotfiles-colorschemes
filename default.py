# pylint: disable=no-self-use
"""Default theme"""

from utils import rmlink_safe, mklink, getlinkpath


class Default:
    """Default theme"""

    @staticmethod
    def get_variants():
        """Returns suppported variant(s)"""
        return [None]

    def dircolors(self):
        """For dircolors"""
        rmlink_safe(getlinkpath("dircolors"))

    def tmux(self):
        """For tmux"""
        rmlink_safe(getlinkpath("tmux"))

    def vim(self):
        """For vim"""
        mklink("/dev/null", getlinkpath("vim"))

    def setup(self):
        """Setup all"""
        self.dircolors()
        self.tmux()
        self.vim()

    def get_themes(self):
        """Returns a list of theme(s)"""
        # pylint: disable=unnecessary-lambda
        return [("Default", lambda: self.setup())]

    def install(self, themes):
        """Install themes into the given list"""
        themes.extend(self.get_themes())

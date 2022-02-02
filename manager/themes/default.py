# pylint: disable=no-self-use
"""Default theme"""

from pathlib import Path

from manager.utils.symlink import rmlink_safe, mklink


SCRIPTPATH = Path(__file__).resolve().parent.parent.parent
# NOTE: SCRIPTPATH is outside the package
# By creating a package under SCRIPTPATH, this python package gets
# a hidden dependency outside the package.
# - SCRIPTPATH/repos - repositories
# - SCRIPTPATH/vim - vim files
# - etc.
# It seems not logical (they shoould be bundled in the same package).

HOME = Path.home()

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

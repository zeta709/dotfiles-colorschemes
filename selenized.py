"""Selenized theme"""

from default import Default
from utils import mklink, getlinkpath


class Selenized(Default):
    """Selenized dark/light"""

    @staticmethod
    def get_variants():
        return ["dark", "light", "black", "white"]

    def __init__(self, variant):
        self.variant = variant

    def vim(self):
        filename = f"selenized-{self.variant}.vim"
        mklink(filename, getlinkpath("vim"))

    def get_themes(self):
        # pylint: disable=unnecessary-lambda
        return [(f"Selenized {self.variant} (24-bit)", lambda: self.setup())]

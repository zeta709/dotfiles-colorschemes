#!/usr/bin/env python3
"""Colorscheme"""

import sys
from typing import Callable, List, Tuple

from default import Default
from selenized import Selenized
from solarized import Solarized

THEMES: List[Tuple[str, Callable]] = []

Default().install(THEMES)
for variant in Selenized.get_variants():
    Selenized(variant).install(THEMES)
for variant in Solarized.get_variants():
    Solarized(variant).install(THEMES)


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

    func = THEMES[ans][1]
    if not callable(func):
        print("Error")
        sys.exit(1)
    func()


if __name__ == '__main__':
    main()

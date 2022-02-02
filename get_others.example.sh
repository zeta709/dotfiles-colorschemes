#!/bin/sh
# vim: noexpandtab:sw=4:ts=4

# NOTE: this way to get the scriptpath is not perfect
scriptpath=$(unset CDPATH && cd -- "$(dirname -- "$0")" && pwd -P)

add() (
	mkdir -p "$1" || return 1
	cd "$1" || return 1
	git submodule add --depth 1 "$2"
)

cd "${scriptpath}" || exit 1
mkdir -p repos || exit 1
cd repos || exit 1

if git rev-parse --absolute-git-dir > /dev/null 2>&1; then
	echo "It's already a git directory!"
	exit 1
fi

git init . || exit 1
git commit --allow-empty -m "Initial commit" || exit 1

add "seebi" "https://github.com/seebi/dircolors-solarized.git"
add "seebi" "https://github.com/seebi/tmux-colors-solarized.git"
add "altercation" "https://github.com/altercation/mutt-colors-solarized.git"
#add "mavnn" "https://github.com/mavnn/mintty-colors-solarized.git"

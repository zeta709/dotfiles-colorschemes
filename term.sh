#!/bin/sh
# vim: noexpandtab:sw=4:ts=4

# NOTE: this way to get the scriptpath is not perfect
scriptpath=$(unset CDPATH && cd -- "$(dirname -- "$0")" && pwd -P)

# replace the exsiting link only if it is a symbolic link
mklink_safe() {
	# target=$1; link_name=$2;
	if [ -e "$2" ] && [ ! -L "$2" ]; then
		printf "'%s' is not a symbolic link; it will not be replaced.\n" "$2"
		return 1
	fi
	ln -sf "$1" "$2"
}

term() (
	cat <<- EOF
	Choose your terminal type (q: quit):
	0) default 1) 16-color 2) 256-color 3) 24-bit-color
	EOF
	while printf '#? ' && read -r ans; do
		case $ans in
			0) file1="/dev/null"; file2="/dev/null"; break;;
			1) file1="16.sh"; file2="/dev/null"; break;;
			2) file1="256.sh"; file2="256.tmux.conf"; break;;
			3) file1="256.sh"; file2="24bit.tmux.conf"; break;;
			q) return 0;;
		esac
	done

	cd "${scriptpath}/sh" || return 1
	printf 'Do you want to set TERM (y/[n])?\n' && read -r ans
	case $ans in
		y|Y) mklink_safe "$file1" ".term.sh";;
		*) mklink_safe "/dev/null" ".term.sh";;
	esac

	cd "${scriptpath}/tmux" || return 1
	mklink_safe "$file2" ".term.tmux.conf"
)

term

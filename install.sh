#!/bin/sh
# vim: noexpandtab:sw=4:ts=4

# NOTE: this way to get the scriptdir is not perfect
# TODO: escape special characters in the scriptdir
scriptdir=$(unset CDPATH && cd -- "$(dirname -- "$0")" && pwd -P)

# do_source_cmd: insert the source command into the rc_file
# usage: do_source_cmd "$color_file" "$rc_file"
do_source_cmd() {
	color_file=$1
	rc_file=$2
	[ ! -e "$color_file" ] && ln -s "/dev/null" "${scriptdir}/${color_file}"
	if ! grep -Fq "$color_file" "$rc_file"; then
		printf 'source "%s"\n' "${scriptdir}/${color_file}" >> "$rc_file"
		printf "Installed: '%s' in '%s'\n" $color_file $rc_file
	else
		printf "Skip: '%s' for '%s'\n" $color_file $rc_file
	fi
}

install() (
	cd "$scriptdir" || return 1

	# shell
	[ -r "${HOME}/.bashrc" ] && do_source_cmd "sh/.term.sh" "${HOME}/.bashrc"
	[ -r "${HOME}/.zshrc" ] && do_source_cmd "sh/.term.sh" "${HOME}/.zshrc"

	# mutt
	mkdir -p "mutt"
	do_source_cmd "mutt/.colors.muttrc" "${HOME}/.muttrc"

	# tmux
	do_source_cmd "tmux/.term.tmux.conf" "${HOME}/.tmux.conf"
	do_source_cmd "tmux/.colors.tmux.conf" "${HOME}/.tmux.conf"

	# vim
	file="${scriptdir}/vim/.colors.vim"
	[ ! -e "$file" ] && ln -s "/dev/null" "$file"
	if ! grep -Fq ".colors.vim" "${HOME}/.vimrc"; then
		printf "exec 'source' fnameescape(\"%s\")\n" "$file" >> "${HOME}/.vimrc"
	fi
)

install

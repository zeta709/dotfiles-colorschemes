#!/bin/sh
# vim: noexpandtab:sw=4:ts=4

# NOTE: this way to get the scriptdir is not perfect
scriptdir=$(unset CDPATH && cd -- "$(dirname -- "$0")" && pwd -P)

install() (
	cd "$scriptdir" || return 1

	file="${scriptdir}/sh/.term.sh"
	[ ! -e "$file" ] && ln -s "/dev/null" "$file"
	if ! grep -Fq ".term.sh" "${HOME}/.zshrc"; then
		printf 'source "%s"\n' "$file" >> "${HOME}/.zshrc"
	fi

	file="${scriptdir}/tmux/.term.tmux.conf"
	[ ! -e "$file" ] && ln -s "/dev/null" "$file"
	if ! grep -Fq ".term.tmux.conf" "${HOME}/.tmux.conf"; then
		printf 'source "%s"\n' "$file" >> "${HOME}/.tmux.conf"
	fi

	file="${scriptdir}/tmux/.colors.tmux.conf"
	if ! grep -Fq ".colors.tmux.conf" "${HOME}/.tmux.conf"; then
		printf 'source -q "%s"\n' "$file" >> "${HOME}/.tmux.conf"
	fi

	file="${scriptdir}/vim/.colors.vim"
	[ ! -e "$file" ] && ln -s "/dev/null" "$file"
	if ! grep -Fq ".colors.vim" "${HOME}/.vimrc"; then
		printf "exec 'source' fnameescape('%s')\n" "$file" >> "${HOME}/.vimrc"
	fi
)

install

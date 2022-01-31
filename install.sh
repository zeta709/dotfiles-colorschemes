#!/bin/sh
# vim: noexpandtab:sw=4:ts=4

# NOTE: this way to get the scriptpath is not perfect
scriptpath=$(unset CDPATH && cd -- "$(dirname -- "$0")" >/dev/null 2>&1 && pwd -P)

install() (
	cd "$scriptpath" || return 1

	file="${scriptpath}/sh/.term.sh"
	[ ! -e "$file" ] && ln -s "/dev/null" "$file"
	if ! grep -Fq ".term.sh" "${HOME}/.zshrc"; then
		printf 'source "%s"\n' "$file" >> "${HOME}/.zshrc"
	fi

	file="${scriptpath}/tmux/.term.tmux.conf"
	[ ! -e "$file" ] && ln -s "/dev/null" "$file"
	if ! grep -Fq ".term.tmux.conf" "${HOME}/.tmux.conf"; then
		printf 'source "%s"\n' "$file" >> "${HOME}/.tmux.conf"
	fi

	file="${scriptpath}/tmux/.colors.tmux.conf"
	if ! grep -Fq ".colors.tmux.conf" "${HOME}/.tmux.conf"; then
		printf 'source -q "%s"\n' "$file" >> "${HOME}/.tmux.conf"
	fi
)

install

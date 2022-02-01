# dotfiles-colorschemes

[![Pylint](https://github.com/zeta709/dotfiles-colorschemes/actions/workflows/pylint.yml/badge.svg)](https://github.com/zeta709/dotfiles-colorschemes/actions/workflows/pylint.yml)

## Installation

``` sh
$ ./install.sh
```

However, some installation procedure have not been automated yet.

### Other repositories

Clone repositories you need:
``` sh
cd ".colorscheme/repos"
mkdir "seebi" && cd "$_"
git clone https://github.com/seebi/dircolors-solarized.git
git clone https://github.com/seebi/tmux-colors-solarized.git

cd ".colorscheme/repos"
mkdir "altercation" && cd "$_"
git clone https://github.com/altercation/mutt-colors-solarized.git
```

### LS_COLORS for Selenized

Selenized `LS_COLORS`:
``` sh
export LS_COLORS="$LS_COLORS:ow=1;7;34:st=30;44:su=30;41"
```

Refer [Selenized settings for dircolors](https://github.com/jan-warchol/selenized/tree/master/other-apps/dircolors).

### Vim

Add Vim plugins:
``` vim
call plug#begin('user/.vim/plugged')
" Solarized and its variants
Plug 'altercation/vim-colors-solarized'
Plug 'lifepillar/vim-solarized8'
Plug 'romainl/flattened'
" Selenized
Plug 'jan-warchol/selenized', { 'rtp': 'editors/vim' }
call plug#end()
```

## Applying color scheme

``` sh
$ ./term.sh
$ ./colorscheme.py
```

You have to set your terminal settings properly. Refer
[altercation/solarized](https://github.com/altercation/solarized) or
[jan-warchol/selenized](https://github.com/jan-warchol/selenized).

# dotfiles-colorschemes

[![Pylint](https://github.com/zeta709/dotfiles-colorschemes/actions/workflows/pylint.yml/badge.svg)](https://github.com/zeta709/dotfiles-colorschemes/actions/workflows/pylint.yml)

## Installation

``` sh
$ ./install.sh
```

However, some installation procedure have not been automated yet.

### Other repositories

You need to clone color scheme repositories.  Review `get_others.example.sh`
and modify it as you need.
Basically, it initializes a new git directory inside this directory, and add
color scheme repositories as submodules.
Thus, this repository itself will not be affected when you add or remove color
scheme repositories. At the same time, it is easy to mange theme repositories.

``` sh
$ ./get_others.example.sh # review the file before execute it
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

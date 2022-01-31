syntax enable
set background=dark
let g:solarized_termcolors=256
colorscheme solarized
let s:path=fnamemodify(resolve(expand("<sfile>:p")), ":h")
exec "source " . s:path . "/solarized-fix.vim"

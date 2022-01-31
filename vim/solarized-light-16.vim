syntax enable
set background=light
let g:solarized_termtrans=1
colorscheme solarized
let s:path=fnamemodify(resolve(expand("<sfile>:p")), ":h")
exec "source " . s:path . "/solarized-fix.vim"
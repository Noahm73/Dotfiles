set incsearch
set noswapfile
set nobackup
syntax enable

call plug#begin('~/.vim/plugged')

Plug 'arcticicestudio/nord-vim'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

call plug#end()

colorscheme nord

let g:airline_powerline_fonts = 1

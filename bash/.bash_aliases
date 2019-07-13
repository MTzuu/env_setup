#
# ~/.bash_aliases
#


# sudo alias, so u can still use aliases when running command with sudo

alias sudo='sudo '

# disk usage
alias du1='du -hca -d 1'

# use color in these commands
alias grep='grep --color=auto'
alias ls='ls --color=auto'

# ls aliases
alias ll='ls -ahl'

# pacman aliases
alias pacro='pacman -Rns $(pacman -Qtdq)'

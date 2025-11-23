# Completion configuration

autoload -Uz compinit promptinit
zmodload zsh/complist

zstyle ':completion:*' completer _complete _ignored
zstyle ':completion:*' file-sort access
zstyle ':completion:*' menu select=0
zstyle ':completion:*' select-prompt '%SScrolling active: current selection at %p%s'
zstyle :compinstall filename '/home/matze/.config/zsh/.zshrc'

compinit
promptinit

# History configuration

HISTFILE=~/.config/zsh/.histfile
HISTSIZE=1000
SAVEHIST=100000
unsetopt autocd beep extendedglob nomatch notify
bindkey -v
export KEYTIMEOUT=5

# version control system (vcs) info configuration

autoload -Uz vcs_info
zstyle ':vcs_info:git:*' formats       "%b"
zstyle ':vcs_info:git:*' actionformats "%b"

zstyle ':vcs_info:git:*' stagedstr   '%F{yellow}'
zstyle ':vcs_info:git:*' unstagedstr '%F{red}'
zstyle ':vcs_info:git:*' cleanstr    '%F{green}'

zstyle ':vcs_info:git:*' formats       '%F{cyan}%b%f'
zstyle ':vcs_info:git:*' actionformats '%F{cyan}%b%f'

update_vc() {
  vcs_info

  color="%F{cyan}"

  if [[ -n ${vcs_info_msg_0_} ]]; then
    git_status=$(git -C "$(pwd)" status --porcelain 2>/dev/null)

    if [[ -n $(echo "$git_status" | grep '^[MARCD]') ]]; then
      zstyle ':vcs_info:git:*' formats       '%F{yellow}%b%f'
      zstyle ':vcs_info:git:*' actionformats '%F{yellow}%b%f'
    elif [[ -n $(echo "$git_status" | grep '^[ ]M') ]]; then
      zstyle ':vcs_info:git:*' formats       '%F{red}%b%f'
      zstyle ':vcs_info:git:*' actionformats '%F{red}%b%f'
    else
      zstyle ':vcs_info:git:*' formats       '%F{cyan}%b%f'
      zstyle ':vcs_info:git:*' actionformats '%F{cyan}%b%f'
    fi
  fi

  update_rprompt
}

# make rprompt (right side of the prompt) show, if you enter
# vi "normal" mode (vicmd) also this is where vcs_info_msg is added

update_rprompt() {
  if [[ "${KEYMAP}" == vicmd ]]; then
    VI_MODE='VI MODE'
  else
    VI_MODE=''
  fi
  RPROMPT='%B'$VI_MODE' %b%F{cyan}'${vcs_info_msg_0_}
}

precmd_functions+=(update_vc)

# prompt configuration, using zsh inbuilt custum theme support

prompt_mytheme_setup() {
  PS1='%B%F{white}%T %F{green}%n@%m%b %F{yellow}%3~ %f%(?.%F{white}.%F{red})$ %f'
}

zle-keymap-select() {
  update_vc
  zle reset-prompt
}

zle-line-init() {
  update_vc
  zle reset-prompt
}

zle -N zle-keymap-select
zle -N zle-line-init

prompt_themes+=(mytheme)
prompt mytheme

# load additional zsh configuration files

for conf in $ZDOTDIR/zsh_*; do
  source $conf;
done
unset conf

#!/bin/bash
# ~/.bashrc
#

# If not running interactively, don't do anything

        HISTORY_RED="\033[1;31m"
     HISTORY_YELLOW="\033[1;33m"
      HISTORY_GREEN="\033[1;32m"
       HISTORY_BLUE="\033[1;34m"
  HISTORY_LIGHT_RED="\033[1;31m"
HISTORY_LIGHT_GREEN="\033[1;32m"
      HISTORY_WHITE="\033[1;37m"
 HISTORY_LIGHT_GRAY="\033[1;37m"
 HISTORY_COLOR_NONE="\e[0m"

[[ $- != *i* ]] && return

PS1='eu@\h \W]\$ '

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

if [ -f ~/.bash_prompt ]; then
    . ~/.bash_prompt
fi

export HISTTIMEFORMAT=`echo -e "${HISTORY_YELLOW}%h %d ${HISTORY_WHITE}%H:%M:%S ${HISTORY_COLOR_NONE}"`
export HISTSIZE=10000
export HISTFILESIZE=10000

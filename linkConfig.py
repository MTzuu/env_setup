#!/usr/bin/env python

import getpass

user = getpass.getuser()

class Config(object):
    Linux = {
        "bash/.bashrc"              : "/home/" + user + "/.bashrc",
        "bash/.bash_aliases"        : "/home/" + user + "/.bash_aliases",
        "bash/.bash_prompt"         : "/home/" + user + "/.bash_prompt",
        "git/.gitconfig"            : "/home/" + user + "/.gitconfig",
        "vim/.vimrc"                : "/home/" + user + "/.vimrc",
        "sway/config"               : "/home/" + user + "/.config/sway/config",
        "sway/scripts/sway_bar.sh"  : "/home/" + user + "/.config/sway/scripts/sway_bar.sh"
    }
    LinuxDirs = [
        "/home/" + user + "/.config/sway/scripts/"
    ]

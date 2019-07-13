#!/usr/bin/env python

import getpass

user = getpass.getuser()

class Config(object):
    Linux = {
        "bash/.bashrc"          : "/home/" + user + "/.bashrc",
        "bash/.bash_aliases"    : "/home/" + user + "/.bash_aliases",
        "bash/.bash_prompt"     : "/home/" + user + "/.bash_prompt",

        "git/.gitconfig"        : "/home/" + user + "/.gitconfig",

        "vim/.vimrc"            : "/home/" + user + "/.vimrc",
    }

import getpass
user = getpass.getuser()

class Config(object):
    Linux = {
        '.config/git',
        '.config/i3blocks',
        '.config/nvim',
        '.config/sway',
        '.config/vim',
        '.config/zsh',
        '.zshenv'
    }
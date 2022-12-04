#!/usr/bin/env python

import os               # used to perform filesystem actions
import textwrap
from pathlib import Path

from linkConfig import Config

def query_yes_no(question, default="yes") -> "bool":
    valid = {"yes" : True, "y": True, "no" : False, "n" : False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        choice = input(question + prompt)
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")

def main():
    config = Config.Linux
    dirs = Config.LinuxDirs

    currentDir = os.path.dirname(os.path.abspath(__file__))
    adaptedConfig = {}

    for key in config:
        newkey = os.path.join(currentDir, key)
        adaptedConfig[newkey] = config[key]

    print("{:-^80}".format("Replace Configs with SymLinks"))
    print("{:80}".format("The following links will be created: "))

    for key, value in config.items():
        print("    {}    ->    {}".format(value, key))

    if query_yes_no("Do you want to continue?"):
        # create directories needed for config files
        # living in ~/.config
        for dir in dirs:
            try:
                Path(dir).mkdir(parents=True, exist_ok=True)
            except:
                print("Error during directory creation! Exception raised:")
                print(textwrap.fill(str(e), 80))

        # create symlinks for all configs
        for key, value in adaptedConfig.items():
            print("\nExecuting    {}    ->    {}".format(value, key))
            try:
                if os.path.lexists(value):
                    os.remove(value)
                os.symlink(key, value)
            except Exception as e:
                print("Error during symlink creation! Exception raised:")
                print(textwrap.fill(str(e), 80))
            else:
                print("    Done!")
    else:
        print("{:80}".format("No changes to your system were made"))
        exit(1)

if __name__ == '__main__':
    main()

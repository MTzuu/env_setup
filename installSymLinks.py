#!/usr/bin/env python

import os
import shutil

from linkConfig import get_links
from helpers import confirm


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_home = os.path.join(current_dir, 'home')

    caller_home = os.path.expanduser('~')
    links = get_links(src_home, user_home=caller_home)
    if not links:
        print("No items found in './home' to link. Nothing to do.")
        return

    print("{:-^80}".format("Create symlinks from ./home to your $HOME"))
    print("Planned links:")
    for src, target in links:
        rel = os.path.relpath(target, caller_home)
        print(f"    ~/{rel}    ->    {src}")

    if not confirm("Do you want to continue and create/overwrite these links?", default=True):
        print("No changes to your system were made")
        return

    for src, target in links:
        target = os.path.abspath(target)
        parent = os.path.dirname(target) or caller_home

        try:
            os.makedirs(parent, exist_ok=True)
        except Exception as e:
            print(f"Error creating parent directory {parent}: {e}")
            continue

        print(f"\nExecuting: {target} -> {src}")
        try:
            if os.path.lexists(target):
                # remove existing symlink or file; remove directories recursively
                if os.path.islink(target) or os.path.isfile(target):
                    os.remove(target)
                elif os.path.isdir(target):
                    shutil.rmtree(target)

            os.symlink(src, target)
        except Exception as e:
            print("Error during symlink creation:", e)
        else:
            print("    Done!")


if __name__ == '__main__':
    main()

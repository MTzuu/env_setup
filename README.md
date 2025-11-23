# env_setup

The purpose of this project is to synchronize configuration files across Linux machines.

`installSymLinks.py` creates symlinks from the `./home` directory in this
repository into the current user's home directory. The `linkConfig.py`
module scans the `./home` tree and automatically builds the list of
items to link — you don't need to edit it when adding files or folders
to `./home`.

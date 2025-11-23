"""Utility to produce symlink mappings from the repository `./home` tree.

This module intentionally keeps behavior simple and predictable:
- Top-level files in `./home` map to `~/<name>`.
- Top-level directories in `./home` map their immediate children to
  `~/<topdir>/<child>` (non-recursive).

The installer is responsible for creating parent directories and
performing the actual filesystem operations.
"""

import os
from typing import List, Tuple


def _repo_home(base: str | None) -> str:
    """Return absolute path to the `./home` directory next to this file.

    If `base` is provided it is returned as an absolute path (useful for
    testing). Otherwise the default is `./home` next to this module.
    """
    if base:
        return os.path.abspath(base)
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(here, 'home'))


def _unique_preserve_order(items: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    seen = set()
    out = []
    for src, rel in items:
        key = (src, rel)
        if key in seen:
            continue
        seen.add(key)
        out.append((src, rel))
    return out


def get_links(home_dir: str | None = None, user_home: str | None = None) -> List[Tuple[str, str]]:
    """Return list of (source_abs_path, target_abs_path) for items under `./home`.

    - `home_dir`: optional path to the `home` directory in the repo to scan.
    - `user_home`: optional absolute path to the caller's home directory; if
        omitted the function uses the current user's `~` (via `os.path.expanduser`).

    The returned `target_abs_path` values are absolute paths under `user_home`.
    """
    home_dir = _repo_home(home_dir)
    if not os.path.exists(home_dir):
        return []

    if user_home is None:
        user_home = os.path.expanduser('~')
    user_home = os.path.abspath(user_home)

    mappings: List[Tuple[str, str]] = []  # store (src_abs, rel_target)

    for entry in sorted(os.listdir(home_dir)):
        entry_path = os.path.join(home_dir, entry)

        # Top-level files or symlinks -> map to ~/entry
        if os.path.isfile(entry_path) or os.path.islink(entry_path):
            mappings.append((os.path.abspath(entry_path), entry))
            continue

        # Top-level directory -> map immediate children (non-recursive)
        if os.path.isdir(entry_path):
            for child in sorted(os.listdir(entry_path)):
                child_path = os.path.join(entry_path, child)
                rel = os.path.join(entry, child)
                mappings.append((os.path.abspath(child_path), rel))

    # Deduplicate while preserving order
    mappings = _unique_preserve_order(mappings)

    # If a directory mapping exists (e.g. '.config/sway'), then any other
    # mappings nested under that relative path are redundant; remove them.
    dir_rels = {rel for (src, rel) in mappings if os.path.isdir(src)}

    def _is_nested_under_any(rel_path: str) -> bool:
        for d in dir_rels:
            if rel_path == d:
                return False
            if rel_path.startswith(d.rstrip(os.sep) + os.sep):
                return True
        return False

    filtered_rel = [(s, r) for (s, r) in mappings if not _is_nested_under_any(r)]

    # Convert relative targets to absolute targets under user_home
    result: List[Tuple[str, str]] = []
    for src, rel in filtered_rel:
        target_abs = os.path.abspath(os.path.join(user_home, rel))
        result.append((src, target_abs))

    return result


if __name__ == '__main__':
    for src, target in get_links():
        print(f"{target} -> {src}")
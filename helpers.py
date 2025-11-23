"""Small helper utilities for the installer.

Currently contains a minimal interactive confirmation helper used by the
installer to ask a single yes/no question.
"""
def confirm(question, default=True):
    """Ask a yes/no question via input() and return True/False.

    `default` controls the default behavior when the user just presses Enter.
    """
    if default:
        prompt = " [Y/n] "
    else:
        prompt = " [y/N] "

    while True:
        try:
            choice = input(question + prompt).strip().lower()
        except (KeyboardInterrupt, EOFError):
            return False

        if choice == '' and default is not None:
            return bool(default)
        if choice in ('y', 'yes'):
            return True
        if choice in ('n', 'no'):
            return False
        print("Please answer 'y' or 'n'.")

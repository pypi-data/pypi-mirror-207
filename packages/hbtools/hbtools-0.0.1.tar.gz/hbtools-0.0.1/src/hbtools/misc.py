"""Module providing miscellaneous functions related to printing."""
from shutil import get_terminal_size


def yes_no_prompt(question: str, *, default: bool = True) -> bool:
    """Prompts the user for a binary answer.

    Args:
        question: The text that will be shown to the user.
        default: Default value to use if the user just presses enter.

    Returns:
        True for yes, False for no
    """
    choices = " [Y/n]: " if default else " [y/N]: "

    answer = input(question + choices).lower().strip()

    if len(answer) == 0:
        return default

    if answer not in ["y", "n"]:
        print("Input invalid, please enter 'y' or 'n'")
        return yes_no_prompt(question)
    return answer == "y"


def clean_print(msg: str, fallback: tuple[int, int] = (156, 38), end: str = "\n") -> None:
    r"""Print the given string to the console and erase any character previously written on the line.

    Args:
        msg: String to print to the console.
        fallback: Size of the terminal to use if it cannot be determined by shutil (if using windows for example).
        end: What to add at the end of the print. Usually '\n' (new line), or '\r' (back to the start of the line).
    """
    print(msg + " " * (get_terminal_size(fallback=fallback).columns - len(msg)), end=end, flush=True)

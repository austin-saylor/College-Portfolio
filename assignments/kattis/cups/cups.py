"""
Main module that runs the program.
"""

import sys
from cup_data import Sort


def main() -> None:
    """
    Take the input and sort
    the given cups.

    :return: None
    """
    input_cups = sys.stdin.readline
    cup_sort = Sort(input_cups)
    cup_sort.read_input()
    cup_sort.solve()
    cup_sort.print_answer()


if __name__ == "__main__":
    """
    Upon execution of the program,
    run the main function.
    """
    main()

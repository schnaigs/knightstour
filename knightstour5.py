import random
import sys

def main():
    """Conduct a knight's tour using a brute force method, representing the
       board as a tuple of (dict, rows, cols).
    """
    if len(sys.argv) != 4:
        sys.exit("usage: python knightstour5.py rows columns attempts")

    rows = checkarg(sys.argv[1])


def checkarg(arg):
    """Returns the input value if it's valid, exits the program otherwise."""

    try:
        if int(arg) >= 1:
            return int(arg)
        else:
            sys.exit("argument must be 1 or higher")
    except ValueError:
        sys.exit("argument must be an integer")


if __name__ == "__main__":
    main()


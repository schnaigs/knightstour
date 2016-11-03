import random
import sys

def main():
    """Conduct a knight's tour using a brute force method, representing the
       board as a tuple of (dict, rows, cols).
    """
    if len(sys.argv) != 4:
        sys.exit("usage: python knightstour5.py rows columns attempts")

    rows = checkarg(sys.argv[1])
    cols = checkarg(sys.argv[2])
    attempts = checkarg(sys.argv[3])

    for attempt in range(attempts):
        board = create_board(rows, cols)
        initial_pos = (0, 0)

        board = conduct_knights_tour(board, initial_pos)

        # at this point, all possible moves have been performed, and the knight's
        # tour is either complete or incomplete
        if None in board['board'].values():
            print "attempt #" + str(attempt + 1)
            print "Knight's tour complete!"
            print_board(board)
            sys.exit()

    # if this point is reached (i.e. sys.exit() is not called because a
    # complete knight's tour was not found) then the knight's tour failed
    print "knight's tour failed!"
    print_board(board)


def print_board(board):
    """Pretty-print a representation of the board."""

    for i in range(board['rows']):
        for j in range(board['cols']):
            if board['board'][(i, j)] is None:
                print '{:3}'.format('x'),
            else:
                print '{:3}'.format(str(board['board'][(i, j)]))
        print


def conduct_knights_tour(board, knight_pos):
    """Conduct the actual knight's tour, return a board with either a complete or
       incomplete knight's tour.
    """

    for j in range(board['rows'] * board['cols']):
        board['board'][knight_pos] = j
        possible_moves = generate_possible_moves(board, knight_pos)

        if possible_moves == ():
            break

        move = random.choice(possible_moves)

        knight_pos = (knight_pos[0] + move[0], knight_pos[1] + move[1])

    return board


def generate_possible_moves(board, initial_pos):
    """Generate a list of possible moves from a given position."""

    possible_moves = ((-2, -1), (-2, 1), (-1, -2), (2, -1), (2, 1),
                      (1, -2), (1, 2))

    actual_possible_moves = ()

    for (movex, movey) in possible_moves:
        test_pos = (initial_pos[0] + movex, initial_pos[1] + movey)

        if (0 <= test_pos[0] < board["rows"] and
            0 <= test_pos[1] < board["cols"] and
            board['board'][test_pos] is None):
            actual_possible_moves += ((movex, movey),)

    return actual_possible_moves

def create_board(rows, cols):
    """Represents a chess board bundled with its amount of rows and columns."""

    keys = [(a, b) for a in range(rows) for b in range(cols)]
    board_dict = {key : None for key in keys}
    return {'board' : board_dict, 'rows' : rows, 'cols' : cols}


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

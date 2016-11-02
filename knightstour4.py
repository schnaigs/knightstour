import random
import sys

def main():
    """Conduct a knight's tour using a brute force method, representing the
       board as a dict.
    """

    if not valid_input():
        sys.exit("usage: python knightstour4.py rows columns attempts")

    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    attempts = int(sys.argv[3])

    for attempt in range(attempts):
        board = create_board(rows, cols)
        knight_pos = [0, 0]

        for j in range(rows * cols):
            board[tuple(knight_pos)] = j
            possible_moves = generate_possible_moves(knight_pos, board, rows, cols)

            if possible_moves == ():
                break

            move = random.choice(possible_moves)

            knight_pos[0] += move[0]
            knight_pos[1] += move[1]

        # at this point, all possible moves have been performed, and the knight's
        # tour is either complete or incomplete
        if None not in board.values():
            print "attempt #" + str(attempt + 1)
            print "Knight's tour complete!"
            print_board(board, rows, cols)
            sys.exit()

    # if this point is reached (i.e. sys.exit() is not called because a
    # complete tour was not found) then the knight's tour failed
    print "knight's tour failed!"
    print_board(board, rows, cols)


def generate_possible_moves(knight_pos, board, rows, cols):
    """Generate a list of possible moves from a given position."""

    possible_moves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1),
                      (1, -2), (1, 2))

    actual_possible_moves = ()

    for (movex, movey) in possible_moves:
        knight_pos[0] += movex
        knight_pos[1] += movey

        if (0 <= knight_pos[0] < rows and
            0 <= knight_pos[1] < cols and
            board[tuple(knight_pos)] == None):
            actual_possible_moves += ((movex, movey),)

        #reset knight_pos to check the next move
        knight_pos[0] -= movex
        knight_pos[1] -= movey

    return actual_possible_moves


def print_board(board, rows, cols):
    """Pretty-print a representation of the board."""

    for i in range(rows):
        for j in range(cols):
            if board[(i, j)] == None:
                print '{:3}'.format('x'),
            else:
                print '{:3}'.format(str(board[(i, j)])),
        print


def create_board(rows, cols):
    """Represents a board as a dictionary, mapping tuples representing positions
       on the board to values representing a potential position for the knight.
    """

    keys = [(a, b) for a in range(rows) for b in range(cols)]
    return {key : None for key in keys}


def valid_input():
    """Returns True if input is valid, False otherwise."""

    if len(sys.argv) != 4:
        return False

    try:
        r, c, a = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    except ValueError:
        return False

    if r < 1 or c < 1 or a < 0:
        return False

    return True


if __name__ == "__main__":
    main()

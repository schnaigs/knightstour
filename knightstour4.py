import random
import string
import sys

def main():
    """Conduct a knight's tour using a brute force method and backtracking,
       representing the board as a dict."""
    if not valid_input():
        sys.exit("usage: knightstour4.py rows columns")

    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    attempts = int(sys.argv[3])

    for attempt in range(attempts):
        print "attempt #" + str(attempt)
        board = create_board(rows, cols)

        knight_pos = [0, 0]

        # (rows * cols) - 1 is the only amount of moves it takes to complete an
        # open knight's tour
        for j in range(rows * cols):
            board[tuple(knight_pos)] = j

            possible_moves = generate_possible_moves(knight_pos, board, rows, cols)

            if possible_moves == []:
                break

            move = random.choice(possible_moves)

            knight_pos[0] = knight_pos[0] + move[0]
            knight_pos[1] = knight_pos[1] + move[1]

        if None in board.values():
            print "Knight's tour failed!"
        else:
            print "Knight's tour complete!"

        print_raw_board(board, rows, cols)


def generate_possible_moves(knight_pos, board, rows, cols):
    possible_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1),
                      (1, -2), (1, 2)]
    rv = []

    for (movex, movey) in possible_moves:
        knight_pos[0] = knight_pos[0] + movex
        knight_pos[1] = knight_pos[1] + movey

        if (knight_pos[0] >= 0 and
            knight_pos[1] >= 0 and
            knight_pos[0] < rows and
            knight_pos[1] < cols and
            board[tuple(knight_pos)] == None):
            rv.append((movex, movey))

        #reset knight_pos to check the next move
        knight_pos[0] = knight_pos[0] - movex
        knight_pos[1] = knight_pos[1] - movey

    return rv


def print_raw_board(board, rows, cols):
    keys_sorted = sorted(board.keys())
    for i in range(rows):
        for j in range(cols):
            print "{:4}".format(str(board[(i, j)])),
        print


def create_board(rows, cols):
    keys = [(a, b) for a in range(rows) for b in range(cols)]
    board = {key : None for key in keys}
    return board


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
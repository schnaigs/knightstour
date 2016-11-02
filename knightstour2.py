import random
import string
import sys

def main():
    """Conduct a knight's tour using a brute force method."""
    if not valid_input(sys.argv):
        sys.exit("usage: python knightstour2.py rows columns attempts")

    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    attempts = int(sys.argv[3])

    for i in range(attempts):
        print "attempt number: " + str(i)
        board = create_board(rows, cols)
        knight_pos = [0, 0]
        board[knight_pos[0]][knight_pos[1]] = i

        for j in range(rows * cols):
            possible_moves = generate_possible_moves(knight_pos, board, rows, cols)

            if possible_moves == []:
                break

            move = random.choice(possible_moves)

            knight_pos[0] += move[0]
            knight_pos[1] += move[1]
             
        list_of_positions = sum([], board)
        if None not in list_of_positions:
            print "attempt #" + str(i + 1)
            print "Knight's tour complete!"
            print_raw_board(board)
            sys.exit()

    print "knight's tour failed!"
    print_raw_board(board)


def create_board(r, c):
    """Creates a bare-bones representation of a chess board"""
    b = [[None for i in range(c)] for j in range(r)]
    return b


def generate_possible_moves(k, b, r, c):
    possible_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1),
                      (1, -2), (1, 2)]

    actual_possible_moves = []
    for (movex, movey) in possible_moves:
        k[0] = k[0] + movex
        k[1] = k[1] + movey
 
        if (0 <= k[0] < r and 
            0 <= k[1] < c and 
            b[k[0]][k[1]] == None):
            actual_possible_moves.append((movex, movey))

        # reset k
        k[0] = k[0] - movex
        k[1] = k[1] - movey

    return actual_possible_moves


def print_board(b):
    """Prints an actual chess board"""
    for i in range((len(b) - 1), -1, -1):
        for j in range(len(b[i])):
            if b[i][j] != None:
                print 'kt ',
            else:
                print str(i + 1) + string.ascii_lowercase[j] + " ",
        print


def print_raw_board(b):
    for i in range(len(b)):
        for j in range(len(b[i])):
            print "{:4}".format(b[i][j]),
        print

def valid_input(args):
    """Checks for valid input."""
    if len(sys.argv) != 4:
        return False

    try:
        rows, cols, attempts = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    except ValueError:
        return False

    # if the chessboard is smaller than 1x1, or attempts fewer than 0
    if rows < 1 or cols < 1 or attempts < 0:
        return False

    return True


if __name__ == '__main__':
    main()

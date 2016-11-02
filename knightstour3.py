import random
import string
import sys

def main():
    """Conduct a knight's tour using a brute force method and backtracking."""
    if not valid_input(sys.argv):
        sys.exit("usage: knightstour3.py rows columns")

    rows = int(sys.argv[1])
    cols = int(sys.argv[2])

    board = create_board(rows, cols)
    knight_pos = [0, 0]
    moves = []
    num_moves = 0

    board[0][0] = num_moves

    for j in range((rows * cols) - 1):
        actual_possible_moves = check_for_possible_moves(knight_pos, board, 
                                                         rows, cols)
        print "actual possible moves: " + str(actual_possible_moves)

        if len(actual_possible_moves) == 1:
            move = random.choice(actual_possible_moves)
            print "chosen move: " + str(move)
            moves.append(move)
            print "list of moves: " + str(moves)
            knight_pos[0] = knight_pos[0] + move[0]
            knight_pos[1] = knight_pos[1] + move[1]
            num_moves = num_moves + 1
            board[knight_pos[0]][knight_pos[1]] = num_moves

        print_raw_board(board)
        print

#       if len(actual_possible_moves) <= 1:
#           # backtrack
#           knight_pos[0] = knight_pos[0] - positions[num_positions][0]
#           knight_pos[1] = knight_pos[1] - positions[num_positions][1]


def print_board(board):
    """Prints an actual chess board"""
    for i in range((len(board) - 1), -1, -1):
        for j in range(len(board[i])):
            if board[i][j] != None:
                print 'kt ',
            else:
                print str(i + 1) + string.ascii_lowercase[j] + " ",
        print


def print_raw_board(board):
    for row in board:
        for pos in row:
            print "{:4}".format(pos),
        print


def check_for_possible_moves(knight_pos, board, rows, cols):
    possible_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1),
                      (1, -2), (1, 2)]

    actual_possible_moves = []

    for (movex, movey) in possible_moves:
        knight_pos[0] = knight_pos[0] + movex
        knight_pos[1] = knight_pos[1] + movey

        if (knight_pos[0] >= 0 and
            knight_pos[1] >= 0 and
            knight_pos[0] < rows and
            knight_pos[1] < cols and
            board[knight_pos[0]][knight_pos[1]] == None):
            actual_possible_moves.append((movex, movey))

        # reset knight to check the next move
        knight_pos[0] = knight_pos[0] - movex
        knight_pos[1] = knight_pos[1] - movey

    return actual_possible_moves
    


def create_board(rows, cols):
    """Creates a bare-bones representation of a chess board"""
    b = [[None for i in range(cols)] for j in range(rows)]
    return b


def valid_input(args):
    """Checks for valid input. Returns True if input is valid, False otherwise."""
    if len(sys.argv) != 3:
        return False

    try:
        rows, cols = int(sys.argv[1]), int(sys.argv[2])
    except ValueError:
        return False

    if rows < 1 or cols < 1:
        return False

    return True


if __name__ == "__main__":
    main()

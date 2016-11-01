import string
import sys
import random


def main():
    """Conduct a knight's tour using a brute force method"""

    if len(sys.argv) != 4:
        sys.exit("usage: knightstour.py rows columns attempts")

    rows = int(sys.argv[1])
    cols = int(sys.argv[2])

    board = create_board(rows, cols)
    knight = [0, 0]
    attempts = int(sys.argv[3])
    i = 0

    board[knight[0]][knight[1]] = 'kt'

    for i in range(attempts):
        knight = move(knight, board)

        board[knight[0]][knight[1]] = 'kt'

        print "board after moving the knight"
        print_board(board)


def create_board(r, c): 
    """Creates an actual chess board"""
    b = [[0 for i in range(r)] for j in range(c)]

    for i in range(len(b)):
        for j in range(len(b[i])):
            b[i][j] = str(i + 1) + string.ascii_lowercase[j]

    return b 
    

def print_board(b):
    """Prints an actual chess board"""
    for i in range((len(b)-1), -1, -1):
        for j in range(len(b[i])):
            print b[i][j],
        print


def move(k, b):
    possible_moves = [[-2,-1], [-2, 1], [-1, -2], [-1, 2], [2, -1], [2, 1], 
                      [1, -2], [1, 2]]
    the_move = random.choice(possible_moves)

    print "the move: " + str(the_move)

    k[0] = k[0] + the_move[0]
    k[1] = k[1] + the_move[1]

    print "knight's new position: " + str(k)
    if (k[0] < 0 or k[1] < 0 or b[k[0]][k[1]] == 'kt'):
        valid_pos = False
    else: 
        valid_pos = True

    print "is valid pos? " + str(valid_pos)
 
    while not valid_pos:
        # reset k
        k[0] = k[0] - the_move[0]
        k[1] = k[1] - the_move[1]

        # pick a new move
        the_move = random.choice(possible_moves)

        print "new move: " + str(the_move)

        # assign k its position plus the new move
        k[0] = k[0] + the_move[0]
        k[1] = k[1] + the_move[1]

        print "knight's new position: " + str(k)

        if (k[0] < 0 or k[1] < 0 or b[k[0]][k[1]] == 'kt'):
            valid_pos = False
        else :
            valid_pos = True

        print "is valid pos? " + str(valid_pos)

    return k


if __name__ == '__main__' :
    main()

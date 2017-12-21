#TODO: Minimax optimization/better heuristic
#TODO: Make more robust (bad input, full column, etc)
#TODO: Graphical interface
#TODO: Randomized Minimax among equal-value states
#TODO: Less hardcoding in this file
#TODO: Make Minimax cleaner (more understandable)

import lib.core as core
import lib.minimax as minimax

_BOARD_HEIGHT = 7
_BOARD_WIDTH  = 7
_DEPTH        = 5
FOOTER   = ("   " + "   ".join([str(x+1) for x in range(_BOARD_WIDTH)])
           +"\n")
OPPOSITE = {
    "X": "O",
    "O": "X"
}

def main():
    memory = {}
    board = core.Board(_BOARD_HEIGHT, _BOARD_WIDTH)
    token = "O"
    print(str(board) + "\n" + FOOTER)
    while not board.is_winner(token):
        token = OPPOSITE[token]
        print("It's {}'s turn. Which column do you want".format(token)
             +" to play? Enter 0 to undo last move.")
        if token == "X":
            col = int(input()) - 1
        else:
            col = minimax.minimax(board, token, _DEPTH, False, memory)[1]
        board.play_token(token, col)
        print("\n" + str(board) + "\n" + FOOTER)
        last_play_col = col
    print("{} has won the game!".format(token))

if __name__ == "__main__":
    main()


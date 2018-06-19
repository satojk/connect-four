#TODO: Make more robust (ties, etc)
#TODO: Graphical interface
#TODO: Randomized Minimax among equal-value states
#TODO: Less hardcoding in this file
#TODO: Make Minimax cleaner (more understandable)
#TODO: Space efficiency (e.g. when aggregating seqs)

import lib.core as core
import lib.alphabeta as alphabeta

_BOARD_HEIGHT = 6
_BOARD_WIDTH  = 7
_DEPTH        = 7
FOOTER   = (" " + " ".join([str(x+1) for x in range(_BOARD_WIDTH)])
           +"\n")
OPPOSITE = {
    "X": "O",
    "O": "X"
}

COLOR = {
    "X": "Blue",
    "O": "Red"
}

def play_from_input(board, token):
    while True:
        try:
            print("It's {}'s turn. Which column".format(COLOR[token])
                 +" do you want to play? Enter 0 to undo last move.")
            board.play_token(token, int(input())-1)
            break
        except Exception:
            print("\nThat is not a valid play!\n")

def play_from_minimax(board, token):
    mem = core.Memory()
    col = alphabeta.minimax(board, token, _DEPTH, False,
                            (float("-inf"),), (float("inf"),), mem)[1]
    while True:
        try: # In hopeless scenario, will play first available col
            board.play_token(token, col)
            break
        except Exception:
            col += 1

def main():
    board = core.Board(_BOARD_HEIGHT, _BOARD_WIDTH)
    token = "X"
    print(str(board) + FOOTER)
    while not board.is_winner(token):
        if board.is_tied():
            print("The game is tied!")
            token = "No one"
            break
        token = OPPOSITE[token]
        if token == "O":
            play_from_input(board, token)
        else:
            play_from_minimax(board, token)
        print("\n" + str(board) + "\n" + FOOTER)
    print("{} has won the game!".format(token))

if __name__ == "__main__":
    main()


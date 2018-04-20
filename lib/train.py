import core
from brain import Brain

_BOARD_HEIGHT = 6
_BOARD_WIDTH = 7
FOOTER = (" " + " ".join([str(x+1) for x in range(_BOARD_WIDTH)])
         +"\n")
OPPOSITE = {
    "X": "O",
    "O": "X"
}

_PATH_TO_EXPERIENCE = "experience.pkl"

def main():
    for trial in range(1000):
        board = core.Board(_BOARD_HEIGHT, _BOARD_WIDTH)
        token = "X"
        brains = [Brain("X", _PATH_TO_EXPERIENCE),
                  Brain("O", _PATH_TO_EXPERIENCE)]
        player = 0
        while not board.is_winner(token):
            if board.is_tied():
                break
            token = OPPOSITE[token]
            player = (player + 1) % 2
            to_play = brains[player].play_from_experience(board)
            board.play_token(
                token, to_play)
        print("Trial: {}\n{}".format(trial, board))
        brains[player].learn(True)
        brains[(player + 1) % 2].learn(False)

if __name__ == "__main__":
    main()

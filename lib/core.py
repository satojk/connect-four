# TODO: make more robust.
# TODO: make graphical interface.
import numpy as np

_BOARD_HEIGHT = 7
_BOARD_WIDTH  = 7
FOOTER = "   " + "   ".join([str(x+1) for x in range(_BOARD_WIDTH)]) + "\n"

class Board:

    def __init__(self, height, width):
        self.board = np.full((height, width), "_") 
        self.height = height
        self.width = width

    def __repr__(self):
        return str(self.board)

    def is_winner(self, token):
        seqs = []
        is_winner = False
        for i in range(self.height-3): #get all 4-diags
            for j in range(self.width):
                cur_diag = []
                if j >= 3:
                    seqs.append([self.board[i]  [j],
                                 self.board[i+1][j-1],
                                 self.board[i+2][j-2],
                                 self.board[i+3][j-3]])
                if j <= (self.width-4):
                    seqs.append([self.board[i]  [j],
                                 self.board[i+1][j+1],
                                 self.board[i+2][j+2],
                                 self.board[i+3][j+3]])
        for i in range(self.height): #get all 4-rows
            for j in range(self.width-3):
                seqs.append((self.board[i][j:j+4]).tolist())
        for i in range(self.height-3): #get all 4-cols
            for j in range(self.width):
                seqs.append((self.board[i:i+4,j]).tolist())
        for seq in seqs:
            if seq == [token]*4:
                is_winner = True
                break
        return is_winner
        
    def play_token(self, token, col):
        for i in range(self.height):
            if self.board[self.height-i-1][col] == "_":
                self.board[self.height-i-1][col] = token
                break
        else:
            raise Exception("Column is full!")

    def unplay_token(self, token, col):
        for i in range(self.height):
            if self.board[self.height-i-1][col] == token:
                self.board[self.height-i-1][col] = "_"
                break
        else:
            raise Exception("This token is not the last in this column")

class Game(Board):

    def __init__(self, height, width):
        super().__init__(height, width)
        print(str(self) + "\n" + FOOTER)

    def __repr__(self):
        return str(self.board)

    def play_turns(self):
        for token in ["X", "O"]:
            print("It's {}'s turn. Which column do you want to play? Enter 0 to undo last move.".format(token))
            col = int(input()) - 1
            self.play_token(token, col)
            print("\n" + str(self) + "\n" + FOOTER)
            if self.is_winner(token):
                print("{} has won the game!".format(token))
                return False
            last_play_col = col
        return True

def main():
    game = Game(_BOARD_HEIGHT, _BOARD_WIDTH)
    while game.play_turns():
        pass

if __name__ == "__main__":
    main()


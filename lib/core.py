# TODO: make more robust.
# TODO: make graphical interface.
import numpy as np

_BOARD_HEIGHT = 7
_BOARD_WIDTH  = 7
FOOTER = "   " + "   ".join([str(x+1) for x in range(_BOARD_WIDTH)]) + "\n"

class Game(object):

    def __init__(self, height, width):
        self.board = np.full((height, width), "_") 
        self.height = height
        self.width = width

    def __repr__(self):
        return str(self.board)

    def is_over(self):
        seqs = []
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
            if seq == ["X"]*4:
                print("X has won the game!")
                return True
            if seq == ["O"]*4:
                print("O has won the game!")
                return True
        return False
        
    def play_turns(self):
        for token in ["X", "O"]:
            print(str(self) + "\n" + FOOTER)
            if self.is_over():
                return False
            print("It's {}'s turn. Which column do you want to play?".format(token))
            col = int(input()) - 1
            print("\n")
            for i in range(self.height):
                if self.board[self.height-i-1][col] == "_":
                    self.board[self.height-i-1][col] = token
                    break
            else:
                raise Exception("Column is full!")
        return True

def main():
    game = Game(_BOARD_HEIGHT, _BOARD_WIDTH)
    while game.play_turns():
        pass

if __name__ == "__main__":
    main()


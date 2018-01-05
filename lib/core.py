import numpy as np

class Board:

    def __init__(self, height, width):
        self.board = np.full((height, width), "_") 
        self.height = height
        self.width = width

    def __repr__(self):
        outstr = (" " + "__"*self.width)[:-1]
        outstr += "\n"
        for row in self.board:
            for cell in row:
                outstr += "|"
                if cell == "X":
                    outstr += "\033[94mO\033[0m"
                elif cell == "O":
                    outstr += "\033[91mO\033[0m"
                else:
                    outstr += cell
            outstr += "|"
            outstr += "\n"
        return outstr

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_board(self):
        return self.board

    def col_is_full(self, col):
        return self.board[0][col] != "_"

    def is_tied(self):
        tie = True
        for row in self.board:
            for cell in row:
                if cell == "_":
                    tie = False
                    break
            if tie == False:
                break
        return tie

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
            if self.board[i][col] == token:
                self.board[i][col] = "_"
                break
        else:
            raise Exception("This token is not the last in this column")

class Memory:

    def __init__(self):
        self.dict = {}

    def __repr__(self):
        return str(self.dict)

    def consult(self, board, depth, alpha, beta):
        try:
            tuplified_board = tuple([tuple(row) for row in board])
            key = (tuplified_board, depth, alpha, beta)
            return self.dict[key]
        except KeyError:
            return False

    def write(self, board, depth, alpha, beta, value):
        tuplified_board = tuple([tuple(row) for row in board])
        key = (tuplified_board, depth, alpha, beta)
        self.dict[key] = value


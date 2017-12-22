import lib.core as core

OPPOSITE = {
    "X": "O",
    "O": "X"
}

def is_in_bounds(board, i, j):
    try:
        board[i][j]
        return True
    except IndexError:
        return False

def threes(board, token):
    net_seqs = 0
    seqs = []
    for i in range(board.get_height()-2):
        for j in range(board.get_width()):
            if j >= 2:
                seqs.append([board.get_board()[i]  [j],
                             board.get_board()[i+1][j-1],
                             board.get_board()[i+2][j-2]])
            if j <= (board.get_width()-3):
                seqs.append([board.get_board()[i]  [j],
                             board.get_board()[i+1][j+1],
                             board.get_board()[i+2][j+2]])
    for i in range(board.get_height()):
        for j in range(board.get_width()-2):
            seqs.append((board.get_board()[i][j:j+3]).tolist())
    for i in range(board.get_height()-2):
        for j in range(board.get_width()):
            seqs.append((board.get_board()[i:i+3,j]).tolist())
    for seq in seqs:
        if seq == [token]*3:
            net_seqs += 1
        elif seq == [OPPOSITE[token]]*3:
            net_seqs -= 1
    return net_seqs

def adjacencies(board, token):
    adjacencies = 0
    b = board.get_board()
    for i in range(board.get_height()):
        for j in range(board.get_width()):
            if (is_in_bounds(b, i, j)
            and b[i][j] == token):
                if (is_in_bounds(b, i, j+1)
                and b[i][j+1] == token):
                    adjacencies += 1
    return adjacencies

def potential(board, token):
    net_pot = 0
    seqs = []
    for i in range(board.get_height()-3):
        for j in range(board.get_width()):
            if j >= 3:
                seqs.append([board.get_board()[i]  [j],
                             board.get_board()[i+1][j-1],
                             board.get_board()[i+2][j-2],
                             board.get_board()[i+3][j-3]])
            if j <= (board.get_width()-4):
                seqs.append([board.get_board()[i]  [j],
                             board.get_board()[i+1][j+1],
                             board.get_board()[i+2][j+2],
                             board.get_board()[i+3][j+3]])
    for i in range(board.get_height()):
        for j in range(board.get_width()-3):
            seqs.append((board.get_board()[i][j:j+4]).tolist())
    for i in range(board.get_height()-3):
        for j in range(board.get_width()):
            seqs.append((board.get_board()[i:i+4,j]).tolist())
    for seq in seqs:
        if token in seq:
            net_pot += 1
    return net_pot


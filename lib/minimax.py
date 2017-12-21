import lib.core as core

OPPOSITE = {
    "X": "O",
    "O": "X"
}

def board_value(board, token):
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

# Type of minimax is sometimes float, sometimes (float, int).

def minimax(board, token, depth, flipswitch):
    if board.is_winner(token):
        return (float("inf"), 0)
    elif board.is_winner(OPPOSITE[token]):
        return (float("-inf"), 0)
    else:
        if depth == 0:
            return (board_value(board, token), 0)
        else:
            vals = []
            for potential_play in range(board.get_width()):
                if not board.col_is_full(potential_play):
                    if flipswitch:
                        token_to_play = OPPOSITE[token]
                    else:
                        token_to_play = token
                    board.play_token(token_to_play, potential_play)
                    vals.append((minimax(board, token, depth-1,
                                         not flipswitch)[0],
                                 potential_play))
                    board.unplay_token(token_to_play, potential_play)
            if flipswitch:
                return min(vals)
            else:
                return max(vals)


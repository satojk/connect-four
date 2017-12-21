import lib.core as core

OPPOSITE = {
    "X": "O",
    "O": "X"
}

def two_d_tuplify(two_d_array):
    out = []
    for row in two_d_array:
        out.append(tuple(row))
    return tuple(out)

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

def minimax(board, token, depth, flipswitch, memory):
    try: # Mechanism for dynamic programming approach
        if ((memory[two_d_tuplify(board.get_board())] == float("inf"))
         or (memory[two_d_tuplify(board.get_board())] == float("-inf"))
         or (depth == 0)):
            return (memory[two_d_tuplify(board.get_board())],)
    except KeyError:
        pass
    if board.is_winner(token): # Base cases: game is over or depth == 0
        memory[two_d_tuplify(board.get_board())] = float("inf")
        return (float("inf"),)
    elif board.is_winner(OPPOSITE[token]):
        memory[two_d_tuplify(board.get_board())] = float("-inf")
        return (float("-inf"),)
    else:
        if depth == 0:
            heuristic_guess = board_value(board, token)
            memory[two_d_tuplify(board.get_board())] = heuristic_guess
            return (heuristic_guess,)
        else: # Recursive case: take minimax of child nodes.
            vals = []
            for potential_play in range(board.get_width()):
                if not board.col_is_full(potential_play):
                    if flipswitch:
                        token_to_play = OPPOSITE[token]
                    else:
                        token_to_play = token
                    board.play_token(token_to_play, potential_play)
                    vals.append((minimax(board, token, depth-1,
                                         not flipswitch, memory)[0],
                                 potential_play))
                    board.unplay_token(token_to_play, potential_play)
            if flipswitch:
                return min(vals)
            else:
                return max(vals)


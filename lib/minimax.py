import lib.core as core
import lib.heuristics as heuristics

OPPOSITE = {
    "X": "O",
    "O": "X"
}

def minimax(board, token, depth, flipswitch):
    if board.is_winner(token): # Base cases: game is over or depth == 0
        return (float("inf"),)
    elif board.is_winner(OPPOSITE[token]):
        return (float("-inf"),)
    else:
        if depth == 0:
            return (heuristics.potential(board, token),)
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
                                 not flipswitch)[0], potential_play))
                    board.unplay_token(token_to_play, potential_play)
            if flipswitch:
                if len(vals) == 0: # Tie case - no possible moves
                    return (-999,)
                else:
                    return min(vals)
            else:
                if len(vals) == 0: # Tie case - no possible moves
                    return (999,)
                else:
                    return max(vals)


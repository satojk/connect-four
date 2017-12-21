import lib.core as core
import lib.heuristics as heuristics

OPPOSITE = {
    "X": "O",
    "O": "X"
}

def minimax(board, token, depth, flipswitch, memory):
    if board.is_winner(token): # Base cases: game is over or depth == 0
        return (float("inf"),)
    elif board.is_winner(OPPOSITE[token]):
        return (float("-inf"),)
    else:
        if depth == 0:
            return (heuristics.adjacencies(board, token),)
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


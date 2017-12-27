import lib.core as core
import lib.heuristics as heuristics

OPPOSITE = {
    "X": "O",
    "O": "X"
}

def min_val(val_play1, val_play2):
    if val_play1[0] > val_play2[0]:
        return val_play2
    else:
        return val_play1

def max_val(val_play1, val_play2):
    if val_play1[0] < val_play2[0]:
        return val_play2
    else:
        return val_play1

def minimax(board, token, depth, is_minimizing, alpha, beta):
    if board.is_winner(token): # Base cases: game is over or depth == 0
        return_val = (float("inf"),0)
    elif board.is_winner(OPPOSITE[token]):
        return_val = (float("-inf"),0)
    else:
        if depth == 0:
            return_val = (heuristics.potential(board, token),)
        else: # Recursive case: take minimax of child nodes.
            if is_minimizing:
                return_val = (999,0)
                for potential_play in range(board.get_width()):
                    if not board.col_is_full(potential_play):
                        board.play_token(OPPOSITE[token],
                                         potential_play)
                        next_val = (minimax(board, token, depth-1,
                                            not is_minimizing, alpha,
                                            beta)[0], potential_play)
                        return_val = min_val(return_val, next_val)
                        board.unplay_token(OPPOSITE[token],
                                           potential_play)
                        beta = min(beta, return_val)
                        if alpha >= beta:
                            break
            else:
                return_val = (-999,0)
                for potential_play in range(board.get_width()):
                    if not board.col_is_full(potential_play):
                        board.play_token(token,
                                         potential_play)
                        next_val = (minimax(board, token, depth-1,
                                            not is_minimizing, alpha,
                                            beta)[0], potential_play)
                        return_val = max_val(return_val, next_val)
                        board.unplay_token(token,
                                           potential_play)
                        alpha = max(alpha, return_val)
                        if alpha >= beta:
                            break
    return return_val


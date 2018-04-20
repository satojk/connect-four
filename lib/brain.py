import pickle
import random
import numpy as np

# At what rate should the last move played be learned?
_LEARNING_RATE = 0.3

# How much should the nth last move be learned relative to the n-1th last move?
_DISCOUNT_LEARNING_RATE = 0.8

class Brain:

    def __init__(self, token, path_to_experience) :
        self.token = token
        self.path_to_experience = path_to_experience
        with open(path_to_experience, "r+b") as exp_pickle:
            try:
                self.experience = pickle.load(exp_pickle)
            except EOFError:
                self.experience = {}
        self.last_moves = []

    def play_from_experience(self, scenario):
        potential_moves = list(range(scenario.get_width()))
        for col in range(scenario.get_width()):
            if scenario.col_is_full(col):
                potential_moves.remove(col)
        conversion = lambda x: (1 if x == self.token else
                                0 if x == "_" else 
                                -1)
        scenario = tuple(map(tuple,
                         np.vectorize(conversion)(scenario.get_board())))
        try:
            best_move = (0, float("-inf"))
            for potential_move in potential_moves:
                if self.experience[potential_move] > best_move[1]:
                    best_move = (potential_move, potential_moves[potential_move])
            self.last_moves.insert(0, (scenario, best_move[0]))
            if len(self.last_moves) == 10:
                self.last_moves.pop()
            return best_move[0]
        except KeyError:
            random_move = random.choice(potential_moves)
            self.last_moves.insert(0, (scenario, random_move))
            return random_move

    def learn(self, is_winner):
        mult = -0.3
        if is_winner: mult *= -1
        for scenario, move in self.last_moves:
            scenario = tuple(scenario)
            try:
                potential_moves = self.experience[scenario]
            except KeyError:
                self.experience[scenario] = {}
                potential_moves = {}
            try:
                prior_value = self.experience[scenario][move]
            except KeyError:
                self.experience[scenario][move] = 1
                prior_value = 1
            self.experience[scenario][move] += (prior_value * mult)
            mult *= 0.8
        with open(self.path_to_experience, "w+b") as exp_pickle:
            pickle.dump(self.experience, exp_pickle)


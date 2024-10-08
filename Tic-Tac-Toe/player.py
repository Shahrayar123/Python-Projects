import math 
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class  HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        while not valid_square:
            square = input(self.letter + '\'s turn. Input moves (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except:
                print('Invalid square. Try again.')

        return val
    

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square  = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.letter # Yourself
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None,
                    'score':1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: recursive using minimax to simulate a game making that move
            sim_score = self.minimax(state, other_player)
            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            # step 4: update the dictionaries if necessary
            if player ==  max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score # replace the best
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
    



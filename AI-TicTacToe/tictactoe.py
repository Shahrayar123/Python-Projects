"""
Tic Tac Toe Player
"""

import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count number of X and O from board
    # and then device whose turn is it
    count_x = sum(row.count(X) for row in board)
    count_o = sum(row.count(O) for row in board)
    if count_x <= count_o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Loop through board to find
    # which spot has None as value
    all_actions = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is None:
                all_actions.add((i, j))
    return all_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Return same board if action is None
    if action is None:
        return board

    # Else return new board with updated action
    board_state = copy.deepcopy(board)
    if board_state[action[0]][action[1]] is None:
        board_state[action[0]][action[1]] = player(board_state)
    else:
        raise Exception("Wrong move! Spot occupied.")
    return board_state


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal check for match
    for row in board:
        if row[0] == row[1] == row[2] and row[0]:
            return row[0]

    # Vertical check for match
    # We can use all() method but it can have overhead of for loops
    for idx in range(3):
        if board[0][idx] is not None:
            if board[0][idx] == board[1][idx] == board[2][idx]:
                return board[0][idx]

    # Diagonal check for match
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2]:
        return board[0][2]

    # Default
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If someone won or there is no action
    # left to perform on board, return true
    if winner(board) is not None:
        return True
    if len(actions(board)) == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_end = winner(board)
    if game_end is not None:
        if game_end == X:
            return 1
        elif game_end == O:
            return -1
    # If game is not over, return 0
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    # If board is empty then choose a random action from actions for AI
    if all(cell is None for row in board for cell in row):
        return random.choice(list(actions(board)))

    def min_value(state):
        """Finds the minimum value from the maximizing player states"""
        if terminal(state):
            return utility(state)
        else:
            v = float('inf')
            for a in actions(state):
                v = min(v, max_value(result(state, a)))
            return v

    def max_value(state):
        """Finds the minimum value from the minimizing player states"""
        if terminal(state):
            return utility(state)
        else:
            v = float('-inf')
            for a in actions(state):
                v = max(v, min_value(result(state, a)))
            return v

    # If its is O turn, AI will play as O, else as X
    # For every action from Action(s), check possible utility of action
    optimal_action = None
    if player(board) == O:
        best = float('inf')
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best:
                best = value
                optimal_action = action
    elif player(board) == X:
        best = float('-inf')
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best:
                best = value
                optimal_action = action

    return optimal_action

import random

def initialize_board():
    return [' ' for _ in range(10)]

def insert_letter(board, letter, pos):
    board[pos] = letter

def space_is_free(board, pos):
    return board[pos] == ' '

def print_board(board):
    print("\n   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]}")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {board[7]} | {board[8]} | {board[9]}")
    print("   |   |   ")

def is_board_full(board):
    return board.count(" ") <= 1

def is_winner(board, letter):
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7)
    ]
    return any(board[a] == board[b] == board[c] == letter for a, b, c in win_conditions)

def user_move(board):
    while True:
        try:
            pos = int(input("Enter a position between 1 to 9: "))
            if 1 <= pos <= 9:
                if space_is_free(board, pos):
                    insert_letter(board, "X", pos)
                    break
                else:
                    print("Sorry, this space is occupied.")
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Please enter a valid number.")

def comp_move(board):
    possible_moves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    
    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                return i

    corners_open = [i for i in possible_moves if i in [1, 3, 7, 9]]
    if corners_open:
        return select_random(corners_open)

    if 5 in possible_moves:
        return 5

    edges_open = [i for i in possible_moves if i in [2, 4, 6, 8]]
    if edges_open:
        return select_random(edges_open)

    return 0

def select_random(lst):
    return random.choice(lst)

def main():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not is_board_full(board):
        if not is_winner(board, "O"):
            user_move(board)
            print_board(board)
        else:
            print("Sorry, you lose!")
            return

        if not is_winner(board, "X"):
            move = comp_move(board)
            if move == 0:
                print("Tie game!")
                return
            else:
                insert_letter(board, "O", move)
                print(f"Computer placed 'O' on position {move}")
                print_board(board)
        else:
            print("You win!")
            return

    print("\nGame tie!")

while True:
    choice = input("Do you want to play a game (Y/N): ").strip().lower()
    if choice == 'y':
        main()
    else:
        break

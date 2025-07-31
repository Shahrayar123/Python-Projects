import random

# Initialize the board
board = [' ' for i in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsfree(pos):
    return board[pos] == ' '

def printBoard(board):
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |   ")

def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True

def isWinner(b, l):  # b = board, l = letter
    # Check all winning combinations
    return ((b[1] == l and b[2] == l and b[3] == l) or
            (b[4] == l and b[5] == l and b[6] == l) or
            (b[7] == l and b[8] == l and b[9] == l) or
            (b[1] == l and b[4] == l and b[7] == l) or
            (b[2] == l and b[5] == l and b[8] == l) or
            (b[3] == l and b[6] == l and b[9] == l) or
            (b[1] == l and b[5] == l and b[9] == l) or
            (b[3] == l and b[5] == l and b[7] == l))

def userMove():
    run = True
    while run:
        pos = input("Enter a position between 1 to 9: ")
        try:
            pos = int(pos)
            if 1 <= pos <= 9:
                if spaceIsfree(pos):
                    run = False
                    insertLetter("X", pos)
                else:
                    print("Sorry, this space is occupied.")
            else:
                print("Please enter a number between 1 and 9.")
        except:
            print("Please enter a valid number.")

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]

    # Try to win or block the player
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                return i

    # Choose corner
    cornersOpen = [i for i in possibleMoves if i in [1, 3, 7, 9]]
    if cornersOpen:
        return selectRandom(cornersOpen)

    # Choose center
    if 5 in possibleMoves:
        return 5

    # Choose edge
    edgesOpen = [i for i in possibleMoves if i in [2, 4, 6, 8]]
    if edgesOpen:
        return selectRandom(edgesOpen)

    return None  # <-- ✅ Added: Return None if no moves available (board is full)

def selectRandom(list_):
    return random.choice(list_)

def main():
    print("Welcome to the Tic Tac Toe game!\n")
    printBoard(board)

    while not isBoardFull(board):
        if not isWinner(board, "O"):
            userMove()
            printBoard(board)
        else:
            print("Sorry, you lose!")
            break

        if not isWinner(board, "X"):
            move = compMove()

            if move is None:  # <-- ✅ Fixed: Properly detect tie when no move is possible
                print("Tie game!")
                break  # <-- ✅ Added: Prevent crash and end the game
            else:
                insertLetter("O", move)
                print(f"Computer placed 'O' on position {move}")
                printBoard(board)
        else:
            print("You win!")
            break

    if isBoardFull(board):  # <-- Optional: Final check to declare tie
        if not isWinner(board, "X") and not isWinner(board, "O"):
            print("\nGame tie!")

# Game loop
while True:
    choice = input("Do you want to play a game (Y/N): ")
    if choice.lower() == 'y':
        board = [' ' for i in range(10)]
        print("-----------------------------------------")
        main()
    else:
        break

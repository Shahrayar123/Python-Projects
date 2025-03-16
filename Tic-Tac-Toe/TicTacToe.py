board = [' ' for i in range(10)]
player_score = 0
computer_score = 0

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
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
    return board.count(" ") <= 1

def isWinner(b, l):  # b = board, l = letter
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
                if spaceIsFree(pos):
                    run = False
                    insertLetter("X", pos)
                else:
                    print("Sorry, this space is occupied.")
            else:
                print("Please enter a number between 1 to 9.")
        except:
            print("Please enter a valid number.")

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornerOpen = [i for i in possibleMoves if i in [1, 3, 7, 9]]
    if cornerOpen:
        return selectRandom(cornerOpen)

    if 5 in possibleMoves:
        return 5

    edgeOpen = [i for i in possibleMoves if i in [2, 4, 6, 8]]
    if edgeOpen:
        return selectRandom(edgeOpen)

def selectRandom(lst):
    import random
    return random.choice(lst)

def main():
    global player_score, computer_score  # Use global variables for score tracking
    print("Welcome to the Tic-Tac-Toe game!\n")
    printBoard(board)

    while not isBoardFull(board):
        if not isWinner(board, "O"):
            userMove()
            printBoard(board)
        else:
            computer_score += 1
            print(f"Computer wins! 🤖 Your Score: {player_score} | Computer Score: {computer_score}")
            break

        if not isWinner(board, "X"):
            move = compMove()
            if move == 0:
                print("Tie game!")
                break
            else:
                insertLetter("O", move)
                print(f"Computer placed O on position {move}")
                printBoard(board)
        else:
            player_score += 1
            print(f"You win! 🎉 Your Score: {player_score} | Computer Score: {computer_score}")
            break

    if isBoardFull(board):
        print("\nGame tied!")
    
    print(f"Current Score -> You: {player_score} | Computer: {computer_score}")

while True:
    choice = input("Do you want to play a game (Y/N): ")
    if choice.lower() == 'y':
        board = [" " for i in range(10)]
        print("-----------------------------------------")
        main()
    else:
        print(f"Final Score -> You: {player_score} | Computer: {computer_score}")
        break

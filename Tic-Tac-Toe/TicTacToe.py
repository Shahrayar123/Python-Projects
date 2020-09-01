board = [' ' for i in range(10)]

def insertLetter(letter,pos):
    board[pos] = letter


def spaceIsfree(pos):
   return board[pos] == ' '

def printBoard(board):
    print("   |   |   ")
    print(" " +board[1] + " | "+ board[2]+ " | " + board[3])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " +board[4] + " | "+ board[5]+ " | " + board[6])
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

def isWinner(b,l):    # b = board, l = letter
    # check all possibilities
    return ((b[1] == l and b[2] == l and b[3] == l) or (b[4] == l and b[5] == l and b[6] == l) or (b[7] == l and b[8] == l and b[9] == l) or (b[1] == l and b[4] == l and b[7] == l) or (b[2] == l and b[5] == l and b[8] == l) or (b[3] == l and b[6] == l and b[9] == l) or (b[1] == l and b[5] == l and b[9] == l) or (b[3] == l and b[5] == l and b[7] == l))

def userMove():
    run = True

    while run:
        pos = input("Enter a position between 1 to 9: ")

        try:
            pos = int(pos)
            if (pos > 0) and (pos < 10):
                if spaceIsfree(pos):
                    run = False
                    insertLetter("X" , pos)
                else:
                    print("Sorry this space is occupied")

            else:
                print("Please enter a number range between 1 to 9")

        except:
            print("Please enter a number ")

def compMove():
    possibleMoves = [x for x,letter in enumerate(board) if letter == " " and x != 0]
    move = 0

    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let

            if isWinner(boardCopy,let):
                move = i
                return move

    cornorOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornorOpen.append(i)

    if len(cornorOpen) > 0:
        move = selectRandom(cornorOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgeOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgeOpen.append(i)


    if len(edgeOpen) > 0:
        move = selectRandom(edgeOpen)
        return move

def selectRandom(list_):
    import random
    ln = len(list_)
    r = random.randrange(0,ln)

    return list_[r]


def main():
    print("Welcome to the tic tac toe game\n")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, "O")):
            userMove()
            printBoard(board)

        else:
            print("Sorry you loose! ")
            break


        if not(isWinner(board, "X")):
            move = compMove()

            if move == 0:
                print("Tie game")

            else:
                insertLetter("O", move)
                print(f"Computer place O on position {move}")
                printBoard(board)

        else:
            print("You win! ")
            break

    if isBoardFull(board):
        print("\nGame tie")


while True:
    choice = input("Do you want to play a game (Y/N): ")
    if choice.lower() == 'y':
        board = [" " for i in range(10)]
        print("-----------------------------------------")
        main()
    else:
        break

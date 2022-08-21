def insertletter(letter, pos):
    board[pos] = letter


def spaceisfree(pos):
    return board[pos] == ' '


def printboard(a_board):
    print("   |   |   ")
    print(" " + a_board[7] + " | " + a_board[8] + " | " + a_board[9])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + a_board[4] + " | " + a_board[5] + " | " + a_board[6])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + a_board[1] + " | " + a_board[2] + " | " + a_board[3])
    print("   |   |   ")


def isboardfull(count_board):
    if count_board.count(" ") > 1:
        return False
    else:
        return True


def iswinner(b, letter):  # b = board, l = letter
    # check all possibilities

    return (b[1] == letter and b[2] == letter and b[3] == letter) or \
           (b[4] == letter and b[5] == letter and b[6] == letter) or \
           (b[7] == letter and b[8] == letter and b[9] == letter) or \
           (b[1] == letter and b[4] == letter and b[7] == letter) or \
           (b[2] == letter and b[5] == letter and b[8] == letter) or \
           (b[3] == letter and b[6] == letter and b[9] == letter) or \
           (b[1] == letter and b[5] == letter and b[9] == letter) or \
           (b[3] == letter and b[5] == letter and b[7] == letter)


def usermove():
    run = True

    while run:
        pos = input("Enter a position between 1 to 9: ")

        try:
            pos = int(pos)
            if (pos > 0) and (pos < 10):
                if spaceisfree(pos):
                    run = False
                    insertletter("X", pos)
                else:
                    print("Sorry this space is occupied")

            else:
                print("Please enter a number range between 1 to 9")

        except ValueError:
            print("Please enter a number ")


def compmove():
    possiblemoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]

    for let in ['O', 'X']:
        for i in possiblemoves:
            boardcopy = board[:]
            boardcopy[i] = let

            if iswinner(boardcopy, let):
                move = i
                return move

    cornoropen = []
    for i in possiblemoves:
        if i in [1, 3, 7, 9]:
            cornoropen.append(i)

    if len(cornoropen) > 0:
        move = selectrandom(cornoropen)
        return move

    if 5 in possiblemoves:
        move = 5
        return move

    edgeopen = []
    for i in possiblemoves:
        if i in [2, 4, 6, 8]:
            edgeopen.append(i)

    if len(edgeopen) > 0:
        move = selectrandom(edgeopen)
        return move


def selectrandom(list_):
    import random
    ln = len(list_)
    r = random.randrange(0, ln)

    return list_[r]


def main():
    print("Welcome to the tic tac toe game\n")
    printboard(board)

    while not (isboardfull(board)):
        if not (iswinner(board, "O")):
            usermove()
            printboard(board)

        else:
            print("Sorry you loose! ")
            break

        if not (iswinner(board, "X")):
            move = compmove()

            if move == 0:
                print("Tie game")

            else:
                insertletter("O", move)
                print(f"Computer place O on position {move}")
                printboard(board)

        else:
            print("You win! ")
            break

    if isboardfull(board):
        print("\nGame tie")


while True:
    choice = input("Do you want to play a game (Y/N): ")
    if choice.lower() == 'y':
        board = [" " for i in range(10)]
        print("-----------------------------------------")
        main()
    else:
        break

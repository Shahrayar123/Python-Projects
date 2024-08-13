#Initializing TicTacToe board  with 10 empty spaces, here we do not use the board[0] index
#Reason: To make the user select between 1 to 9 positions.

board = [' ' for i in range(10)] 

#This function is used to insert the symbol in the board at given position
#This function takes letter and position as arguments and add the letter to the board at the given position
#imagine the board as a list with continous 9 elements, initially filled with spaces and by calling insertLetter function, user add the symbol to the list 

def insertLetter(letter,pos):
    board[pos] = letter

# The spaceIsfree function is used to check the position, where the user want to insert symbol before calling insertLetter function,which inserts symbol in the board.
#After calling spaceIsfree function, it returns true if the position is free else it will return false 

def spaceIsfree(pos):
   return board[pos] == ' '

#printBoard function is used to print the board
#here this function takes board list as argument and print the symbols in TicTacToe board format
#In board list the symbols are stores according to the position.So the function print the symbols from the board list by specifing the position.

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
 
#Here is BoardFull function is used to check whether the board if full or not, We know that we dont use the board[0] to make the user comfort to insert 
#here the function checks the board list how many spaces are there. If there are more than one except the board[0] then the board has space to insert if it is equal to 1 then the board is full
#this function is called every time before inserting the symbol to the board

def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True
#Here the isWinner function is used to check the possible combinations to win the game.
#This function take the board and letter as arguments and check which symbol satisfies any of the condition to win TicTacToe game
#This function will be called twice, one for user and one for computer.

def isWinner(board,letter):    
                                                                    # check all possibilities and return true if the contion is satisfied else return false
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[7] == letter and board[8] == letter and board[9] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter))

#
def userMove():                                                     #userMove function is called when the chance is for user and when the board has space to fill 
    run = True

    while run:                                                      #the while loop itterates until the run is false. The run will be false after inserting the letter 
        pos = iinput("Enter a position between 1 to 9: ")           #here the user enter the positon to insert

        try:             
            pos = int(pos)                                          #try block is used to handle the exception if the user enter the string instead of number
            if (pos > 0) and (pos < 10):
                if spaceIsfree(pos):                                #we know that spaceIsfree function checks whether the position is free or not
                    run = False                 
                    insertLetter("X" , pos)                         #here the insertLetter function is called to insert the symbol in the board
                else:
                    print("Sorry this space is occupied")           #else is the position is not free then it will print the message
 
            else:                                                   #if the pos number is not in the range of 1 to 9 then it will print the message asking to enter the number again between 1 to 9
                print("Please enter a number range between 1 to 9")

        except:                                                     #here the except catch the error if the user enter string and ask to enter the integer
            print("Please enter a number ")                         #unless the symbol is inserted the loop will be itterated
                                                                    

def compMove():                                                     #This function is called when the chance is for computer and when the board has space to fill
    possibleMoves = [x for x,letter in enumerate(board) if letter == " " and x != 0] #here the free positions will be added to the possible moves list except 0 position by using list comprehension
    move = 0

    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let

            if isWinner(boardCopy,let):
                move = i
                return move

    cornorOpen = []                                                 #here the for loop is created to check the corners or free or not if the corner is free then it will be added to freecorner list
    for i in possibleMoves:
        if i in [1,3,7,9]:                                          #1,3,7,9 are the 4 corners of board
            cornorOpen.append(i)

    if len(cornorOpen) > 0:                                         #here if statement was created , if any corner is free then it will select the random corner from the list
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
    print("Welcome to the tic tac toe game\n")                      # Welcome message to the user
    printBoard(board)                                               #calling the printBoard function to print the board for the user so that the user can select the position to insert the symbol

    while not(isBoardFull(board)):                                  #while loop to check whether the board is full or not if not full then the loop will be itterated
        if not(isWinner(board, "O")):                               #if statement to check whether the computer wins or not if not then the user will get the chance to insert the symbol
            userMove()
            printBoard(board)

        else:
            print("Sorry you loose! ")
            break


        if not(isWinner(board, "X")):                               #if statement to check whether the user wins or not if not then the computer will get the chance to insert the symbol
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


while True:                                                         #while loop to ask the user whether he wants to play the game or not
    choice = input("Do you want to play a game (Y/N): ")   
    if choice.lower() == 'y':
        board = [" " for i in range(10)]
        print("-----------------------------------------")
        main()
    else:
        break

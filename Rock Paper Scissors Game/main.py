#Rock Paper Scissors game by marsian
print("\n\n\nRock Paper Scissors by marsian83\n\npresss Ctrl+. when you feel like exitting the game.")
input("\n\n<<PRESS ENTER TO BEGIN>>\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

#Framework declaration
from time import sleep
from random import choice
def game():
    print("\n\n\n\n\n\n\n\nDecide your move, enter \"R\" for Rock, \"S\" for Scissors and \"P\" for Paper.")
    tempVal=input()
    while tempVal not in 'RSPrsp':
        print("Decide your move, enter \"R\" for Rock, \"S\" for Scissors and \"P\" for Paper.")
        tempVal=input();
    sleep(0.13)
    if tempVal in "Rr":
        Pmove=1
    elif tempVal in "Pp":
        Pmove=2
    elif tempVal in "Ss":
        Pmove=3
    else:
        print("Custom_ERROR-01 : can't recognize user's input")
        raise SystemExit(0);

    sleep(0.13)
    Cmove=choice(MoveSet)
    if Cmove == 1:
        cpumove='Rock'
    elif Cmove == 2:
        cpumove='Paper'
    elif Cmove == 3:
        cpumove='Scissor'
    else:
        print("Custom_ERROR-00 : CPU's move unrecognizable")
        raise SystemExit(0)
    del tempVal;
    sleep(0.038)
    return Cmove, Pmove, cpumove
def decisive(Cmove,Pmove):
    if [Cmove,Pmove] == [1,3] or [Cmove,Pmove] == [2,1] or [Cmove,Pmove] == [3,2]:
        winner=1
    elif [Cmove,Pmove] == [1,2] or [Cmove,Pmove] == [2,3] or [Cmove,Pmove] == [3,1]:
        winner=2
    elif [Cmove,Pmove] == [1,1] or [Cmove,Pmove] == [2,2] or [Cmove,Pmove] == [3,3]:
        winner=0
    else:
        print("Custom_ERROR-03 : Set [cpumove,playermove] was assigned an unexpected value")
        raise SystemExit(0)
    return winner
def Scoreboard(winner,cm,cs,ps):
    if winner == 1:
        print("\nCPU won the round by choosing",cm)
        cs=cs+1
    elif winner == 2:
        print("\nPlayer won the round!")
        ps=ps+1
    else:
        print("Custom_ERROR-02 : Scoreboard function recieved explicit values")
        raise SystemExit(0)
    print("\nSession Score:")
    print("Player : ",ps)
    print("CPU : ",cs)
    return cs, ps

#Variable declaration
MoveSet = [1,2,3]
Cmove=0
Pmove=0
Cscore=0
Pscore=0

#Driver Code
while True:
    Cmove,Pmove,cpumove=game()
    winner=decisive(Cmove,Pmove)
    while winner == 0:
        print("WoW! A Draw! \nBoth Player and CPU have chosen",cpumove)
        print("Let's go again")
        Cmove,Pmove,cpumove=game()
        winner=decisive(Cmove,Pmove)
    sleep(0.13)
    cmCache=cpumove;
    print("CPU - ",cmCache)
    RoundWinner=winner
    cs,ps=Scoreboard(RoundWinner,cmCache,Cscore,Pscore)
    Cscore=cs; Pscore=ps
    input("<<< PRESS ENTER TO CONTINUE >>>");

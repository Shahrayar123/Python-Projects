import random

# Gives the player the option to begin the game or read the instructions first
helpQ = input("Press enter if you already know the rules and would like to begin playing. If you would like to read the rules before playing, press any other key: ")
if helpQ != '':
    print("To begin the game, you will be asked to place a bet. You can bet any amount between 1"
    "and your entire stack of chips. You will then be dealt two cards (face up), and the dealer"
    "will be dealt two cards (one up one down). The goal is to get the value of your hand closer to"
    "21 than the dealer (without going over). Aces are worth 1 or 11, face cards are worth 10, and all"
    "other cards are worth their face value. Once you are dealt your cards, you can choose to either hit"
    "(get another card) or stand (leave your hand as is). If you want to hit in our game, you will be"
    "prompted to hit the enter key. You can hit as many times as you want as long as the value of your"
    "hand remains under 21. However, if your hand surpasses 21, you bust and lose your entire bet. Once"
    "the player decides to stand, the dealers face down card will be revealed. As long as the dealers hand"
    "is under 17, they must hit. If it is between 17 and 21, they must stand. If it goes over 21, the dealer"
    "busts and you double your bet. This game does not allow any splitting or doubling down. Blackjack pays 3:2")


stack1 = 100
stack = stack1


# the main while loop that allows the player to run multiple individual rounds
playing = True
while playing:
    playerSum = 0
    dealerSum1 = 0
    dealerSum = 0
    playerHand = []
    dealerHand = []
    deck = ['2 of Clubs','3 of Clubs','4 of Clubs','5 of Clubs','6 of Clubs','7 of Clubs','8 of Clubs','9 of Clubs','10 of Clubs',
    'Jack of Clubs','Queen of Clubs','King of Clubs','Ace of Clubs','2 of Diamonds','3 of Diamonds','4 of Diamonds','5 of Diamonds','6 of Diamonds','7 of Diamonds','8 of Diamonds','9 of Diamonds',
    '10 of Diamonds','Jack of Diamonds','Queen of Diamonds','King of Diamonds','Ace of Diamonds',
    '2 of Spades','3 of Spades','4 of Spades','5 of Spades','6 of Spades','7 of Spades','8 of Spades','9 of Spades','10 of Spades',
    'Jack of Spades','Queen of Spades','King of Spades','Ace of Spades','2 of Hearts','3 of Hearts','4 of Hearts','5 of Hearts','6 of Hearts','7 of Hearts','8 of Hearts',
    '9 of Hearts','10 of Hearts','Jack of Hearts','Queen of Hearts','King of Hearts','Ace of Hearts']
    print("Your current stack is",stack,"chips. Please place a bet of up to",stack,"chips")
   
# allows the player to make a bet between 0 and their stack total
    x = True
    while x:
        bet = int(input("Place bet: "))
        if bet > stack or bet <= 0:
            print("Your bet is invalid. Please enter a number between 0 and",stack)
        else:
            x = False
            
# deals the player and the dealer their first two cards
    selectCard1 = random.randint(0,51)
    playerCard1 = deck[selectCard1]
    deck.pop(selectCard1)
    playerHand += playerCard1
    selectCard2 = random.randint(0,50)
    dealerCard1 = deck[selectCard2]
    deck.pop(selectCard2)
    dealerHand += dealerCard1
    selectCard3 = random.randint(0,49)
    playerCard2 = deck[selectCard3]
    deck.pop(selectCard3)
    playerHand += playerCard2
    selectCard4 = random.randint(0,48)
    dealerCard2 = deck[selectCard4]
    deck.pop(selectCard4)
    dealerHand += dealerCard2
    print("You are dealt the " + playerCard1, 'and the ' + playerCard2)
    blackjack = False
    
# determines if the player gets blackjack immediately after the deal
    if (((playerCard1[0]=='J'or playerCard1[0]=='Q'or playerCard1[0]=='K' or playerCard1[0]=='1') and (playerCard2[0]=='A')) or ((playerCard2[0]=='J'or playerCard2[0]=='Q'or playerCard2[0]=='K' or playerCard2[0]=='1') and (playerCard1[0]=='A'))):
        print("You have made Blackjack!. Your score is 21.")
        print("The dealer's cards are the",dealerCard1,"and the",dealerCard2)
        blackjack = True
        if (((dealerCard1[0]=='J'or dealerCard1[0]=='Q'or dealerCard1[0]=='K' or dealerCard1[0]=='1') and (dealerCard2[0]=='A')) or ((dealerCard2[0]=='J'or dealerCard2[0]=='Q'or dealerCard2[0]=='K' or dealerCard2[0]=='1') and (dealerCard1[0]=='A'))):
            print("The dealer has also made blackjack! You tie. You are returned your",bet,"chips")
            print("Your stack is still",stack,"chips.")
        else:
            print("You win! Your bet pays off 3:2. You earn",(bet*1.5),"chips!")
            stack += (bet*1.5)
            print("Your stack is now",stack,"chips.")
    
    if blackjack == False:
        
        print("The dealer is dealt the" , dealerCard1 , 'and a second card face down.')
            
        #add points of playercard 1
        if playerCard1[0]=='A':
            choice1 = input("Press enter if you would like the ace to count as 1, or press any other key if you would like the ace to count as 11: ")
            if choice1 == '':
                playerSum += 1
            else:
                playerSum += 11
        elif playerCard1[0]=='J'or playerCard1[0]=='Q'or playerCard1[0]=='K' or playerCard1[0]=='1':
            playerSum += 10
        else:
            playerSum += int(playerCard1[0])
                
        #add points of playercard 2      
        if playerCard2[0]=='A':
            choice2 = input("Press enter if you would like the ace to count as 1, or press any other key if you would like the ace to count as 11: ")
            if choice2 == '':
                playerSum += 1
            else:
                playerSum += 11
        elif playerCard2[0]=='J'or playerCard2[0]=='Q'or playerCard2[0]=='K' or playerCard2[0]=='1':
            playerSum += 10
        else:
            playerSum += int(playerCard2[0])
                
        #add dealer points     
        if dealerCard1[0]=='A':
            dealerSum += 11
            dealerSum1 += 11
        elif dealerCard1[0]=='J'or dealerCard1[0]=='Q'or dealerCard1[0]=='K' or dealerCard1[0]=='1':
            dealerSum += 10
            dealerSum1 += 10
        else:
            dealerSum += int(dealerCard1[0])
            dealerSum1 += int(dealerCard1[0])
        
        print('Dealer Total = ' , dealerSum)
              
        # dealer face down card
        if dealerCard2[0]=='A':
            if dealerSum < 11:
                dealerSum += 11
            else:
                dealerSum += 1
        elif dealerCard2[0]=='J'or dealerCard2[0]=='Q'or dealerCard2[0]=='K' or dealerCard2[0]=='1':
            dealerSum += 10
        else:
            dealerSum += int(dealerCard2[0])
                
        print('Player Total = ' , playerSum)
            
            
# While loop that contintues to deal cards as long as the player decides to hit and their score is below 21  
        numCards = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
                    31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]

        decision = input("Press enter if you would like to hit, or press any other key if you would like to stand: ")
        while decision == '' and playerSum < 21:
            selectCard = random.randint(0,numCards[-1])
            playerCard = deck[selectCard]
            deck.pop(selectCard)
            numCards.pop()
            playerHand += playerCard
            print("You are dealt the " + playerCard)
            if playerCard[0]=='A':
                choice = input("Press enter if you would like the ace to count as 1, or press any other key if you would like the ace to count as 11: ")
                if choice == '':
                    playerSum += 1
                else:
                    playerSum += 11
            elif playerCard[0]=='J'or playerCard[0]=='Q'or playerCard[0]=='K' or playerCard[0]=='1':
                playerSum += 10
            else:
                playerSum += int(playerCard[0])
            print("Your new score is " , playerSum)
     
# breaks the loop if the player goes over 21
            if playerSum > 21:
                print("You have gone over 21! You lose",bet,"chips!")
                stack -= bet
                break
            
# automatically forces the player to stand if their score equals 21           
            if playerSum == 21:
                decision = 'stand'
                break
            decision = input("Press enter if you would like to hit, or press any other key if you would like to stand: ")
       
# displays the dealer's second card if the player decides to stand   
        if decision != '' and playerSum <= 21:
            print("The dealer's second card is the " + dealerCard2)
            print("Dealer Total = " , dealerSum)
            print("Player Total = " , playerSum)
            
# deals cards to the dealer until their score reaches 17            
            while dealerSum < 17:
                selectCard = random.randint(0,numCards[-1])
                dealerCard = deck[selectCard]
                deck.pop(selectCard)
                numCards.pop()
                dealerHand += dealerCard
                print("The dealer is dealt the " + dealerCard)
                if dealerCard[0]=='A':
                    if dealerSum < 11:
                        dealerSum += 11
                    else:
                        dealerSum += 1
                elif dealerCard[0]=='J'or dealerCard[0]=='Q'or dealerCard[0]=='K' or dealerCard[0]=='1':
                    dealerSum += 10
                else:
                    dealerSum += int(dealerCard[0])
                print("The dealer's new total is" , dealerSum)
                
 # Ends the code if the dealer busts               
        if dealerSum > 21:
            print("The dealer has gone over 21! You win",bet,"chips!")
            stack += bet
        
 # determines the winner of the round if neither the player or the dealer busts       
        if dealerSum <= 21 and playerSum <= 21:
            if dealerSum > playerSum:
                print("The dealer has a higher score than you! You lose",bet, "chips!")
                stack -= bet
            elif playerSum > dealerSum:
                print("You have a higher score than the dealer! You win",bet,"chips!")
                stack += bet
            elif playerSum == dealerSum:
                print("You tied! You have the same score as the dealer.")
                print("The game is over, you are returned your",bet,"chips")
        
 # ends the game if the player runs out of chips       
        if stack <= 0:
            print("You are out of chips. GAME OVER!")
            break
        print("Your current stack is",stack,"chips.")
        
        
# Allows the player to continue playing & build upon their stack, or walk away after each round
    var = input("If you would like to play again, press enter. If you would like to quit, press any other key: ")
    if var != '':
        playing = False
        if stack>stack1:
            print("Well done! You have cashed out with",stack,"chips. Your net earnings are",(stack-stack1),"chips!")
        elif stack<stack1:
            print("Unlucky! You have cashed out with",stack,"chips. Your net losses are",(stack1-stack),"chips.")
        else:
            print("You have cashed out with",stack,"chips. You broke even.")


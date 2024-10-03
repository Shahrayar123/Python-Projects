import random

cards = {
    'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 10, 'Queen': 10, 'King': 10
}

def create_deck():
    return list(cards.keys()) * 4

def deal_card(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

def calculate_hand(hand):
    total = sum(cards[card] for card in hand)
    aces = hand.count('Ace')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def play_blackjack():
    ##init deck and hands -> dealer and player
    deck = create_deck()
    player_hand = []
    dealer_hand = []
    player_hand.append(deal_card(deck))
    player_hand.append(deal_card(deck))
    dealer_hand.append(deal_card(deck))
    dealer_hand.append(deal_card(deck))

    while True:
        print(f"\nYour hand: {player_hand}, Total: {calculate_hand(player_hand)}")
        print(f"Dealer's hand: [{dealer_hand[0]}, Hidden]")

        #immediate win
        if calculate_hand(player_hand) == 21:
            print("Blackjack! You win!")
            return

        ##hit or stand
        choice = input("Do you want to (H)it or (S)tand? ").lower()
        if choice == 'h':
            player_hand.append(deal_card(deck))
            if calculate_hand(player_hand) > 21:
                print(f"\nYour hand: {player_hand}, Total: {calculate_hand(player_hand)}")
                print("Bust! You lose.")
                return
        elif choice == 's':
            break

    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

    print(f"\nYour hand: {player_hand}, Total: {calculate_hand(player_hand)}")
    print(f"Dealer's hand: {dealer_hand}, Total: {calculate_hand(dealer_hand)}")

    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)

    #game state conditions
    if dealer_total > 21:
        print("Dealer busts! You win!")
    elif player_total > dealer_total:
        print("You win")
    elif player_total < dealer_total:
        print("Dealer wins")
    else:
        print("It's a tie")

#Main game loop
while True:
    play_blackjack()
    play_again = input("Do you want to play again? (Y/N) ").lower()
    if play_again != 'y':
        break

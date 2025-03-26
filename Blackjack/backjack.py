import random

class CardDeck:
    """Represents a deck of cards for Blackjack."""
    
    def __init__(self):
        self.deck = self.create_deck()
        
    def create_deck(self):
        cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        random.shuffle(cards)
        return cards
    
    def draw_card(self):
        """Draw a card from the deck."""
        return self.deck.pop()

class Player:
    """Represents a player in the game (either player or dealer)."""
    
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def add_card(self, card):
        """Add a card to the player's hand."""
        self.hand.append(card)
        
    def calculate_hand_value(self):
        """Calculate the total value of the hand with Ace adjustments."""
        value = 0
        aces = 0
        
        for card in self.hand:
            if card in ['J', 'Q', 'K']:
                value += 10
            elif card == 'A':
                value += 11
                aces += 1
            else:
                value += int(card)
        
        # Adjust for Aces if value goes over 21
        while value > 21 and aces:
            value -= 10
            aces -= 1
            
        return value
    
    def show_hand(self, hide_first_card=False):
        """Show the player's hand. Optionally hide the first card (for dealer)."""
        if hide_first_card:
            print(f"{self.name}'s Hand: ['X', {self.hand[1]}] (Value: Hidden)")
        else:
            print(f"{self.name}'s Hand: {' '.join(self.hand)} (Value: {self.calculate_hand_value()})")
    
    def is_busted(self):
        """Check if the player has busted (hand value > 21)."""
        return self.calculate_hand_value() > 21

class BlackjackGame:
    """Represents the main Blackjack game logic."""
    
    def __init__(self):
        self.deck = CardDeck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")
    
    def deal_initial_cards(self):
        """Deal two cards to both the player and the dealer."""
        for _ in range(2):
            self.player.add_card(self.deck.draw_card())
            self.dealer.add_card(self.deck.draw_card())
    
    def player_turn(self):
        """Handle the player's turn."""
        while True:
            self.player.show_hand()
            choice = input("\nDo you want to [h]it or [s]tand? ").lower()
            if choice == 'h':
                self.player.add_card(self.deck.draw_card())
                if self.player.is_busted():
                    self.player.show_hand()
                    print("\nYou busted!")
                    break
            elif choice == 's':
                break
            else:
                print("Invalid input, please choose 'h' for hit or 's' for stand.")
    
    def dealer_turn(self):
        """Handle the dealer's turn."""
        print("\nDealer's turn...")
        self.dealer.show_hand()  # Reveal dealer's full hand
        
        while self.dealer.calculate_hand_value() < 17:
            print("Dealer hits.")
            self.dealer.add_card(self.deck.draw_card())
            self.dealer.show_hand()
            if self.dealer.is_busted():
                print("\nDealer busted!")
                break
    
    def determine_winner(self):
        """Determine the winner based on the hand values."""
        player_value = self.player.calculate_hand_value()
        dealer_value = self.dealer.calculate_hand_value()
        
        if self.player.is_busted():
            return "You busted! Dealer wins."
        elif self.dealer.is_busted():
            return "Dealer busted! You win!"
        elif player_value == dealer_value:
            return "It's a tie!"
        elif player_value > dealer_value:
            return "You win!"
        else:
            return "Dealer wins."
    
    def play(self):
        """Play the game."""
        print("Welcome to Blackjack!")
        self.deal_initial_cards()
        self.dealer.show_hand(hide_first_card=True)  # Hide dealer's first card
        
        # Player's turn
        self.player_turn()
        
        # Dealer's turn (if player hasn't busted)
        if not self.player.is_busted():
            self.dealer_turn()
        
        # Determine and show the result
        print("\nFinal Result:")
        print(self.determine_winner())

# Play the game
while True:
  choice = input("Do you want to play a game (Y/N): ")
  if choice == 'N':
    break;
  else:
    if __name__ == "__main__":
        game = BlackjackGame()
        game.play()


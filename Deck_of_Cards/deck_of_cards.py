import random


class Card(object):

    dict1 = {
        1: "Ace",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Jack",
        12: "Queen",
        13: "King",
    }

    def __init__(self, suit, val):
        self.suit = suit
        self.value = Card.dict1[val]

    def show(self):
        print(f"{self.value} of {self.suit}")


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def showCards(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()


card = Card("Clubs", 1)
card.show()

mydeck = Deck()
mydeck.shuffle()
mydeck.showCards()


player1 = Player("Shubham")
player1.draw(mydeck)
player1.showHand()

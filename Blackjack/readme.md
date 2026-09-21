# Basic Blakjack game

This project is a text-based Blackjack game written in Python. It simulates a simple version of Blackjack, where the player competes against the dealer. The goal of the game is to beat the dealer by having a hand value as close to 21 as possible without going over.

## Description

Blackjack is a popular card game where the goal is to have a hand value as close to 21 as possible without exceeding it. Players are dealt two cards initially and can choose to "hit" (draw a card) or "stand" (keep their hand). The dealer also plays by drawing cards until their hand totals at least 17. The player wins if their hand value is higher than the dealer's without exceeding 21, or if the dealer busts (goes over 21).

## Prerequisites

- Python 3.x

## Usage

- Clone or download this repository to your local machine.
- Open a terminal or command prompt and navigate to the directory containing the code.
- Run the game by executing:
  > python blackjack.py

## Controls

- Hit: Draw another card to your hand.
- Stand: End your turn and let the dealer play.
- The game will display the winner based on the rules of Blackjack.

## For Customization

You can modify the following aspects in the code to customize the game:

- Card Deck: Change the cards by adjusting the deck list in the CardDeck class.
- Dealer's Strategy: Modify the dealer's behavior in the dealer_turn method.
- Game Rules: You can tweak the values assigned to face cards, change the threshold for the dealer's stopping point (currently 17), or implement advanced Blackjack features like splitting or doubling down.

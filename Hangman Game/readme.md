# Hangman Game

This Python script is a simple implementation of the classic Hangman game. The game selects a random word from a webpage and the player has to guess it by suggesting letters, within a limited number of chances.

## Features

- Random word selection from a specific website.
- Limited number of guesses before the player loses.
- Visual representation of the hangman as the player loses chances.

## How to Play

1. Run the script.
2. Enter your name when prompted.
3. The game will then fetch a random word and start the guessing process.
4. Enter one letter at a time to guess the word.
5. If the guessed letter is not in the word, a part of the hangman will appear, and the number of remaining chances decreases.
6. The game continues until the player correctly guesses the word or the hangman is fully drawn.

## Requirements

- Python 3.x
- `requests` library
- `lxml` library

## Setup and Installation

1. Ensure you have Python installed on your machine.
2. Install the required libraries using pip:

   ```bash
   pip install requests lxml

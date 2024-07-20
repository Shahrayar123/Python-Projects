# Hangman Game

Welcome to the Hangman game! This project implements a simple command-line version of the classic Hangman game using Python. The game fetches random words from an online source and challenges the player to guess the word within a limited number of attempts.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Code Explanation](#code-explanation)
5. [License](#license)

## Introduction

The Hangman game is a popular word-guessing game where the player has to guess the word by suggesting letters within a certain number of attempts. In this implementation, random words are fetched from an online source, and the player has 10 chances to guess the word correctly.

## Installation

To run this project, you need to have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

Additionally, you need to install the `requests` and `lxml` libraries. You can install them using `pip`:

```bash
pip install requests lxml
```

## Usage

1. Clone this repository or download the script file.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using the following command:

```bash
python hangman.py
```

4. Enter your name when prompted.
5. Guess the word by entering one letter at a time.

## Code Explanation

The script is divided into several parts:

### Importing Libraries

```python
import requests
import random
from lxml import etree
```

- `requests`: Used to send HTTP requests to fetch the word.
- `random`: Used to select random letters and words.
- `lxml`: Used to parse the HTML content.

### Random Choices

```python
alphabetChoice = random.choice(["a","b","c","d","e","f","g","h","i"])
columnChoice = random.choice(range(1, 3))
wordChoice = random.choice(range(1, 10))
```

These lines randomly choose an alphabet and word position to fetch the word from the online source.

### Checking the Player's Name

```python
def checkName(name):
    if name == "":
        print("Sorry, you did not enter your name")
        return 0
    else:
        print("\n--------------------------------------\n")
        return 1
```

This function checks if the player has entered a name.

### Hangman Game Function

```python
def hangman():
    ...
```

The `hangman` function contains the main logic of the game:
- Fetches a random word from the online source.
- Parses the HTML content to extract the word.
- Prompts the player to guess the word.
- Provides feedback and updates the player's remaining chances.
- Displays the hangman diagram as the player makes incorrect guesses.

### Starting the Game

```python
name = input("Hey there! What is your name: ")

if checkName(name):
    print(name+" lets play a game")
    hangman()
else:
    pass
```

This section prompts the player for their name and starts the game if a valid name is provided.

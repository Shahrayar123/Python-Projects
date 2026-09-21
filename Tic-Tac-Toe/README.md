# Tic Tac Toe Game

This is a simple implementation of the classic Tic Tac Toe game in Python.

## Overview

The program allows a user to play Tic Tac Toe against the computer. The game board is represented as a list, and players can place their respective letters ('X' for the user and 'O' for the computer) on the board by choosing positions from 1 to 9.

## How to Use

1. Run the Python script.
2. Follow the prompts to play the game.
3. Enter positions on the board by inputting numbers from 1 to 9.
4. Enjoy the game!

## Functions

### `insertLetter(letter, pos)`

Inserts the specified letter at the given position on the board.

### `spaceIsFree(pos)`

Checks if the specified position on the board is empty.

### `printBoard(board)`

Prints the current state of the game board.

### `isBoardFull(board)`

Checks if the game board is full, indicating a tie.

### `isWinner(board, letter)`

Checks if the specified player (letter) has won the game.

### `userMove()`

Handles the user's move by taking input for their chosen position.

### `compMove()`

Handles the computer's move using basic AI logic to determine the best possible move.

### `selectRandom(list_)`

Selects a random move from a list of available moves.

### `main()`

Runs the main game loop and controls the flow of

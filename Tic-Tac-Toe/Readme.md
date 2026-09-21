# Tic Tac Toe Game

This is a simple Tic Tac Toe game implemented in Python. You can play against the computer.

## How to Play

1. Run the Python script.
2. You will be asked to make moves by entering the position (1 to 9) where you want to place your 'X'.
3. The computer will make its move automatically.
4. The game continues until either you or the computer wins, or the board is full (a tie).

## Instructions

- The game board is represented by numbers from 1 to 9 corresponding to the positions as shown below:
    ```
       |   |
     1 | 2 | 3
    ---|---|---
       |   |
     4 | 5 | 6
    ---|---|---
       |   |
     7 | 8 | 9
       |   |
    ```

- You (the player) will be represented by 'X' and the computer by 'O'.
- To make a move, enter the position number where you want to place your 'X'.

## Functions

- `insertLetter(letter, pos)`: Inserts a letter ('X' or 'O') at the specified position on the board.
- `spaceIsFree(pos)`: Checks if a space on the board is free at the specified position.
- `printBoard(board)`: Prints the current state of the board.
- `isBoardFull(board)`: Checks if the board is full (no empty spaces left).
- `isWinner(b, l)`: Checks if a player ('X' or 'O') has won the game.
- `userMove()`: Allows the user to make a move.
- `compMove()`: Determines the computer's move.
- `selectRandom(list_)`: Selects a random element from a list.
- `main()`: Main function to run the game.

## Running the Game

1. Clone or download this repository.
2. Open a terminal and navigate to the directory containing the Python script.
3. Run the script using the command `python TicTacToe.py`.
4. Follow the on-screen instructions to play the game.

Enjoy playing Tic Tac Toe!

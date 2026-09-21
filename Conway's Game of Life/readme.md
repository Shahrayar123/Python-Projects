
## Conway's Game of Life in Python

This is a simple implementation of Conway's Game of Life using Python and the Pygame library.

## Description

Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning its evolution is determined by its initial state, requiring no further input. The game is played on a grid of cells, each of which can be alive or dead. The game progresses in steps, with each step following a set of rules to determine the state of each cell in the next generation.

In this Python implementation, we've created a grid of cells on the screen. You can interact with the game by clicking on cells to bring them to life or kill them. Pressing the spacebar will start and stop the game's automatic progress. The game will evolve according to the rules of Conway's Game of Life.

## Prerequisites

- Python 3.x
- Pygame
- Numpy
- You can install it using pip:


pip install -r requirements.txt


## Usage

- Clone or download this repository to your local machine.
- Open a terminal or command prompt and navigate to the directory containing the code.
- Run the game by executing python conways_game_of_life.py.


## Controls

- Left mouse click: Toggle cell state (alive or dead).
- Spacebar: Start or stop the automatic progression of the game.
- Close the game window to exit.


## Customization
You can customize the game by modifying the following constants in the code:

- COLOR_BG: Background color.
- COLOR_GRID: Grid color.
- COLOR_DIE_NEXT: Color of cells that will die in the next generation.
- COLOR_ALIVE_NEXT: Color of cells that will survive in the next generation.
- TICK_SPEED: Speed of the game's progression (frames per second).
- cells = np.zeros((60, 80)): Initial state of the grid. You can change the grid size and initial configuration here.
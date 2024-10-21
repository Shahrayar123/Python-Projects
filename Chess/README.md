# Chess

## Overview
This is a Python-based Chess game that allows two players to compete against each other or one player to face a bot on the same machine. The game includes the full set of chess rules, such as castling, en passant, and pawn promotion. Currently, there are two bot difficulty levels: `Easy` and `Medium`, both explained in the script. A `Hard` mode is also available but commented out as its logic hasn't been implemented yet. Feel free to challenge yourself by completing it!

## Features
- Complete implementation of chess rules
- Playable with two players or against a simple bot
- Graphical user interface (GUI) using Pygame
- Move validation, check, and checkmate detection
- Game restart functionality

## Requirements
- Python 3.x
- [Pygame](https://pypi.org/project/pygame/) library
- [Chess](https://pypi.org/project/chess/) library

## How to Play
To start the game, run the following command:

```sh
python main.py
```

## Contributing
Feel free to fork this project and contribute to its development! Some potential updates include:

- Implement the `Hard` mode bot logic (then uncomment all its references).
- Add a countdown timer and support time increments for matches.
- Improve the GUI styling (e.g., buttons, title, etc.).
- Add an "Exit" button alongside the "Restart" button on the main screen.

Contributions in any form are welcome—be it code, bug reports, or feature suggestions!

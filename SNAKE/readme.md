## Snake game

### This is a classic implementation of the Snake Game using Python's 'turtle' module.

#### Goal:
- The player controls a snake, navigating it around a confined box to eat food and grow in length.
- It consumes as much food as possible without colliding with the snake's own body or exiting the game boundaries.

#### Game Mechanics:
- The game starts with a snake of five segments positioned in the center of the screen, moving upward by default.
- The food appears randomly on the screen within the boundaries, and the player must guide the snake to collide with the food to grow the snake.
- After consuming the food, the score increases by 10 points, and a new food piece is generated at a random position.

#### Screen Wrapping:
- If the snake moves beyond the edges of the box, it will reappear on the opposite side of the screen, allowing for continuous gameplay without hitting the borders.

#### Collision Detection:
- If the snake's head collides with any part of its own body, the game resets, and the current score is displayed.

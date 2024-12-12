```markdown
# Fractal Drawing with Turtle Graphics

This project generates fractals using Python's Turtle Graphics and an L-System (Lindenmayer System).

## Features
- Generates fractal patterns based on defined production rules.
- Customizable parameters for axiom, iterations, and angles.

## Installation

1. install pygame library by "pip install pygame"

## Usage

1. Clone this repository or download the files.
2. Open the `fractal_drawing.py` file in your preferred text editor or IDE.
3. Run the script using Python:
   ```bash
   python fractal_drawing.py
   ```

## Code Overview

- **Production Rules**: Defines how the initial axiom transforms over iterations.
- **apply_rules()**: Applies the defined rules to generate the final string.
- **draw_fractal()**: Interprets the final string and draws the fractal using turtle graphics.

## Configuration

Modify the following parameters in the `main()` function to change the fractal's appearance:
- **Axiom**: Initial string (e.g., `'VZFFF'`).
- **Iterations**: Number of times to apply the production rules (e.g., `12`).
- **Angle**: Angle for turtle turns (e.g., `30` degrees).

## Example Output

Running the script generates a fractal pattern that visually represents branching structures.


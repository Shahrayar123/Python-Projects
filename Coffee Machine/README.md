# ☕ Coffee Machine Project

This is a simple Python project that simulates a coffee vending machine.  
Users can choose from different types of coffee, insert coins to pay, and receive their drinks if enough resources and payment are available.

## Features

- Menu options: **Latte**, **Espresso**, **Cappuccino**
- Coin collection and payment processing
- Resource checking (water, milk, coffee)
- Transaction management (gives change if needed)
- Report generation for current resources and earnings
- Machine shutdown option (`off` command)

## How It Works

1. The machine asks, **"What would you like? (latte/espresso/cappuccino)"**.
2. If enough ingredients are available:
   - It asks how many coins the user is inserting (5, 10, 20 coins).
   - It checks if the inserted money is enough.
   - If yes, it deducts ingredients, gives change if needed, and serves coffee.
   - If not, it refunds the money.
3. Special Commands:
   - Type `report` to see the current resources and money.
   - Type `off` to turn off the machine.

## Requirements

- Python 3

(No external libraries are required.)

## How to Run

1. Save the code in a Python file, e.g., `CoffeeMachine.py`.
2. Open your terminal or command prompt.
3. Navigate to the folder containing `CoffeeMachine.py`.
4. Run the script:

```bash
python CoffeeMachine.py
```

## Example Usage

```
What would you like? (latte/espresso/cappuccino): latte
Please insert coins
How many 5 coins? 4
How many 10 coins? 5
How many 20 coins? 2
Here is your change 30.
Here is your latte ☕. Enjoy!
Thank you for using the coffee machine!
```

## Project Structure

```
CoffeeMachine.py   # Main program file
README.md           # Project description and instructions
```

## Future Improvements

- Add more drink options.
- Handle invalid inputs more smoothly.
- Introduce different coin denominations.
- Add an admin login to refill resources.

---

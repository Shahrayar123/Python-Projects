import random
import time
import easygui

# Initialize the score and start time
score = 0
start_time = time.time()

# List of operators to be used in the problems
operators = ['+', '-', '/', '%', '*']

# Loop to generate 5 problems for the user
for i in range(1, 6):
    # Generate two random numbers for the math problem
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)

    # Randomly select an operator
    selected_operator = random.choice(operators)

    # Create the problem message for the user
    message = f"Problem {i} -> {first_number} {selected_operator} {second_number}"
    
    # Get the user's answer through an input dialog
    user_answer = easygui.enterbox(message, "Enter your answer:")

    # If the user cancels the dialog, exit the loop early
    if user_answer is None:
        easygui.msgbox("Game cancelled.", "Exit")
        break

    # Calculate the correct result based on the selected operator
    if selected_operator == '+':
        result = first_number + second_number
    elif selected_operator == '-':
        result = first_number - second_number
    elif selected_operator == '/':
        # Avoid division by zero, if second_number is zero, skip this iteration
        if second_number == 0:
            easygui.msgbox("Skipping division by zero problem.", "Warning")
            continue
        result = round(first_number / second_number, 1)
    elif selected_operator == '%':
        # Avoid modulo by zero, if second_number is zero, skip this iteration
        if second_number == 0:
            easygui.msgbox("Skipping modulo by zero problem.", "Warning")
            continue
        result = first_number % second_number
    elif selected_operator == '*':
        result = first_number * second_number

    # Check if the user's answer matches the correct result
    try:
        # Use float comparison for cases with division results
        if float(user_answer) == result:
            score += 1
        else:
            easygui.msgbox(f"Wrong answer! The correct answer is {result}.", "Incorrect")
    except ValueError:
        # If the user's input isn't a number, notify the user
        easygui.msgbox("Invalid input! Please enter a numeric answer.", "Error")

# Calculate the total time taken to complete the problems
end_time = time.time()
final_time = round(end_time - start_time, 2)

# Display the final score and time taken to the user
result_message = f"You scored {score} points in {final_time} seconds."
easygui.msgbox(result_message, "Result")

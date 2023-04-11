import random
import winsound

# Create a list of riddles
riddles = [
    {"question": "What starts with an 'E', ends with an 'E', but only contains one letter?",
        "answer": "envelope"},
    {"question": "What has a heart that doesn't beat?", "answer": "artichoke"},
    {"question": "What is always in front of you but can't be seen?", "answer": "future"},
    {"question": "What is so fragile that saying its name breaks it?", "answer": "silence"},
    {"question": "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?", "answer": "pencil lead"},
    {"question": "What goes up but never comes down?", "answer": "age"},
    {"question": "What has a neck but no head?", "answer": "bottle"},
    {"question": "What begins with T, ends with T, and has T in it?", "answer": "teapot"},
    {"question": "What has a thumb and four fingers, but is not alive?", "answer": "glove"},
    {"question": "I am an odd number. Take away a letter and I become even. What number am I?", "answer": "seven"},
    {"question": "What is full of holes but still holds water?", "answer": "sponge"},
    {"question": "What has four legs in the morning, two legs in the afternoon, and three legs in the evening?", "answer": "human"},
    {"question": "What goes through cities and fields, but never moves?", "answer": "road"},
    {"question": "What has a head and a tail, but no body?", "answer": "coin"},
]

# Create variables to keep track of the user's score and the total number of riddles
score = 0
total_riddles = len(riddles)

# Create a function to generate a random riddle


def generate_riddle():
    riddle = random.choice(riddles)
    return riddle


# Print a welcome message
print("Welcome to the Riddle Generator! Can you solve this riddle?\n")

# Start the game loop
while True:
    # Generate a random riddle and prompt the user for an answer
    riddle = generate_riddle()
    print(riddle["question"])
    user_answer = input("Enter your answer (or type 'quit' to exit): ").lower()

    # Check if the user wants to quit
    if user_answer == "quit" or user_answer == "q":
        print("Thanks for playing!")
        break

    # Check if the user's answer is correct
    if user_answer == riddle["answer"]:
        print("Congratulations, you got it right!")
        score += 1
        winsound.PlaySound("correct.wav", winsound.SND_FILENAME)
    else:
        print(
            f"Sorry, the correct answer is {riddle['answer']}. Better luck next time!")
        winsound.PlaySound("wrong.wav", winsound.SND_FILENAME)

    # Print the user's score
    print(f"\nYour current score is: {score}/{total_riddles}\n")

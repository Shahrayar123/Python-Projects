import random

# Riddle game

riddles = {
    "I have cities but no houses, forests but no trees, and water but no fish. What am I?": "A map",
    "I am always hungry, I must always be fed. The finger I touch, will soon turn red. What am I?": "Fire",
    "I am not alive, but I grow. I don't have lungs, but I need air. I don't have a mouth, but water kills me. What am I?": "Fire",
    "What has a heart that doesn't beat?": "Artichoke",
    "What is so fragile that saying its name breaks it?": "Silence",
    "What has keys but can't open locks?": "A piano"
}

riddle_keys = list(riddles.keys())  # Convert the dictionary keys into a list.

random.shuffle(riddle_keys)  # Shuffle the list of riddle keys.

score = 0  # Create a variable to keep track of user score

# Loop through each riddle, get user answer
for riddle_key in riddle_keys:
    print(riddle_key)
    user_answer = input("Answer: ").lower()
    
    # If answer is correct, Print Correct! and increment their score
    if user_answer == riddles[riddle_key].lower():
        print("Correct!")
        score += 1
    
    # Else, let them know they have wrong answer, tell them the correct one
    else:
        print("Wrong answer. Correct answer: " + riddles[riddle_key])

print("Game over! Your score is: " + str(score))  # When all riddles have been said, let user know their score and that the game is over.

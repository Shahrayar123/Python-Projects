import random

# Riddle game

riddles = {
    "I have cities but no houses, forests but no trees, and water but no fish. What am I?": "A map",
    "I am always hungry, I must always be fed. The finger I touch, will soon turn red. What am I?": "Fire",
    "I am not alive, but I grow. I don't have lungs, but I need air. I don't have a mouth, but water kills me. What am I?": "Fire",
    "What has a heart that doesn't beat?": "Artichoke",
    "What is so fragile that saying its name breaks it?": "Silence"
}

riddle_keys = list(riddles.keys())  # Convert the dictionary keys into a list.

random.shuffle(riddle_keys)  # Shuffle the list of riddle keys.

score = 0

for riddle_key in riddle_keys:
    print(riddle_key)
    user_answer = input("Answer: ").lower()
    if user_answer == riddles[riddle_key].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong.")
        again = input("Try again? Y/N ")
        if again.lower() == "y": 
            continue
        elif again.lower() == "n":
            print("Quitter!! Correct answer was: " + riddles[riddle_key])

print("Game over! Your score is: " + str(score))

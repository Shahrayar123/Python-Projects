import random

def choose_adventure():
  print("You find yourself at the edge of a mysterious forest. Which path will you take?")
  print("1. The winding path to the left")
  print("2. The straight path through the trees")
  choice = input("Enter your choice (1 or 2): ")

  if choice == "1":
    encounter_monster()
  elif choice == "2":
    find_treasure()
  else:
    print("Invalid choice. Please try again.")

def encounter_monster():
  print("A fearsome dragon blocks your path!")
  print("Do you fight or flee?")
  choice = input("Enter your choice (fight or flee): ")

  if choice == "fight":
    if random.randint(1, 2) == 1:
      print("You bravely defeat the dragon and claim its treasure!")
    else:
      print("The dragon overpowers you. Game over.")
  elif choice == "flee":
    print("You manage to escape, but lose your backpack.")
  else:
    print("Invalid choice. Please try again.")

def find_treasure():
  print("You discover a hidden treasure chest filled with gold and jewels!")
  print("You've won the game!")

if __name__ == "__main__":
  choose_adventure()
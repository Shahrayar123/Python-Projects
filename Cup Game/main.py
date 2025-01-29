import random
import time

def shuffle_cups(shuffle_max: int = 100) -> list[int]:
    cups = [0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
    for i in range(shuffle_max):
        cup = cups[0]
        cups.remove(cups[0])
        cups.insert(random.randint(0, 8), cup)

    return cups

money = 500

if __name__ == "__main__":
    while True:
        print(f"You Have {money} Balance")
        print("Enter How Much you wish to Wage (Enter 0 if you wish to quit)")
        wager = int(input(": "))
        cups = shuffle_cups()
        if wager == 0: break
        elif wager <= money:
            print("Wager accepted!")
            money -= wager

            c = int(input("Please enter a number from 1 to 10: ")) - 1
            print(f"You win {cups[c] * wager} !!!")
            money += wager * cups[c]
            print(f"You now have a balance of {money}")
            input()

        else:
            print("That Is not a valid amount Please Try Again")
            input()

import time
import numpy as np
import sys


# Delay printing
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


# Type advantage matrix
TYPE_ADVANTAGE = {
    "Fire": {"weak": ["Water"], "strong": ["Grass"]},
    "Water": {"weak": ["Grass"], "strong": ["Fire"]},
    "Grass": {"weak": ["Fire"], "strong": ["Water"]},
}


class Pokemon:
    def __init__(self, name, ptype, moves, EVs, level=1, health="==================="):
        self.name = name
        self.ptype = ptype
        self.moves = moves
        self.attack = EVs["ATTACK"]
        self.defense = EVs["DEFENSE"]
        self.level = level
        self.health = health
        self.bars = 20  # Amount of health bars
        self.experience = 0

    def type_advantage(self, opponent_type):
        if opponent_type in TYPE_ADVANTAGE[self.ptype]["strong"]:
            return 2, "\nIt's super effective!"
        elif opponent_type in TYPE_ADVANTAGE[self.ptype]["weak"]:
            return 0.5, "\nIt's not very effective..."
        else:
            return 1, "\nIt's not very effective..."

    def fight(self, opponent):
        # Print fight information
        print("-----POKEMON BATTLE-----")
        print(f"\n{self.name} (LVL {self.level})")
        print("TYPE/", self.ptype)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3 * (1 + np.mean([self.attack, self.defense])))
        print("\nVS")
        print(f"\n{opponent.name} (LVL {opponent.level})")
        print("TYPE/", opponent.ptype)
        print("ATTACK/", opponent.attack)
        print("DEFENSE/", opponent.defense)
        print("LVL/", 3 * (1 + np.mean([opponent.attack, opponent.defense])))

        time.sleep(2)

        # Type advantage
        attack_multiplier, string_1_attack = self.type_advantage(opponent.ptype)
        defense_multiplier, string_2_attack = opponent.type_advantage(self.ptype)
        self.attack *= attack_multiplier
        self.defense /= defense_multiplier
        opponent.attack *= defense_multiplier
        opponent.defense /= attack_multiplier

        # Fight loop
        while self.bars > 0 and opponent.bars > 0:
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{opponent.name}\t\tHLTH\t{opponent.health}\n")

            print(f"Go {self.name}!")
            for i, move in enumerate(self.moves):
                print(f"{i+1}. {move}")
            index = int(input("Pick a move: "))
            if 1 <= index <= len(self.moves):
                delay_print(f"\n{self.name} used {self.moves[index-1]}!")
                time.sleep(1)
                delay_print(string_1_attack)
            else:
                print("\nInvalid move. Try again.")
                continue

            # Determine damage
            opponent.bars -= self.attack
            opponent.health = "=" * max(int(opponent.bars + 0.1 * opponent.defense), 0)

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{opponent.name}\t\tHLTH\t{opponent.health}\n")
            time.sleep(0.5)

            if opponent.bars <= 0:
                delay_print("\n..." + opponent.name + " fainted.")
                break

            # Opponent's turn
            print(f"Go {opponent.name}!")
            for i, move in enumerate(opponent.moves):
                print(f"{i+1}. {move}")
            index = np.random.randint(
                1, len(opponent.moves) + 1
            )  # Random move for the opponent
            delay_print(f"\n{opponent.name} used {opponent.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine damage
            self.bars -= opponent.attack
            self.health = "=" * max(int(self.bars + 0.1 * self.defense), 0)

            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{opponent.name}\t\tHLTH\t{opponent.health}\n")
            time.sleep(0.5)

            if self.bars <= 0:
                delay_print("\n..." + self.name + " fainted.")
                break

        money = np.random.choice(5000)
        delay_print(f"\nOpponent paid you ${money}.\n")
        self.gain_experience(100)

    def gain_experience(self, exp):
        self.experience += exp
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.attack += 1
        self.defense += 1
        self.bars += 5
        self.health = "=" * self.bars
        self.experience = 0
        print(f"\n{self.name} leveled up to level {self.level}!")


if __name__ == "__main__":
    # Create Pokemon
    Charizard = Pokemon(
        "Charizard",
        "Fire",
        ["Flamethrower", "Fly", "Blast Burn", "Fire Punch"],
        {"ATTACK": 12, "DEFENSE": 8},
    )
    Blastoise = Pokemon(
        "Blastoise",
        "Water",
        ["Water Gun", "Bubblebeam", "Hydro Pump", "Surf"],
        {"ATTACK": 10, "DEFENSE": 10},
    )
    Venusaur = Pokemon(
        "Venusaur",
        "Grass",
        ["Vine Whip", "Razor Leaf", "Earthquake", "Frenzy Plant"],
        {"ATTACK": 8, "DEFENSE": 12},
    )

    Charmander = Pokemon(
        "Charmander",
        "Fire",
        ["Ember", "Scratch", "Tackle", "Fire Punch"],
        {"ATTACK": 4, "DEFENSE": 2},
    )
    Squirtle = Pokemon(
        "Squirtle",
        "Water",
        ["Bubblebeam", "Tackle", "Headbutt", "Surf"],
        {"ATTACK": 3, "DEFENSE": 3},
    )
    Bulbasaur = Pokemon(
        "Bulbasaur",
        "Grass",
        ["Vine Whip", "Razor Leaf", "Tackle", "Leech Seed"],
        {"ATTACK": 2, "DEFENSE": 4},
    )

    Charmeleon = Pokemon(
        "Charmeleon",
        "Fire",
        ["Ember", "Scratch", "Flamethrower", "Fire Punch"],
        {"ATTACK": 6, "DEFENSE": 5},
    )
    Wartortle = Pokemon(
        "Wartortle",
        "Water",
        ["Bubblebeam", "Water Gun", "Headbutt", "Surf"],
        {"ATTACK": 5, "DEFENSE": 5},
    )
    Ivysaur = Pokemon(
        "Ivysaur",
        "Grass",
        ["Vine Whip", "Razor Leaf", "Bullet Seed", "Leech Seed"],
        {"ATTACK": 4, "DEFENSE": 6},
    )

    Charizard.fight(Squirtle)  # Get them to fight

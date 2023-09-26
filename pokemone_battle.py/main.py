import time
import numpy as np
import sys

# Delay printing
def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


def pokemon_fight(Pokemon1, Pokemon2):
    """
    Allow two pokemons to fight each other
    :param Pokemon1: a pokemon object
    :param Pokemon2: a pokemon object
    :return: 1 if Pokemon1 wins, 2 if Pokemon2 wins
    Example:
    >>> pokemon_fight(Charizard, Charmander)
    1
    Charizard wins
    """

    # Print fight information
    print("-----POKEMON BATTLE-----")
    print(f"\n{Pokemon1.name}")
    print("TYPE/", Pokemon1.types)
    print("ATTACK/", Pokemon1.attack)
    print("DEFENSE/", Pokemon1.defense)
    print("LVL/", 3 * (1 + np.mean([Pokemon1.attack, Pokemon1.defense])))
    print("\nVS")
    print(f"\n{Pokemon2.name}")
    print("TYPE/", Pokemon2.types)
    print("ATTACK/", Pokemon2.attack)
    print("DEFENSE/", Pokemon2.defense)
    print("LVL/", 3 * (Pokemon2.level))

    time.sleep(2)

    # Consider type advantages
    version = ['Fire', 'Water', 'Grass']
    for i, k in enumerate(version):
        if Pokemon1.types == k:
            # Both are same type
            if Pokemon2.types == k:
                string_1_attack = '\nIts not very effective...'
                string_2_attack = '\nIts not very effective...'

            # Pokemon2 is STRONG
            if Pokemon2.types == version[(i + 1) % 3]:
                Pokemon2.attack *= 2
                Pokemon2.defense *= 2
                Pokemon1.attack /= 2
                Pokemon1.defense /= 2
                string_1_attack = '\nIts not very effective...'
                string_2_attack = '\nIts super effective!'

            # Pokemon2 is WEAK
            if Pokemon2.types == version[(i + 2) % 3]:
                Pokemon1.attack *= 2
                Pokemon1.defense *= 2
                Pokemon2.attack /= 2
                Pokemon2.defense /= 2
                string_1_attack = '\nIts super effective!'
                string_2_attack = '\nIts not very effective...'

    turn = 1    # semaphore to check which pokemon's turn it is
    # Now for the actual fighting...
    # Continue while pokemon still have health
    while (Pokemon1.bars > 0) and (Pokemon2.bars > 0):
        # Print the health of each pokemon
        print(f"\n{Pokemon1.name}\t\tHLTH\t{Pokemon1.health}")
        print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

        if turn == 1:
            print(f"Go {Pokemon1.name}!")
            for i, x in enumerate(Pokemon1.moves):
                print(f"{i + 1}.", x)
            # print(f"{i+2}.", )
            index = int(input('Pick a move: '))
            if (index > len(Pokemon1.moves)):
                continue
            delay_print(f"\n{Pokemon1.name} used {Pokemon1.moves[index - 1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Determine damage
            Pokemon2.bars -= Pokemon1.attack
            Pokemon2.health = ""

            # Add back bars plus defense boost
            for j in range(int(Pokemon2.bars + .1 * Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f"\n{Pokemon1.name}\t\tHLTH\t{Pokemon1.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' fainted.\n')
                return 1

            turn = 2

        # Pokemon2s turn

        if turn == 2:
            print(f"\nGo {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i + 1}.", x)
            index = int(input('Pick a move: '))
            if (index > len(Pokemon2.moves)):
                continue
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index - 1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine damage
            Pokemon1.bars -= Pokemon2.attack
            Pokemon1.health = ""

            # Add back bars plus defense boost
            for j in range(int(Pokemon1.bars + .1 * Pokemon1.defense)):
                Pokemon1.health += "="

            time.sleep(1)
            print(f"\n{Pokemon1.name}\t\tHLTH\t{Pokemon1.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if Pokemon1.bars <= 0:
                delay_print("\n..." + Pokemon1.name + ' fainted.\n')
                return 2

            turn = 1


# Function to simulate a battle between two trainers
def trainer_battle(trainer1, trainer2):
    """
    Allows 2 pokemon trainers to fight each other in rounds.
    Both trainers must have the same amount of pokemons.
    :param trainer1: a trainer object
    :param trainer2: another trainer object
    :return: nothing
    Example:
    >>> trainer_battle(trainer1, trainer2)
    """
    delay_print(f"Trainer {trainer1.name} challenges Trainer {trainer2.name}!")

    # counters for each trainer's round wins
    trainer1Wins = 0
    trainer2Wins = 0

    for i in range(len(trainer1.pokemon_list)):
        delay_print(f"\nRound {i + 1}:")
        delay_print(f"{trainer1.name}'s {trainer1.pokemon_list[i].name} vs {trainer2.name}'s {trainer2.pokemon_list[i].name}\n")
        winner = pokemon_fight(trainer1.pokemon_list[i], trainer2.pokemon_list[i])
        if winner == 1:
            trainer1Wins += 1
        else:
            trainer2Wins += 1

    if trainer1Wins == trainer2Wins:
        delay_print(f"It's a draw!")

    money = np.random.choice(5000)  # calculate money for the winner

    if trainer1Wins > trainer2Wins:
        delay_print(f"\n{trainer2.name} paid {trainer1.name} ${money}.\n")
    elif trainer2Wins > trainer1Wins:
        delay_print(f"\n{trainer1.name} paid {trainer2.name} ${money}.\n")

    pass


class Trainer:
    """
    Trainer class that represents a pokemon trainer.
    Each trainer has an ID, a name and list of pokemons.
    """
    def __init__(self, trainer_id, name, pokemon_list):
        self.trainer_id = trainer_id
        self.name = name
        self.pokemon_list = pokemon_list

    def display_info(self):
        print(f"Trainer ID: {self.trainer_id}")
        print(f"Name: {self.name}")
        print("Pokémon:")
        for pokemon in self.pokemon_list:
            print(f"- {pokemon.name} (Level {pokemon.level})")


class Pokemon:
    """
    Pokemon class to represent a pokemon.
    Each pokemon has a name, type, a list of moves and a list of stats (attack and defense) and a health string.
    """
    def __init__(self, name, types, moves, EVs, health='==================='):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20  # Amount of health bars
        self.level = 1 + np.mean([self.attack, self.defense]) # calculation of level


if __name__ == '__main__':
    # Create Pokemon
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'],
                        {'ATTACK': 12, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],
                        {'ATTACK': 10, 'DEFENSE': 10})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],
                       {'ATTACK': 8, 'DEFENSE': 12})

    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],
                         {'ATTACK': 4, 'DEFENSE': 2})
    Squirtle = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'], {'ATTACK': 3, 'DEFENSE': 3})
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],
                        {'ATTACK': 2, 'DEFENSE': 4})

    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],
                         {'ATTACK': 6, 'DEFENSE': 5})
    Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],
                        {'ATTACK': 5, 'DEFENSE': 5})
    Ivysaur = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],
                      {'ATTACK': 4, 'DEFENSE': 6})

    # Create Trainers
    trainer1 = Trainer(0, "ash", [Bulbasaur, Charmander, Squirtle])
    trainer2 = Trainer(1, "gary", [Venusaur, Charizard, Blastoise])

    # Battle!
    trainer_battle(trainer1, trainer2)

import random
import time

# Game initialization
characters = ["Jack", "Lenzi", "Kim", "Sarah"]
powers = ["Super Strength", "Super Intelligence", "Super Speed", "None"]
health = [1, 1, 1, 1]
inventory = [[], [], [], []]  # one list per character

creatures = [
    {
        "name": "Fanglore",
        "description": "A mutated wolf-like creature with razor-sharp teeth and poisonous claws.",
        "attacks": ["Claw Slash", "Venomous Bite", "Speed Dash"],
        "weakness": "Super Strength"
    },
    {
        "name": "Stazer",
        "description": "A ghostly creature that causes fear and confusion with illusions.",
        "attacks": ["Illusion Creation", "Confuse", "Scare"],
        "weakness": "Super Intelligence"
    },
    {
        "name": "Rooterous",
        "description": "A massive plant creature that restrains prey with fast-growing roots.",
        "attacks": ["Root Grasp", "Thorn Barrage", "Earthquake"],
        "weakness": "Super Speed"
    }
]

# Start game logic
def start_game_logic():
    print("Quest: Find the remote to signal flares in the sky!")
    remote = "Remote for the Flares"
    inventory[0].append(remote)  # Assuming the first character picked (index 0)
    print(f"Character {characters[0]} found the {remote}!\n")

# Fight function
def fight():
    creature = random.choice(creatures)
    print(f"A wild {creature['name']} appears!")
    print(creature["description"])
    
    attack = random.choice(creature["attacks"])
    print(f"{creature['name']} uses {attack}!\n")
    
    # Simple mock fight result
    player_win = random.choice([True, False])
    if player_win:
        return f"You defeated {creature['name']}!"
    else:
        return f"{creature['name']} defeated you. Game Over."

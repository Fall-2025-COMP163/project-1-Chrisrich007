"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Christopher Arnold
Date: 10/28/2025

AI Usage:
Assistance from ChatGPT (GPT-5) used for structuring function logic 
and creating balanced stat formulas for each character class.
All logic is fully reviewed and understood by me.
"""

import os

VALID_CLASSES = ["Warrior", "Mage", "Rogue", "Cleric"]

def calculate_stats(character_class, level):
    """Calculates base stats based on class and level. Returns (strength, magic, health)."""
    if character_class.lower() == "warrior":
        return (12 + 3*level, 4 + 1*level, 120 + 10*level)
    elif character_class.lower() == "mage":
        return (5 + 1*level, 15 + 4*level, 80 + 7*level)
    elif character_class.lower() == "rogue":
        return (8 + 2*level, 8 + 2*level, 90 + 5*level)
    elif character_class.lower() == "cleric":
        return (7 + 2*level, 13 + 3*level, 110 + 8*level)
    else:
        return (5, 5, 100)

def create_character(name, character_class):
    """Creates a character dictionary with calculated stats."""
    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    return {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100
    }

def save_character(character, filename):
    """Saves character to a file if writable. Returns True on success, False on failure."""
    folder = os.path.dirname(filename) or "."
    if not os.access(folder, os.W_OK):
        print(f"Error: Cannot write to '{filename}'. Permission denied.")
        return False

    file = open(filename, "w")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()
    return True

def load_character(filename):
    """Loads character if file exists. Returns dictionary or None if file not found."""
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return None

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    character = {}
    for line in lines:
        if ":" in line:
            key, value = line.strip().split(": ", 1)
            key = key.lower().replace("character name", "name")
            if key in ["name", "class"]:
                character[key] = value
            else:
                character[key] = int(value)
    return character

def display_character(character):
    """Prints a formatted character sheet."""
    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("=======================")

def level_up(character):
    """Increases level and recalculates stats."""
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    character["gold"] += 50

# ------------------ Main Program ------------------
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    name = input("Enter your hero's name: ")

    # Validate character class input
    while True:
        char_class = input("Choose a class (Warrior, Mage, Rogue, Cleric): ")
        if char_class.capitalize() in VALID_CLASSES:
            char_class = char_class.capitalize()
            break
        else:
            print("Invalid class. Please choose Warrior, Mage, Rogue, or Cleric.")

    hero = create_character(name, char_class)
    display_character(hero)

    filename = "hero.txt"
    if save_character(hero, filename):
        print(f"\nCharacter saved to {filename}")
    else:
        print("Failed to save character.")

    print("\nLoading character...")
    loaded_hero = load_character(filename)
    if loaded_hero:
        display_character(loaded_hero)
    else:
        print("Failed to load character.")

    print("\nLeveling up character...")
    if loaded_hero:
        level_up(loaded_hero)
        display_character(loaded_hero)


#Note:
#python -m pytest tests/test_character_creation.py -v
#python -m pytest tests/test_comprehensive.py -v
#python -m pytest tests/test_file_operations.py -v

"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Christopher Arnold
Date: 10/28/2025

AI Usage:
Assistance from ChatGPT (GPT-5) used for structuring function logic 
and creating balanced stat formulas for each character class.
All logic is fully reviewed and understood by me.
"""

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level.
    Returns: tuple (strength, magic, health)

    Class Stat Profiles:
    - Warrior: High strength, low magic, high health
    - Mage: Low strength, high magic, medium health  
    - Rogue: Medium strength, medium magic, low health
    - Cleric: Medium strength, high magic, high health
    """
    if character_class.lower() == "warrior":
        strength = 12 + (3 * level)
        magic = 4 + (1 * level)
        health = 120 + (10 * level)
    elif character_class.lower() == "mage":
        strength = 5 + (1 * level)
        magic = 15 + (4 * level)
        health = 80 + (7 * level)
    elif character_class.lower() == "rogue":
        strength = 8 + (2 * level)
        magic = 8 + (2 * level)
        health = 90 + (5 * level)
    elif character_class.lower() == "cleric":
        strength = 7 + (2 * level)
        magic = 13 + (3 * level)
        health = 110 + (8 * level)
    else:
        strength = 5
        magic = 5
        health = 100

    return (strength, magic, health)


def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats.
    Returns a dictionary with keys:
    name, class, level, strength, magic, health, gold
    """
    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100
    }
    return character


def save_character(character, filename):
    """
    Saves character to text file in the required format.
    Returns True when writing completes successfully.
    """
    with open(filename, "w") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
    return True
def load_character(filename):
    """
    Loads character from a text file.
    Returns a character dictionary.
    (Assumes the file exists and is formatted correctly.)
    """
    with open(filename, "r") as file:
        lines = file.readlines()

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
    """
    Prints a formatted character sheet.
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("=======================")


def level_up(character):
    """
    Increases the character's level and recalculates stats.
    Updates the dictionary directly.
    """
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    character["gold"] += 50


# Optional testing section
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    name = input("Enter your hero's name: ")
    char_class = input("Choose a class (Warrior, Mage, Rogue, Cleric): ")

    hero = create_character(name, char_class)
    display_character(hero)

    filename = "hero.txt"
    save_character(hero, filename)
    print(f"\nCharacter saved to {filename}")

    print("\nLoading character...")
    loaded_hero = load_character(filename)
    display_character(loaded_hero)

    print("\nLeveling up character...")
    level_up(loaded_hero)
    display_character(loaded_hero)
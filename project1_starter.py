"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Christopher Arnold
Date: 10/28/2025

AI Usage:
Assistance from ChatGPT (GPT-5) was used for:
- Structuring function logic for modularity (calculate_stats, create_character, save/load system)
- Designing balanced stat formulas per class
- Improving readability and commenting standards
All logic, formulas, and structure have been fully reviewed and understood by me.

--------------------------------------------
Program Summary:
This program is a simple RPG-style "Character Creator" that allows a user to:
1. Create a new character (choose a name and class)
2. Automatically generate stats (strength, magic, health) based on class and level
3. Save the character’s data to a file
4. Load that data back into memory
5. Level up the character, increasing stats and gold
It demonstrates file I/O operations, dictionaries, input validation, and modular function design.
6. Helped me with using the os function
--------------------------------------------
"""

import os  # Used for file and directory checking

# A list of valid character classes that the user can choose from
VALID_CLASSES = ["Warrior", "Mage", "Rogue", "Cleric"]

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level.
    Returns (strength, magic, health) tuple.
    """
    # Each class scales differently based on level to reflect RPG balance
    if character_class.lower() == "warrior":
        return (12 + 3*level, 4 + 1*level, 120 + 10*level)
    elif character_class.lower() == "mage":
        return (5 + 1*level, 15 + 4*level, 80 + 7*level)
    elif character_class.lower() == "rogue":
        return (8 + 2*level, 8 + 2*level, 90 + 5*level)
    elif character_class.lower() == "cleric":
        return (7 + 2*level, 13 + 3*level, 110 + 8*level)
    else:
        # Default stats for unknown classes
        return (5, 5, 100)

def create_character(name, character_class):
    """
    Creates a character dictionary that stores all key stats and info.
    Starts at level 1 and uses calculate_stats() for initial values.
    """
    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    return {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100  # Starting amount of in-game currency
    }

def save_character(character, filename):
    """
    Saves the character’s data to a text file.
    Returns True if the file was written successfully, False otherwise.
    """
    folder = os.path.dirname(filename) or "."
    # Check for permission errors before writing
    if not os.access(folder, os.W_OK):
        print(f"Error: Cannot write to '{filename}'. Permission denied.")
        return False

    # Write each attribute as a line in the file
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
    """
    Loads a saved character file if it exists.
    Returns a character dictionary or None if file not found.
    """
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
            # Normalize keys to dictionary-friendly names
            key = key.lower().replace("character name", "name")
            if key in ["name", "class"]:
                character[key] = value
            else:
                character[key] = int(value)
    return character

def display_character(character):
    """
    Prints a formatted character sheet.
    Helps visualize all the stored data clearly.
    """
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
    """
    Increases the character’s level and recalculates stats.
    Also rewards extra gold for leveling up.
    """
    character["le]()

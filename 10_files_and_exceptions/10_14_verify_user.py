#2
from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        userinfo = json.loads(contents)
        return userinfo
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    name = input("What is your name?\n")
    pet = input("What's your pet's name?\n")
    food = input("Favorite food?\n")
    userinfo = {
        'name': name,
        'pet': pet,
        'food': food
        }
    contents = json.dumps(userinfo)
    path.write_text(contents)
    return userinfo

def greet_user():
    """Greet the user by name."""
    path = Path('10_files_and_exceptions/userinfo.json')
    userinfo = get_stored_username(path)
    if userinfo:
        print(f"Welcome back, {userinfo['name']}.")
        print(f"Have you fed {userinfo['pet']} yet?")
        print(f"We know you're a big fan of {userinfo['food']}.")
        confirm = input("\nThis is you, correct? (y/n)\n")
        if confirm == 'n':
            userinfo = get_new_username(path)
            contents = json.dumps(userinfo)
            path.write_text(contents)
            print(f"\nWe'll remember your new information, {userinfo['name']}.")
        else:
            print("\nPleasure to see you again.")
    else:
        userinfo = get_new_username(path)
        contents = json.dumps(userinfo)
        path.write_text(contents)
        print(f"We'll remember everything you told us, {userinfo['name']}.")
greet_user()
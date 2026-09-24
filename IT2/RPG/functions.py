from classes import *

def show_stats(x):
    stats(x)

def attack(x):
    print(f"You attacked {x.name}!")

def avoid(x):
    print(f"You avoided {x.name}.")

def exit_game():
    print("Bye!")

def stats(obj):
  if isinstance(obj, Enemy):
    print(f"""
Name: {obj.name}
HP: {obj.hp}
Damage: {obj.dmg}
Sentience: {obj.sentience}
    """)

actions = {
  "1": ("Stats", show_stats),
  "2": ("Attack", attack),
  "3": ("Avoid", avoid),
  "4": ("Exit", exit_game)
}

def menu():
  for key, (description, action) in actions.items():
    print(f"{key}. {description}")

def handle_menu(choice, enemy):
    if choice in actions:
        actions[choice][1](enemy)
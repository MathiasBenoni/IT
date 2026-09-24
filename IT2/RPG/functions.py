from classes import *

def stats(obj):
  if isinstance(obj, Enemy):
    print(f"""
Name: {obj.name}
HP: {obj.hp}
Damage: {obj.dmg}
Sentience: {obj.sentience}
    """)

actions = {
  "1": "Stats",
  "2": "Attack",
  "3": "Avoid",
  "4": "Exit"
}

def menu():

  for key, action in actions.items():
    print(f"{key}. {action}")
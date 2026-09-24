from classes import *
from functions import *



name = input("What are you called? ")
player = Player(name, 100)

first_enemy = Enemy("Bob", 10, 0, True)

menu()
choice = input("What do you do (1 - 4)? ")

if choice == "1":
  stats(first_enemy)
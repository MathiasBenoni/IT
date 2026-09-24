from more_itertools import first


class Entity():
  def __init__(self, name: str):
    self.name = name

class Character(Entity):
  def __init__(self, name: str, hp: int):
    super().__init__(name)
    self.hp = hp

class Player(Character):
  def __init__(self, name: str, hp: int):
    super().__init__(name, hp)

class Enemy(Character):
  def __init__(self, name: str, hp: int, dmg: int, sentience: bool):
    super().__init__(name, hp)
    self.dmg = dmg
    self.sentience = sentience

def stats(obj):
  if isinstance(obj, Enemy):
    print()
    print(f"Name: {obj.name}")
    print(f"HP: {obj.hp}")
    print(f"Damage: {obj.dmg}")
    print(f"Sentience: {obj.sentience}")
    print()

name = input("What are you called? ")
player = Player(name, 100)

first_enemy = Enemy("Bob", 10, 0, True)

print(player.name)
print(player.hp)

print(f"You encounter {first_enemy.name}!")
print("=======================")
print("Actions:")
print()
print("1. See stats on the poor fella")
print("2. Kill the poor fella")
print("3. Take avoiding action and go around him")
print("4. Nothing")

choice = input("What do you do (1 - 4)? ")

if choice == "1":
  stats(first_enemy)


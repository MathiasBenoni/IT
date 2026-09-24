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
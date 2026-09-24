class entity():
  def __init__(self, name: str):
    self.name = name

class character(entity):
  def __init__(self, name: str, hp: int):
    super().__init__(name)
    self.hp = hp

class player(character):
  def __init__(self, name, hp):
    super().__init__(name, hp)
  

mathias = character("Mathias", 100)

print(mathias)

class Entety:
  def __init__(self, radius : int, hostile : bool):
    self.radius = radius
    self.hostile = hostile

  def was_attacked(self, damage):
    self.radius -= damage
    if self.radius <= 0:
      return False
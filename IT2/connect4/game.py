import pygame
import my_functions

CELL = 100
RADIUS = 10

class Game:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.board = my_functions.create_board(self.width, self.height)
    pass

  # def draw(self, screen, left, top, width, height, center_x, center_y):
  #   pygame.draw.rect(screen, "black", (left, top, width, height))
  #   pygame.draw.circle(screen, "yellow", (center_x, center_y), RADIUS)

game_1 = Game(7, 6)
print(game_1.height)
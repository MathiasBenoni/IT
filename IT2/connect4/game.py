from turtle import screensize

import pygame
import my_functions

CELL = 100
RADIUS = 40
PADDING = RADIUS / 2

BOARD_WIDTH = RADIUS * 2 * 7 + PADDING
BOARD_HEIGHT = RADIUS * 2 * 6 + PADDING

class Game:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.board = my_functions.create_board(self.width, self.height)

  def piece(self, screen, left, top, width, height, center_x, center_y):
    # pygame.draw.rect(screen, "black", (left, top, width, height))
    pygame.draw.circle(screen, "yellow", (center_x, center_y), RADIUS)

  def draw_board(self, screen, center_x, bottom_y):
    pygame.draw.rect(screen, "black", (center_x - BOARD_WIDTH / 2, bottom_y - BOARD_HEIGHT, BOARD_WIDTH, BOARD_HEIGHT))
    
    pass

game_1 = Game(7, 6)

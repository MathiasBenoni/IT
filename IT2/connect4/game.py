from turtle import screensize

import pygame
import my_functions

CELL = 100
RADIUS = 40
PADDING = RADIUS / 2

BOARD_WIDTH = RADIUS * 2 * 7 + PADDING * 4
BOARD_HEIGHT = RADIUS * 2 * 6 + PADDING * 4

class Game:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.board = my_functions.create_board(self.width, self.height)

  def piece(self, screen, left, top, width, height, center_x, center_y):
    # pygame.draw.rect(screen, "black", (left, top, width, height))
    pygame.draw.circle(screen, "yellow", (center_x, center_y), RADIUS)

  def draw_board(self, screen, center_x, bottom_y, background_color):
    left = center_x - BOARD_WIDTH / 2
    top = bottom_y - BOARD_HEIGHT
    pygame.draw.rect(screen, "black", (left, top, BOARD_WIDTH, BOARD_HEIGHT), 0, 10)

    # Split the board into equal cells and put one hole in the middle of each
    cell_width = BOARD_WIDTH / self.width
    cell_height = BOARD_HEIGHT / self.height
    for row in range(self.height):
      for col in range(self.width):
        hole_x = left + cell_width * col + cell_width / 2
        hole_y = top + cell_height * row + cell_height / 2
        pygame.draw.circle(screen, background_color, (hole_x, hole_y), RADIUS)

game_1 = Game(7, 6)

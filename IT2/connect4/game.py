from turtle import screensize

import pygame
import my_functions

CELL = 100
RADIUS = 40
PADDING = RADIUS / 2

BOARD_WIDTH = RADIUS * 2 * 7 + PADDING * 4
BOARD_HEIGHT = RADIUS * 2 * 6 + PADDING * 4

player_piece = {
  0: "X",
  1: "O"
}
colors = {
  0: "\x1b[31m",
  1: "\x1b[34m",
  "White": "\x1b[37m",
}
backgrounds = {
  0: "\x1b[41m",
  1: "\x1b[44m",
  "No": "\x1b[49m"
}

class Game:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.board = my_functions.create_board(self.width, self.height)

  def piece(self, screen, center_x, center_y, color):
    # pygame.draw.rect(screen, "black", (left, top, width, height))
    pygame.draw.circle(screen, color, (center_x, center_y), RADIUS)

  def draw_board(self, screen, center_x, bottom_y, background_color):
    self.left = center_x - BOARD_WIDTH / 2
    left = self.left
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

  def graphical_place_piece(self, screen, x):
    # print("X: ", x)
    cell_width = BOARD_WIDTH / self.width
    col = int((x - self.left) // cell_width)
    print(col)
    my_functions.place_piece(col + 1, self.board, player_piece, 0)
    my_functions.print_board(7, 6, self.board, player_piece, colors, backgrounds)
    pass

game_1 = Game(7, 6)
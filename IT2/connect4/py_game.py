import pygame
import game
import my_functions

SCREEN_WIDHT = 1280
SCREEN_HEIGHT = 720

BACKGROUND_COLOR = "purple"

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))

clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      raise SystemExit

  pos = pygame.mouse.get_pos()
  
  screen.fill(BACKGROUND_COLOR)

  # game.game_1.piece(screen, pos[0], pos[1], 10, 10, 10, 10)
  game.game_1.piece(screen, 0, 0, 10, 10, pos[0], game.RADIUS)
  game.game_1.draw_board(screen, SCREEN_WIDHT / 2, SCREEN_HEIGHT, BACKGROUND_COLOR)

  pygame.display.flip()
  clock.tick(60)
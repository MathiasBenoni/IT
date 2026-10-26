import pygame
import game
import my_functions

SCREEN_WIDHT = 1280
SCREEN_HEIGHT = 720

BACKGROUND_COLOR = "purple"

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))

clock = pygame.time.Clock()

COOLDOWN = 300

last_click = -COOLDOWN
waiting = False

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      raise SystemExit

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      now = pygame.time.get_ticks()
      if now - last_click >= COOLDOWN:
        last_click = now
        waiting = True
        print("NOW")
        game.game_1.graphical_place_piece(screen, pos[0])
        #print(pygame.mouse.get_pos())

  if waiting and pygame.time.get_ticks() - last_click >= COOLDOWN:
    waiting = False
    print("Wait = False")
  pos = pygame.mouse.get_pos()
  
  screen.fill(BACKGROUND_COLOR)

  # game.game_1.piece(screen, pos[0], pos[1], 10, 10, 10, 10)
  game.game_1.piece(screen, pos[0], game.RADIUS, "yellow")

  game.game_1.draw_board(screen, SCREEN_WIDHT / 2, SCREEN_HEIGHT, BACKGROUND_COLOR)

  pygame.display.flip()
  clock.tick(60)
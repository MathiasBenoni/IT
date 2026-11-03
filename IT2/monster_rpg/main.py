import pygame
from classes import *

HEIGHT = 720
WIDTH = 1280

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Awesome game")

running = True

player = Entety(10, False)

enemy = Entety(10, True)



while running:
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      running = False

  screen.fill("purple")

  




  pygame.display.flip()

  clock.tick(60)

pygame.quit()
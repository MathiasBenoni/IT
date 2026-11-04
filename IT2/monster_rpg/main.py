import pygame
from classes import *

HEIGHT = 720
WIDTH = 1280

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.init()
pygame.font.init()

pygame.display.set_caption("Awesome game")

running = True



player = Entety(10, False)
enemy = Entety(10, True)

button_1 = Button(300, 200, 'gray', (200, 300), 'test')


while running:
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      running = False

  button_1.update()

  screen.fill("purple")

  button_1.draw_button(screen)

  pygame.display.flip()

  clock.tick(60)

pygame.quit()
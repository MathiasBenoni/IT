import pygame
from classes import *
import functions as my_funcs
HEIGHT = 720
WIDTH = 1280

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.init()
pygame.font.init()

pygame.display.set_caption("Awesome game")

running = True

enteties = [
  Entety(10, False, 'blue', (100, 100)),
  Entety(10, True, 'black', (10, 100)), 
  Entety(20, True, 'cyan', (50, 100))
]

player = enteties[0]

button_width = 150
button_height = 40
padding = 10


buttons = [
    Button(button_width, button_height, 'gray', 'yellow', (WIDTH // 2, HEIGHT // 2 - button_height - padding), 'Start', my_funcs.start_game),
    Button(button_width, button_height, 'gray', 'blue', (WIDTH // 2, HEIGHT // 2), 'Attack'),
    Button(button_width, button_height, 'gray', 'green', (WIDTH // 2, HEIGHT // 2 + button_height + padding), 'Quit', my_funcs.quit_game)
  ]

while running:
  events = pygame.event.get()
  for event in events:

    if event.type == pygame.QUIT:
      running = False
    

  # LOGIC

  for button in buttons:
      button.update(events)
  


  # VISUAL

  screen.fill("white")

  for button in buttons:
      button.draw_self(screen)

  for entety in enteties:
     entety.draw_self(screen)

  pygame.display.flip()

  clock.tick(60)

pygame.quit()
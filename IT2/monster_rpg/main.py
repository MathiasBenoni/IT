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


global_y_pos = HEIGHT // 2
enemy_x_pos = WIDTH // 2 + 50
enteties = [
  Entety(10, False, 'blue', (100, global_y_pos)), # Player
  Entety(10, True, 'black', (enemy_x_pos, global_y_pos)), 
  Entety(20, True, 'cyan', (enemy_x_pos + 50, global_y_pos))
]

player = enteties[0]

button_width = 150
button_height = 40
padding = 10


buttons = [
    Button(button_width, button_height, 'gray', 'yellow', (WIDTH // 3, HEIGHT // 2 - button_height - padding), 'Start', my_funcs.start_game),
    Button(button_width, button_height, 'gray', 'blue', (WIDTH // 3, HEIGHT // 2), 'Attack', lambda: my_funcs.attack(enteties[1])),
    Button(button_width, button_height, 'gray', 'green', (WIDTH // 3, HEIGHT // 2 + button_height + padding), 'Quit', my_funcs.quit_game)
  ]

while running:
  events = pygame.event.get()
  for event in events:

    if event.type == pygame.QUIT:
      running = False
    

  # LOGIC

  for button in buttons:
      button.update(events)

  for entety in enteties[:]:
     if entety.radius <= 0:
        enteties.remove(entety)


  # VISUAL

  screen.fill("white")

  for button in buttons:
      button.draw_self(screen)

  for entety in enteties:
     entety.draw_self(screen)

  pygame.display.flip()

  clock.tick(60)

pygame.quit()
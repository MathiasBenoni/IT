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


button_width = 150
button_height = 40
padding = 10

global_y_pos = HEIGHT // 2
enemy_x_pos = WIDTH // 2 + 150

enteties = [
  Entety(100, False, 'blue', (WIDTH // 6 - button_width // 4, global_y_pos)), # Player
  Entety(200, True, 'black', (enemy_x_pos, global_y_pos)), 
  Entety(50, True, 'cyan', (enemy_x_pos + 200 + 50 + padding, global_y_pos))
]

player = enteties[0]

### DAMAGE VARS

tentacles = 5
lightning = 2


buttons = [
    Button(button_width, button_height, 'gray', 'yellow', (WIDTH // 3, HEIGHT // 2 - button_height - padding), 'Stab', my_funcs.attack(enteties[1], 10)),
    Button(button_width, button_height, 'gray', 'yellow', (WIDTH // 3, HEIGHT // 2), 'Tentacles', lambda: my_funcs.attack_all(enteties[1:len(enteties)], tentacles)),
    Button(button_width, button_height, 'gray', 'yellow', (WIDTH // 3, HEIGHT // 2 + button_height + padding), 'Lightning', lambda: my_funcs.attack_all(enteties[1:len(enteties)], lightning)),
    Button(button_width, button_height, 'gray', 'green', (WIDTH // 3, HEIGHT // 2 + button_height * 2 + padding * 2), 'Quit', my_funcs.quit_game)
  ]

while running:
  events = pygame.event.get()
  for event in events:

    if event.type == pygame.QUIT:
      running = False
    

  # LOGIC
  try:
    for button in buttons:
      button.update(events)

  except IndexError:
      print("error")


  for entety in enteties[:]:
    if entety.radius <= 0:
      enteties.remove(entety)

      if len(enteties) == 1:
         print("DONE")

  # VISUAL

  screen.fill("white")

  for button in buttons:
      button.draw_self(screen)

  for entety in enteties:
     entety.draw_self(screen)

  pygame.display.flip()

  clock.tick(60)

pygame.quit()
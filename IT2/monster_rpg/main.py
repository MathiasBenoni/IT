import pygame
import os

from classes import *
import functions as my_funcs
HEIGHT = 720
WIDTH = 1280

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.init()
pygame.font.init()

pygame.display.set_caption("Voidstrike")

running = True


button_width = 150
button_height = 40
padding = 10

global_y_pos = HEIGHT - 150
enemy_x_pos = WIDTH // 2 + 150

creatures = [
  Player(100, (WIDTH // 6 - button_width // 4, global_y_pos), "VG3/IT/IT2/monster_rpg/assets/images/turtle.webp"),
  Foe(200, (enemy_x_pos, global_y_pos), "VG3/IT/IT2/monster_rpg/assets/images/samurai.gif", lambda: my_funcs.attack(creatures[0], 35)), 
  Foe(50, (enemy_x_pos + 200 + 50 + padding, global_y_pos), "VG3/IT/IT2/monster_rpg/assets/images/samurai.gif", lambda: my_funcs.attack(creatures[0], 15))
]

player = creatures[0]


"""
TODO:

Make pos not be a tuple (classes.py) - 45

"""


# print(enteties)

### DAMAGE VARS

stab = 20
tentacles = 2
lightning = 4


buttons = [
    Button(button_width, button_height, 'gray', 'yellow', (WIDTH // 3, HEIGHT // 2 - button_height - padding), 'Stab', lambda: player.attack('stab', stab)),
    Button(button_width, button_height, 'gray', 'yellow', (WIDTH // 3, HEIGHT // 2), 'Tentacles', lambda: player.attack('tentacles', tentacles)),
    Button(button_width, button_height, 'gray', 'yellow', (WIDTH // 3, HEIGHT // 2 + button_height + padding), 'Lightning', lambda: player.attack('lightning', lightning)),
    Button(button_width, button_height, 'gray', 'green', (WIDTH // 3, HEIGHT // 2 + button_height * 2 + padding * 2), 'Quit', my_funcs.quit_game)
  ]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

background = pygame.image.load(os.path.join(BASE_DIR, "assets", "images", "background.jpg")).convert()
scale = screen.get_height() / background.get_height()
background = pygame.transform.scale(background, screen.get_size())

# fences = pygame.image.load(os.path.join(BASE_DIR, "assets", "images", "foreground_fences.png")).convert_alpha()
# fences = pygame.transform.scale(fences, screen.get_size())


GROUND_Y = int(200 * scale)



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


  for entety in creatures[:]:
    if entety.health <= 0:
      creatures.remove(entety)

      if len(creatures) == 1:
        print("DONE")
        my_funcs.quit_game()

  # VISUAL

  screen.fill("white")
  screen.blit(background, (0, 0))

  for entety in creatures:
     entety.draw_self(screen)

  # screen.blit(fences, (0, 0))

  for button in buttons:
        button.draw_self(screen)

  pygame.display.flip()

  clock.tick(60)

pygame.quit()
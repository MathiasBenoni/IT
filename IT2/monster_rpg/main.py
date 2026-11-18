import pygame
import os
import random

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

moves = Attacks()

# No () after moves.stab etc. -> we store the method so we can call it later
player = Player(500, (WIDTH // 6 - button_width // 4, global_y_pos), "VG3/IT/IT2/monster_rpg/assets/images/turtle.webp", {
  "Stab": moves.stab,
  "Tentacles": moves.tentacles,
  "Lightning": moves.lightning,
})

big_samurai = Foe(200, (enemy_x_pos, global_y_pos), "VG3/IT/IT2/monster_rpg/assets/images/samurai.gif", {
  "Slash": moves.slash,
  "Fireball": moves.fireball,
})

small_samurai = Foe(50, (enemy_x_pos + 200 + 50 + padding, global_y_pos), "VG3/IT/IT2/monster_rpg/assets/images/samurai.gif", {
  "Slash": moves.slash,
})

creatures = [player, big_samurai, small_samurai]


"""
TODO:

Make pos not be a tuple (classes.py) - 45

"""

def player_turn(attack):
  enemies = []
  for creature in creatures:
    if isinstance(creature, Foe):
      enemies.append(creature)

  attack(enemies)

  # Every living foe hits back with one of its own moves
  for foe in enemies:
    if foe.health > 0:
      foe_moves = list(foe.attacks.values())
      chosen = random.choice(foe_moves)
      chosen([player])


buttons = []
y = HEIGHT // 2 - button_height - padding

for name in player.attacks:
  attack = player.attacks[name]
  # attack=attack is needed, otherwise every button would use the last attack
  button = Button(button_width, button_height, 'gray', 'yellow', (WIDTH // 3, y), name,
                  lambda attack=attack: player_turn(attack))
  buttons.append(button)
  y = y + button_height + padding

buttons.append(Button(button_width, button_height, 'gray', 'green', (WIDTH // 3, y), 'Quit', my_funcs.quit_game))

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

  if player.health <= 0:
    print("GAME OVER")
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
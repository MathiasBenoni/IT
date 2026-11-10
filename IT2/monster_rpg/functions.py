import pygame

def start_game():
   print("START")

def quit_game():
  print("QUIT")
  pygame.event.post(pygame.event.Event(pygame.QUIT))

def attack(enemy : object, damage):
  enemy.take_damage(damage)

def attack_all(enemies : list, damage : int):
  for enemy in enemies:
    enemy.take_damage(damage)
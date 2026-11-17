import pygame

def start_game():
   print("START")

def quit_game():
  print("QUIT")
  pygame.event.post(pygame.event.Event(pygame.QUIT))

def attack(enemies : object | list, damage : int):
  
  if type(enemies) == list:
     
    for enemy in enemies:
        enemy.take_damage(damage)
  else:
     enemies.take_damage(damage)
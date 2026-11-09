import pygame
import classes

def start_game():
   print("START")

def quit_game():
  print("QUIT")
  pygame.event.post(pygame.event.Event(pygame.QUIT))

def attack(enemy):
   enemy.take_damage(10)
   
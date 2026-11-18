import pygame

def start_game():
   print("START")

def quit_game():
  print("QUIT")
  pygame.event.post(pygame.event.Event(pygame.QUIT))
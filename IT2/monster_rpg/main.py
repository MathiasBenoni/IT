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

def start_game():
   print("START")

buttons = [
    Button(300, 200, 'gray', (200, 100), 'Start', start_game),
    Button(300, 200, 'gray', (200, 400), 'Quit'),
    Button(300, 200, 'gray', (200, 300), 'test')
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

  screen.fill("purple")

  for button in buttons:
      button.draw_button(screen)


  pygame.display.flip()

  clock.tick(60)

pygame.quit()
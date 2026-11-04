
import pygame

class Entety:
  def __init__(self, radius : int, hostile : bool):
    self.radius = radius
    self.hostile = hostile

  def was_attacked(self, damage):
    self.radius -= damage
    if self.radius <= 0:
      return False

class Button:
  
  def __init__(self, width : int, height : int, color, pos : tuple, text : str, border_radius=10):
    if color == None:
      color = 'blue'
    self.width = width
    self.height = height
    self.color = color
    self.border_radius = border_radius
    self.pos = pos

    self.text = text
    self.font = pygame.font.SysFont('Arial', 100)

    self.default_color = self.color

  def update(self):
    if self.is_hovering():
      self.color = 'blue'
    else:
      self.color = self.default_color

  def draw_button(self, screen):
    pygame.draw.rect(screen, self.color, (
      self.pos[0],
      self.pos[1],
      self.width,
      self.height
    ), 0, self.border_radius)

    text_surface = self.font.render(self.text, True, 'white')

    text_rect = text_surface.get_rect(
      center=(
        self.pos[0] + self.width // 2,
        self.pos[1] + self.height // 2
      )
    )
    screen.blit(text_surface, text_rect)

  def is_hovering(self):
    temp_rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
    

    return temp_rect.collidepoint(pygame.mouse.get_pos())
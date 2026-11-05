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
  
  def __init__(self, width : int, height : int, color : str, pos : tuple, text : str, on_click=None, border_radius=10):
    if color == None:
      color = 'blue'
    self.width = width
    self.height = height
    self.color = color
    self.border_radius = border_radius
    self.pos = pos
    self.on_click = on_click

    self.text = text
    self.font = pygame.font.SysFont('Arial', 100)

    self.default_color = self.color

  def update(self, events):
    
    if self.is_hovering():
      self.color = 'blue'

      if self.clicked(events):
        if self.on_click:
          self.on_click()

    else:
      self.color = self.default_color

  def clicked(self, events):
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        return True
      
    return False

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
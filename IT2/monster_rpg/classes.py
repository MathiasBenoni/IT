import pygame

class Entity:
  def __init__(self, pos : tuple):
    self.pos = pos
  

class Creature(Entity):
  id = 0
  def __init__(self, health : int, hostile : bool, color : str, pos : tuple, sprite : str):
    super().__init__(pos)
    self.hostile = hostile
    self.health = health

    self.color = color

    self.sprite = sprite

    self.pos = pos
    # self.rect = pygame.Rect(0, 0, self.radius, self.radius)
    # self.rect.center = self.pos

    self.id = Creature.id
    Creature.id += 1


    self.heathbar = HealthBar(self.pos)

  def __repr__(self):
    return f"{self.__class__.__name__}({self.health}, {self.hostile}, {self.color}, {self.pos}, '{self.sprite}')"

  def take_damage(self, damage):
    self.health -= damage
    if self.health <= 0:
      return False
    
  def draw_self(self, screen):
    
    self.image = pygame.image.load(self.sprite)
    self.image_rect = self.image.get_rect(center=self.pos)

    if self.hostile:
      screen.blit(pygame.transform.flip(self.image, True, False), self.image_rect)
    else:
      screen.blit(self.image, self.image_rect)

    self.heathbar.draw(screen)
    # pygame.draw.circle(screen, self.color, (self.pos), self.radius)

class HealthBar:
  def __init__(self, pos : tuple, color="red", border_radius=5):

    self.width = 100
    self.height = 20
    self.color = color
    self.border_radius = border_radius

    self.pos = pos

    self.rect = pygame.Rect(0, 0, self.width, self.height)
    self.rect.center = self.pos

  def draw(self, screen):
    pygame.draw.rect(screen, self.color, self.rect, 0, self.border_radius)
    pass

class Button(Entity):
  
  def __init__(self, width : int, height : int, color : str, hover_color : str, pos : tuple, text : str, on_click=None, border_radius=5):
    if color == None:
      color = 'blue'
    super().__init__(pos)
    self.width = width
    self.height = height
    self.color = color
    self.border_radius = border_radius
    
    self.on_click = on_click

    self.text = text
    self.font = pygame.font.SysFont('Arial', 30)

    self.default_color = self.color
    self.hover_color = hover_color

    self.rect = pygame.Rect(0, 0, self.width, self.height)
    self.rect.center = self.pos
    
    

  def update(self, events):
    
    if self.is_hovering():
      self.color = self.hover_color

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

  def draw_self(self, screen):
    pygame.draw.rect(screen, self.color, self.rect, 0, self.border_radius)

    text_surface = self.font.render(self.text, True, 'white')

    text_rect = text_surface.get_rect(center=self.rect.center)
    screen.blit(text_surface, text_rect)

  def is_hovering(self):
    return self.rect.collidepoint(pygame.mouse.get_pos())
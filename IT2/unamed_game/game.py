import pygame

WIDTH = 1280
HEIGHT = 720
MOVE_SPEED = 500


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
delta_time = 0


player_coordinates = {
   "x": WIDTH / 2 - 40 / 2,
   "y": HEIGHT / 2 - 40 / 2
}
player_pos = pygame.Vector2(player_coordinates["x"], player_coordinates["y"])

touched = False

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill("white")


  wall = pygame.draw.rect(screen, "black", (0, 0, WIDTH, 50))


  # Player
  player = pygame.draw.rect(screen, "red", (*player_pos, 40, 40))

  

  keys = pygame.key.get_pressed()

  movement = pygame.Vector2(0, 0)

  if keys[pygame.K_w]:
      movement.y -= MOVE_SPEED * delta_time
  if keys[pygame.K_s]:
      movement.y += MOVE_SPEED * delta_time
  if keys[pygame.K_a]:
      movement.x -= MOVE_SPEED * delta_time
  if keys[pygame.K_d]:
      movement.x += MOVE_SPEED * delta_time

  # Move
  player_pos += movement

  # Update the rect's position
  player.topleft = player_pos

  # If we hit the wall, undo the movement
  if player.colliderect(wall):
      player_pos -= movement
      player.topleft = player_pos
  



  pygame.display.flip()

  delta_time = clock.tick(60) / 1000

pygame.quit()
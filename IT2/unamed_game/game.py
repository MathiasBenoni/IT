import pygame

WIDTH = 1280
HEIGHT = 720
MOVE_SPEED = 500

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(
    WIDTH / 2 - 40 / 2,
    HEIGHT / 2 - 40 / 2
)

movement = pygame.Vector2(0, 0)
next_movement = pygame.Vector2(0, 0)

while running:

    delta_time = clock.tick(60) / 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                next_movement = pygame.Vector2(0, -1)

            elif event.key == pygame.K_s:
                next_movement = pygame.Vector2(0, 1)

            elif event.key == pygame.K_a:
                next_movement = pygame.Vector2(-1, 0)

            elif event.key == pygame.K_d:
                next_movement = pygame.Vector2(1, 0)

    
    if movement.length_squared() == 0:
        movement = next_movement
        next_movement = pygame.Vector2(0, 0)

    
    velocity = movement * MOVE_SPEED * delta_time

    # Move
    player_pos += velocity

    
    player = pygame.Rect(
        *player_pos,
        40,
        40
    )

    
    wall = pygame.Rect(0, 0, WIDTH, 50)

    
    if player.colliderect(wall):

        
        player_pos -= velocity

        
        movement = pygame.Vector2(0, 0)

        
        movement = next_movement
        next_movement = pygame.Vector2(0, 0)

    
    screen.fill("white")
    pygame.draw.rect(screen, "black", wall)
    pygame.draw.rect(screen, "red", (*player_pos, 40, 40))

    pygame.display.flip()

pygame.quit()
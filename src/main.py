import pygame
from player import Player
from map import Map
pygame.init()

D_Width, D_Length = 1000,800
canvas = pygame.Surface((D_Width, D_Length))
window = pygame.display.set_mode((D_Width,D_Length))
running = True
clock = pygame.time.Clock()
fps = 60
player = Player()
ground = Map()

while running:
    dt = clock.tick(60) * .001 * fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.LEFT_KEY = True
            elif event.key == pygame.K_RIGHT:
                player.RIGHT_KEY = True
            elif event.key == pygame.K_SPACE:
                player.jump()


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.LEFT_KEY = False
            elif event.key == pygame.K_RIGHT:
                player.RIGHT_KEY = False
            elif event.key == pygame.K_SPACE:
                if player.is_jumping:
                    player.velocity.y *= .25
                    player.is_jumping = False
        
        if pygame.mouse.get_pressed()[0]:
            ground.add_ground(canvas, pygame.mouse.get_pos())
    player.update(dt, D_Length)  
    
        
    canvas.fill((0, 255, 255))
    window.blit(canvas, (0,0))
    try:
        ground.draw(window)
    except:
        pass
    player.draw(window)    
    pygame.display.update()

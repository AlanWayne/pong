import pygame as pg
from colors import *
from random import random

WINDOW_WIDTH  = 640
WINDOW_HEIGHT = 480
FPS = 60

pg.init()
pg.mixer.init()  
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
surface = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))


pg.display.set_caption("Pong")
clock = pg.time.Clock()

game_running = True

# player
pl_width = 10
pl_height = 80
pl_x = 10
pl_y = WINDOW_HEIGHT // 2 - pl_height // 2
move_down = False
move_up   = False
pl_speed = 10

# enemy
en_width = 10
en_height = 80
en_x = WINDOW_WIDTH - en_width - 10
en_y = WINDOW_HEIGHT // 2 - en_height // 2
en_speed = 10

# ball
bl_radius = 10
bl_x = WINDOW_WIDTH // 2 - bl_radius // 2
bl_y = WINDOW_HEIGHT // 2 - bl_radius // 2
bl_speed = 15
bl_speed_v = bl_speed * random()
bl_speed_h = bl_speed - bl_speed_v

while game_running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_running = False
            
# input
        key = pg.key.get_pressed()
        if key[pg.K_w]:
            pl_speed = -10
        elif key[pg.K_s]:
            pl_speed = 10
        else:
            pl_speed = 0

# player movement
    pl_y += pl_speed
    if pl_y < 0:
        pl_y = 0
    elif pl_y > WINDOW_HEIGHT - pl_height:
        pl_y = WINDOW_HEIGHT - pl_height

# enemy movement
    if en_y < bl_y - en_height // 2:
        en_y += en_speed
    elif en_y > bl_y - en_height // 2:
        en_y -= en_speed

    if en_y < 0:
        en_y = 0
    elif en_y > WINDOW_HEIGHT - en_height:
        en_y = WINDOW_HEIGHT - en_height
    
        
# ball movement
    bl_x += bl_speed_h
    bl_y += bl_speed_v
    
    if bl_y > WINDOW_HEIGHT - bl_radius or bl_y < bl_radius:
        bl_speed_v = - bl_speed_v

    if bl_x < pl_x + pl_width + bl_radius and bl_y > pl_y and bl_y < pl_y + pl_height:
        bl_speed_h = -bl_speed_h

    if bl_x > en_x - bl_radius and bl_y > en_y and bl_y < en_y + en_height:
        bl_speed_h = -bl_speed_h

    
    

# draw
    surface.fill(GRAY10)

    pg.draw.rect(surface,GRAY90,(pl_x,pl_y,pl_width,pl_height))
    pg.draw.rect(surface,GRAY90,(en_x,en_y,en_width,en_height))
    pg.draw.circle(surface,GRAY90,(bl_x,bl_y),bl_radius)

    screen.blit(surface,(0,0))
    pg.display.flip()
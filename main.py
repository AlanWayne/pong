import pygame as pg
from colors import *

WINDOW_WIDTH  = 640
WINDOW_HEIGHT = 480
FPS = 60

pg.init()
pg.mixer.init()  
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Pong")
clock = pg.time.Clock()
screen.fill(BLACK)

game_running = True

while game_running:
    clock.tick(FPS)


    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_running = False


    pg.display.flip()

############################
# Filename: sacrilege.py
# Desc: Main game loop
# Date created: 04/22/2022
############################
import config as c
import pygame as pg
import ground
import sys

view = pg.image.load("sprites/mid.png").convert_alpha()
view = pg.transform.scale(view, (c.WIDTH, c.HEIGHT))
ground.make()


def next():  # updates frame
    pg.display.update()
    pg.event.clear()
    c.clock.tick(100)


def draw():
    ground.group.draw(c.screen)
    c.screen.blit(view, (0, 0))


def keys():
    x = 0
    y = 0
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        y += 1
    if keys[pg.K_s]:
        y -= 1
    if keys[pg.K_a]:
        x += 1
    if keys[pg.K_d]:
        x -= 1
    if x != 0 and y != 0:
        c.pos[0] += x * c.DIAG_SPEED
        c.pos[1] += y * c.DIAG_SPEED
    else:
        c.pos[0] += x * c.SPEED
        c.pos[1] += y * c.SPEED


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            exit(0)
    keys()
    ground.move()
    draw()
    next()

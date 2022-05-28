############################
# Filename: main.py
# Desc: Main game loop
# Date created: 04/22/2022
############################
import config as c
import pygame as pg
import ground
import player
import wd
import npc
import obst
import sys

black = c.image("black")
mask = c.image("mask")
ground.make()
move_count = 0
moving = False


def next():  # updates frame
    pg.display.update()
    pg.event.clear()
    c.clock.tick(100)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            exit(0)


def in_radius(x, y, r):
    return x*x + y*y <= r*r


def keys():
    global move_count
    global moving
    x = 0
    y = 0
    move_vector = [0, 0]
    keys = pg.key.get_pressed()  # x is always inverted for some reason
    if keys[pg.K_w]:
        y += 1
    if keys[pg.K_s]:
        y -= 1
    if keys[pg.K_a]:
        x -= 1
    if keys[pg.K_d]:
        x += 1
    if x == 0 and y == 0:
        moving = False
        c.pl_state[2] = 3
        return
    elif moving == False:
        moving = True
        move_count = 10
        player.upd()
    move_vector, c.pl_state = c.move_anim(
        x, y, c.SPEED, c.DIAG_SPEED, c.pl_state)
    if in_radius(c.offset[0]+move_vector[0], c.offset[1]-move_vector[1], c.OFFSET_RAD):
        c.offset[0] += move_vector[0]
        c.offset[1] -= move_vector[1]
        player.pl.re_position()
    else:
        c.pos[0] += move_vector[0]
        c.pos[1] += move_vector[1]


def draw():
    ground.draw()
    player.draw()
    c.screen.blit(mask, (0, 0))
    c.screen.blit(black, (0, 0))


while True:
    move_count += 1
    if move_count >= 10:
        move_count = 0
        player.upd()
    keys()
    ground.move()
    draw()
    next()

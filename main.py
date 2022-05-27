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


def next():  # updates frame
    pg.display.update()
    pg.event.clear()
    c.clock.tick(100)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            exit(0)


def keys():
    x = 0
    y = 0
    move_vector = [0, 0]
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        y += 1
    if keys[pg.K_s]:
        y -= 1
    if keys[pg.K_a]:
        x -= 1
    if keys[pg.K_d]:
        x += 1

    if x != 0 and y != 0:
        if x == -1:
            c.pl_state[1] = True
        if y == 1:
            c.pl_state[0] = 4
        else:
            c.pl_state[0] = 2
        move_vector[0] = x * c.DIAG_SPEED
        move_vector[1] = y * c.DIAG_SPEED
    else:
        if x == 1:
            c.pl_state[1] = True
            c.pl_state[0] = 3
        elif x == -1:
            c.pl_state[1] = False
            c.pl_state[0] = 3
        elif y == 1:
            c.pl_state[0] = 0
        else:
            c.pl_state[0] = 1
        move_vector[0] = x * c.SPEED
        move_vector[1] = y * c.SPEED
    c.pos[0] += move_vector[0]
    c.pos[1] += move_vector[1]
    print(c.pos)


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

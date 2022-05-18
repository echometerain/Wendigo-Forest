############################
# Filename: sacrilege.py
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


def next():  # updates frame
    pg.display.update()
    pg.event.clear()
    c.clock.tick(100)


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
        x += 1
    if keys[pg.K_d]:
        x -= 1
    if x != 0 and y != 0:
        move_vector[0] = x * c.DIAG_SPEED
        move_vector[1] = y * c.DIAG_SPEED
    else:
        move_vector[0] = x * c.SPEED
        move_vector[1] = y * c.SPEED


def draw():
    ground.group.draw(c.screen)
    c.screen.blit(mask, (0, 0))
    c.screen.blit(black, (0, 0))


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

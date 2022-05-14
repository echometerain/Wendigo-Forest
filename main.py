#!/usr/bin/env python
############################
# Filename: sacrilege.py
# Desc: Main game loop
# Date created: 04/22/2022
############################
import config as c
import pygame as pg
import ground
import sys
import math


def next():  # updates frame
    pg.display.update()
    pg.event.clear()
    c.clock.tick(60)


def draw():
    ground.group.draw(c.screen)


while True:
    x = 0
    y = 0
    for event in pg.event.get():
        if event.type == pg.K_w:
            y -= c.SPEED
        if event.type == pg.K_s:
            y += c.SPEED
        if event.type == pg.K_a:
            x -= c.SPEED
        if event.type == pg.K_d:
            x -= c.SPEED
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            exit(0)
    if x != 0 and y != 0:
        pos[0] += x*math.sqrt(2)
        pos[1] += y*math.sqrt(2)
    else:
        pos[0] += x
        pos[1] += y

    ground.move()
    draw()
    next()

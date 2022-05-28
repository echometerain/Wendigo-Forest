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


def next():  # updates frame
    pg.display.update()
    c.clock.tick(100)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            exit(0)
    pg.event.clear()


def keys():
    x = 0
    y = 0
    keys = pg.key.get_pressed()  # x is always inverted for some reason
    if keys[pg.K_w]:
        y += 1
    if keys[pg.K_s]:
        y -= 1
    if keys[pg.K_a]:
        x -= 1
    if keys[pg.K_d]:
        x += 1
    player.pl.move(x, y)


def draw():
    ground.draw()
    player.draw()
    c.screen.blit(mask, (0, 0))
    c.screen.blit(black, (0, 0))


while True:
    keys()
    ground.move()
    draw()
    next()

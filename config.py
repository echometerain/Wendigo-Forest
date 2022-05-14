#!/usr/bin/env python
############################
# Filename: config.py
# Desc: Configuration
# Date created: 04/22/2022
############################
import pygame as pg

pg.init() # starts pygame and functions
pg.mixer.pre_init(44100, 16, 2, 4096)
pg.mixer.init()

pg.font.init()

screen = pg.display.set_mode((0,0), pg.HWSURFACE | pg.FULLSCREEN | pg.DOUBLEBUF, 16)
WIDTH, HEIGHT = pg.display.get_surface().get_size() # screen width and height
IN_WIDTH, IN_HEIGHT = (448, 252) # internal size
IN_RATIO = WIDTH / IN_WIDTH

#pg.display.set_icon(pg.image.load("sprites/icon.png").convert_alpha())
pg.display.set_caption("Sacrilege")

pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])

clock = pg.time.Clock()

ground = pg.image.load("sprites/ground.png").convert()
ground = pg.transform.scale(plat, (ground.get_height()*IN_RATIO, ground.get_width()*IN_RATIO), screen)
plat_rect = plat.get_rect(topleft = (0,0))
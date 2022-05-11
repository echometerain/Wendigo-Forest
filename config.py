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

#pg.display.set_icon(pg.image.load("sprites/icon.png").convert_alpha())
pg.display.set_caption("Sacrilege")

pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])

clock = pg.time.Clock()

plat = pg.image.load("sprites/plat.png").convert_alpha()
plat = pg.transform.scale(plat, (WIDTH, HEIGHT))
plat_rect = plat.get_rect(topleft = (0,0))
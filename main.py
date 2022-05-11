#!/usr/bin/env python
############################
# Filename: sacrilege.py
# Desc: Main game loop
# Date created: 04/22/2022
############################
import config as c
import pygame as pg
import sys

def next(): # updates frame
	pg.display.update()
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()
			exit(0)
	pg.event.clear();c.clock.tick(60)
    

while True:
    c.screen.blit(c.plat, c.plat_rect)
    next()
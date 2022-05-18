############################
# Filename: player.py
# Desc: Manage player movement
# Date created: 04/22/2022
############################
import pygame as pg
import config as c


def get_state():
    if c.pl_state[0] == 1:
        if c.pl_state[1] == 1:

    else:
        if c.pl_state[1] == 1:


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super.__init__()
        self.image = c.image(f"pl_{}")

    def update(self):
        self.image = c.image

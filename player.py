############################
# Filename: player.py
# Desc: Manage player movement
# Date created: 04/22/2022
############################
import pygame as pg
import config as c


def get_state():
    return pl_state[0]*5+pl_state[2]


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super.__init__()
        self.spritesheet = pygame.image.load(
            "sprites/player.png").convert_alpha()
        self.rect = self.spritesheet.get_rect()
        self.sheetWidth = self.rect.width
        self.numImages = numImages
        self.rect.width = self.sheetWidth//numImages

    def update(self):
        self.image = c.image

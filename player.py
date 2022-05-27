############################
# Filename: player.py
# Desc: Manage player movement
# Date created: 04/22/2022
############################
import pygame as pg
import config as c


def get_sprites():
    return c.pl_state[0]*5+c.pl_state[2]+1


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spritesheet = c.image("player")
        self.rect = self.spritesheet.get_rect()
        self.sheetWidth = self.rect.width
        self.numImages = 25
        self.rect.width = self.sheetWidth//self.numImages
        self.update()
        self.re_position()

    def update(self):
        self.spritesheet.set_clip(
            self.rect.width*get_sprites(), 0, self.rect.width, self.rect.height)
        self.image = self.spritesheet.subsurface(self.spritesheet.get_clip())
        if c.pl_state[1]:
            self.image = pg.transform.flip(self.image, True, False)
        if c.pl_state[2] < 0:
            c.pl_state[2] = 3
        c.pl_state[2] -= 1

    def re_position(self):
        self.rect = self.image.get_rect(
            center=(c.WIDTH//2+c.offset[0], c.HEIGHT//2+c.offset[1]))


pl = Player()
group = pg.sprite.Group()
group.add(pl)


def upd():
    pl.update()


def draw():
    group.draw(c.screen)

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
    moving = False
    move_count = 0

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
            c.pl_state[2] = 4
        c.pl_state[2] -= 1

    def re_position(self):
        self.rect = self.image.get_rect(
            center=(c.WIDTH//2+c.offset[0], c.HEIGHT//2+c.offset[1]))

    def move(self, x, y):
        move_vector = [0, 0]
        self.move_count += 1
        if self.move_count >= 10:
            self.move_count = 0
            self.update()
        if x == 0 and y == 0:
            self.moving = False
            c.pl_state[2] = 3
            return
        elif self.moving == False:
            self.moving = True
            self.move_count = 10
            self.update()
        move_vector, c.pl_state = c.move_anim(
            x, y, c.SPEED, c.DIAG_SPEED, c.pl_state)
        if in_radius(c.offset[0]+move_vector[0], c.offset[1]-move_vector[1], c.OFFSET_RAD):
            c.offset[0] += move_vector[0]
            c.offset[1] -= move_vector[1]
            self.re_position()
        else:
            c.pos[0] += move_vector[0]
            c.pos[1] += move_vector[1]


pl = Player()
group = pg.sprite.Group()
group.add(pl)


def draw():
    group.draw(c.screen)


def in_radius(x, y, r):
    return x*x + y*y <= r*r

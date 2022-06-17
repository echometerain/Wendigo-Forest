import pygame as pg
import config as c


class Remains():
    pos = [0, 0]
    screen_pos = [0, 0]

    def __init__(self, pos_x, pos_y, type):
        self.pos[0] = pos_x
        self.pos[1] = pos_y
        self.image = c.image(f"{type}_remains")
        self.rect = self.image.get_rect()
        self.re_position()

    def re_position(self):
        self.rect.center = (
            c.WIDTH//2-(c.cam_pos[0]-self.pos[0]),
            c.HEIGHT//2+(c.cam_pos[1]-self.pos[1])
        )

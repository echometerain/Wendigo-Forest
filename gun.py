import pygame as pg
import config as c
import math


class Gun():
    rm = False
    pos = [0, 0]
    screen_pos = [0, 0]
    vector = [0, 0]

    def __init__(self, pl_x, pl_y):
        self.pos[0] = pl_x
        self.pos[1] = pl_y
        mouse_pos = pg.mouse.get_pos()
        rel_mouse_pos = [
            mouse_pos[0] - c.WIDTH//2 + c.cam_pos[0] - pl_x,
            -(mouse_pos[1] - c.HEIGHT//2 - c.cam_pos[1] + pl_y)
        ]
        len_vector = math.sqrt(rel_mouse_pos[0]**2+rel_mouse_pos[1]**2)
        self.vector = [
            (rel_mouse_pos[0]/len_vector)*c.GUN_SPEED,
            (rel_mouse_pos[1]/len_vector)*c.GUN_SPEED
        ]

    def move(self):

    def re_position(self):

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

    def move(self):  # apply the movement vector onto the bullet's position
        self.pos[0] += self.vector[0]  # x coordinate
        self.pos[1] += self.vector[1]  # y coordinate
        self.re_position()  # call re_position

    def re_position(self):
        self.screen_pos[0] = self.pos[0] - c.cam_pos[0] + c.WIDTH//2
        self.screen_pos[1] = self.pos[1] - c.cam_pos[1] + c.HEIGHT//2
        # a function which would convert the game position
        # of the bullet to its relative position on the screen

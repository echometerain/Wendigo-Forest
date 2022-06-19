############################
# Filename: gun.py
# Desc: Manage bullets
# Date created: 06/14/2022
############################
import pygame as pg
import config as c
import math


class Gun():
    rm = False  # whether bullet needs removal
    pos = [0, 0]  # in-game position
    screen_pos = [0, 0]  # position on screen
    vector = [0, 0]  # movement vector

    def __init__(self, pl_x, pl_y):
        self.pos[0] = pl_x  # sets position to player position
        self.pos[1] = pl_y
        mouse_pos = pg.mouse.get_pos()
        rel_mouse_pos = [  # get position of mouse relative to the player
            mouse_pos[0] - c.WIDTH//2 + c.cam_pos[0] - pl_x,
            -(mouse_pos[1] - c.HEIGHT//2 - c.cam_pos[1] + pl_y)
        ]
        # get vector length
        len_vector = math.sqrt(rel_mouse_pos[0]**2+rel_mouse_pos[1]**2)
        self.vector = [  # normalize vectors and set them to a speed
            (rel_mouse_pos[0]/len_vector)*c.GUN_SPEED,
            (rel_mouse_pos[1]/len_vector)*c.GUN_SPEED
        ]

    def move(self):  # apply the movement vector onto the bullet's position
        self.pos[0] += self.vector[0]  # x coordinate
        self.pos[1] += self.vector[1]  # y coordinate
        if self.pos[0] > c.WIDTH//2 or self.pos[0] < -c.WIDTH//2 \
                or self.pos[1] > c.HEIGHT//2 or self.pos[1] < -c.HEIGHT//2:
            self.rm = True  # removes bullet if out of range
        self.re_position()  # call re_position

    def re_position(self):  # converts in-game position to screen position
        self.screen_pos = [
            c.WIDTH//2-(c.cam_pos[0]-self.pos[0]),
            c.HEIGHT//2+(c.cam_pos[1]-self.pos[1])
        ]

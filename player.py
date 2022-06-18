############################
# Filename: player.py
# Desc: Manage player action
# Date created: 04/22/2022
############################
import pygame as pg
import config as c
import entity


class Player(entity.Entity):
    ammo_count = 3

    def __init__(self):
        super().__init__("player", 25, 5, c.PL_SPEED, [0, 0], 30, 65)

    def move(self, x, y):
        if x == 0 and y == 0:
            self.moving = False
            self.anim_state[2] = 3
            self.update()
            return
        move_vector = self.move_anim(x, y)
        self.pos[0] += move_vector[0]
        self.pos[1] += move_vector[1]
        if (c.cam_pos[0]-self.pos[0]-move_vector[0])**2 \
                + (c.cam_pos[1]-self.pos[1]-move_vector[1])**2 <= c.OFFSET_RAD**2:
            self.re_position()
        else:
            c.cam_pos[0] += move_vector[0]
            c.cam_pos[1] += move_vector[1]
        self.re_position()

############################
# Filename: npc.py
# Desc: Manage npc actions
# Date created: 04/26/2022
############################
import entity
import pygame as pg
import config as c
import random
import time
import math


class NPC(entity.Entity):
    has_ammo = True
    run_index = -1

    def __init__(self, pos):  # constructor
        super().__init__("npc", 25, 5, c.NPC_SPEED, pos, 30, 65)

    def check_move(self, pl):
        # check if close to you, doesn't move when close to you
        if (pl.pos[0]-self.pos[0])**2 \
                + (pl.pos[1]-self.pos[1])**2 >= c.NPC_CLOSE_RAD**2:
            self.moving = True
            x = 0
            y = 0
            if abs(pl.pos[0]-self.pos[0]) < self.diag_speed:  # fix for sprite flashing
                self.pos[0] = pl.pos[0]
            if abs(pl.pos[1]-self.pos[1]) < self.diag_speed:
                self.pos[1] = pl.pos[1]
            if pl.pos[0]-self.pos[0] < 0:  # finds the drection to follow you
                x = -1
            elif pl.pos[0]-self.pos[0] > 0:
                x = 1
            if pl.pos[1]-self.pos[1] < 0:
                y = -1
            elif pl.pos[1]-self.pos[1] > 0:
                y = 1
            self.move(x, y)
            self.re_position()
        elif self.moving:
            if self.has_ammo:  # gives you ammo
                pl.ammo_count += random.randint(1, 3)
                self.has_ammo = False
            self.moving = False
            self.anim_state[2] = 3  # idle position
            self.update()  # update animation
            return

    def move(self, x, y):
        move_vector = self.move_anim(x, y)
        self.pos[0] += move_vector[0]  # moves itself
        self.pos[1] += move_vector[1]

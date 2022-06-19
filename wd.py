############################
# Filename: wd.py
# Desc: Manage wendigo action
# Date created: 05/13/2022
############################
import pygame as pg
import config as c
import entity


class Wendigo(entity.Entity):  # dedicated to wendigoon <3
    run = False  # "run away" mode activates after it eats someone

    def __init__(self, pos):
        super().__init__("wendigo", 25, 5, c.WD_SPEED, pos, 125, 50)

    def check_move(self, pl):
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
        if self.run:
            self.move(-x, -y)  # runs away from you
            # removes wendigo when it gets off-screen
            # they are faster than you
            if self.pos[0] > c.WIDTH//2 or self.pos[0] < -c.WIDTH//2 \
                    or self.pos[1] > c.HEIGHT//2 or self.pos[1] < -c.HEIGHT//2:
                self.rm = True
        else:
            self.move(x, y)  # runs towards you
        self.re_position()  # changes screen position

    def move(self, x, y):
        move_vector = self.move_anim(x, y)
        self.pos[0] += move_vector[0]  # moves itself
        self.pos[1] += move_vector[1]

import pygame as pg
import config as c
import entity


class NPC(entity.Entity):
    def __init__(self, start_pos):
        super().__init__("npc", 25, 5, c.NPC_SPEED, [0, 0])
        self.pos = start_pos

    def check_move(self, pl):
        if (pl.pos[0]-self.pos[0])**2 \
                + (pl.pos[1]-self.pos[1])**2 >= c.NPC_CLOSE_RAD**2:
            x = 0
            y = 0
            if abs(pl.pos[0]-self.pos[0]) < self.diag_speed:
                self.pos[0] = pl.pos[0]
            if abs(pl.pos[1]-self.pos[1]) < self.diag_speed:
                self.pos[1] = pl.pos[1]
            if pl.pos[0]-self.pos[0] < 0:
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
            self.moving = False
            self.anim_state[2] = 3
            self.update()
            return

    def move(self, x, y):
        move_vector = self.move_anim(x, y)
        self.pos[0] += move_vector[0]
        self.pos[1] += move_vector[1]

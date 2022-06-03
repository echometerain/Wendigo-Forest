import pygame as pg
import config as c
import entity


class NPC(entity.Entity):
    def __init__(self):
        super().__init__("npc", 25, 5, c.PL_SPEED, [0, 0])
        self.pos = [0, 0]

    def check_move(pl):
        # if (pl.pos[0]-self.pos[0])**2 \
        #         + (pl.pos[0]-self.pos[1])**2 >= c.NPC_CLOSE_RAD**2:
        #     x = 0
        #     y = 0
        #     if pl.pos[0]-self.pos[0] <=
        pass

    def move(self, x, y):
        if x == 0 and y == 0:
            self.moving = False
            self.anim_state[2] = 3
            self.update()
            return
        move_vector = self.move_anim(x, y)
        self.pos[0] += move_vector[0]
        self.pos[1] += move_vector[1]

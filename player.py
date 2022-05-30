############################
# Filename: player.py
# Desc: Manage player action
# Date created: 04/22/2022
############################
import pygame as pg
import config as c
import entity


class Player(entity.Entity):
    def __init__(self):
        super().__init__("player", 25, 5, c.PL_SPEED, [0, 0])

    def in_radius(self):
        return (self.pos[0] - c.cam_pos[0])**2 + (self.pos[0] - c.cam_pos[0])**2 <= c.OFFSET_RAD**2

    def move(self, x, y):
        move_vector = [0, 0]
        self.nomove_frames += 1
        if self.nomove_frames >= 10:
            self.nomove_frames = 0
            self.update()
        if x == 0 and y == 0:
            self.moving = False
            self.anim_state[2] = 3
            return
        elif self.moving == False:
            self.moving = True
            self.nomove_frames = 10
            self.update()
        move_vector = self.move_anim(x, y)
        self.pos[0] += move_vector[0]
        self.pos[1] -= move_vector[1]  # -= may be a problem
        if not self.in_radius():
            c.cam_pos[0] += move_vector[0]
            c.cam_pos[1] -= move_vector[1]
        else:
            self.re_position()


pl = Player()
group = pg.sprite.Group()
group.add(pl)


def draw():
    group.draw(c.screen)

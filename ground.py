############################
# Filename: ground.py
# Desc: Generate ground tiles
# Date created: 05/15/2022
############################
import pygame as pg
import config as c

cur_pos = [0, 0]  # current position
SIZE = int(64 * c.IN_RATIO)  # the ground file is 64px large
tiles = []
group = pg.sprite.Group()


class Ground(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pg.image.load("sprites/ground_gray.png").convert()
        self.image = pg.transform.scale(self.image, (SIZE, SIZE))
        self.rect = self.image.get_rect(bottomright=(x, y))

    def move_to(self, x, y):
        self.rect = self.image.get_rect(bottomright=(x, y))


def make():  # makes the tiles
    for i in range(cur_pos[0], c.WIDTH, SIZE):
        tiles.append([])
        for j in range(cur_pos[1], c.WIDTH, SIZE):
            tmp_ground = Ground(i, j)
            group.add(tmp_ground)
            tiles[len(tiles) - 1].append(tmp_ground)


def move():  # moves the tiles
    cur_pos[0] = -c.pos[0] % SIZE  # how the f*ck does this work
    cur_pos[1] = c.pos[1] % SIZE
    for i in range(cur_pos[0]+SIZE, c.WIDTH, SIZE):
        for j in range(cur_pos[1], c.WIDTH, SIZE):
            tiles[(i-cur_pos[0]) // SIZE][(j-cur_pos[1]) // SIZE].move_to(i, j)


def draw():  # draws all the ground tiles
    group.draw(c.screen)

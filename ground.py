############################
# Filename: ground.py
# Desc: Infinite ground tiles generation
# Date created: 05/15/2022
############################
import pygame as pg
import config as c

cur_pos = [0, 0]  # current position
SIZE = int(64 * c.IN_RATIO)  # the ground file is 64px large
tiles = []
group = pg.sprite.Group()


class Ground(pg.sprite.Sprite):  # tile object
    def __init__(self, x, y):
        super().__init__()

        self.image = pg.image.load("sprites/ground_gray.png").convert()
        self.image = pg.transform.scale(self.image, (SIZE, SIZE))
        self.move_to(x, y)

    def move_to(self, x, y):
        self.rect = self.image.get_rect(bottomright=(x, y))


def make():  # makes the tiles
    for i in range(cur_pos[0], c.WIDTH, SIZE):
        tiles.append([])  # puts the ground objects into the tiles list
        for j in range(cur_pos[1], c.WIDTH, SIZE):
            tmp_ground = Ground(i, j)
            group.add(tmp_ground)
            tiles[len(tiles) - 1].append(tmp_ground)


def move():  # moves the tiles
    # get tiles' offset from the camera
    cur_pos[0] = SIZE - c.cam_pos[0] % SIZE
    cur_pos[1] = c.cam_pos[1] % SIZE
    # reassigns tiles when they go out of range
    for i in range(cur_pos[0]+SIZE, c.WIDTH, SIZE):
        for j in range(cur_pos[1], c.WIDTH, SIZE):
            tiles[(i-cur_pos[0]) // SIZE][(j-cur_pos[1]) // SIZE].move_to(i, j)


def draw():  # draws all the ground tiles
    group.draw(c.screen)

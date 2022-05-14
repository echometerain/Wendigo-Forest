import pygame as pg
import config as c

cur_pos = [0, 0]  # current position
SIZE = 64 * c.IN_RATIO  # the ground file is 64px large
tiles = []
group = pg.sprite.Group()


class Ground(pg.sprite.Sprite()):
    def __init__(x, y):
        super().__init__()
        self.image = pg.image.load("sprites/ground.png").convert()
        pg.transform.scale(self.image, (SIZE, SIZE), c.screen)
        self.rect = self.image.get_rect(topleft=(x, y))

    def move_to(x, y):
        self.rect = self.image.get_rect(topleft=(x, y))


def make():
    for i in range(cur_pos[0], c.WIDTH, size):
        tiles.append([])
        for j in range(cur_pos[1], c.WIDTH, size):
            tmp_ground = ground(i, j)
            group.add(tmp_ground)
            tiles[len(tiles) - 1].append(tmp_ground)


def move():
    cur_pos[0] = c.pos[0] % SIZE
    cur_pos[1] = c.pos[1] % SIZE
    for i in range(cur_pos[0], c.WIDTH, size):
        for j in range(cur_pos[1], c.WIDTH, size):
            tiles[(i-cur_pos[0]) / size][(j-cur_pos[1]) / size].move_to(i, j)

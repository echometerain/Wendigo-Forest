############################
# Filename: player.py
# Desc: Manage player movement
# Date created: 04/22/2022
############################
import pygme as pg
import config as c


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super.__init__()

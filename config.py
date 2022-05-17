############################
# Filename: config.py
# Desc: Configuration
# Date created: 04/22/2022
############################
import pygame as pg
import math

pg.init()  # starts pygame and functions
pg.mixer.pre_init(44100, 16, 2, 4096)
pg.mixer.init()
pg.font.init()

screen = pg.display.set_mode(
    (0, 0), pg.HWSURFACE | pg.FULLSCREEN | pg.DOUBLEBUF, 16)
WIDTH, HEIGHT = pg.display.get_surface().get_size()  # screen width and height
IN_WIDTH, IN_HEIGHT = (448, 252)  # internal size
IN_RATIO = WIDTH / IN_WIDTH

# pg.display.set_icon(pg.image.load("sprites/icon.png").convert_alpha())
pg.display.set_caption("Wendigo Forest")

pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT, pg.USEREVENT])

clock = pg.time.Clock()

pos = [0, 0]
offset = [0, 0]
SPEED = 6
DIAG_SPEED = int(SPEED/math.sqrt(2))


def image(file):
    img = pg.image.load(f"sprites/{file}.png").convert_alpha()
    img = pg.transform.scale(
        img, (img.get_width()*IN_RATIO, img.get_height()*IN_RATIO))
    return img

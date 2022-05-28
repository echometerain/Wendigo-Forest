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
OFFSET_RAD = 100
SPEED = 6
pl_state = [4, False, 3]  # turn #, flip, running frame (4 is idle)
DIAG_SPEED = int(SPEED/math.sqrt(2))


def image(file):  # makes loading images with alpha
    img = pg.image.load(f"sprites/{file}.png").convert_alpha()
    img = pg.transform.scale(
        img, (img.get_width()*IN_RATIO, img.get_height()*IN_RATIO))
    return img


def move_anim(x, y, speed, diag_speed, anim_state):
    move = [0, 0]
    if x != 0 and y != 0:
        if x == -1:
            anim_state[1] = True
        elif x == 1:
            anim_state[1] = False
        if y == 1:
            anim_state[0] = 1
        else:
            anim_state[0] = 3
        move[0] = x * diag_speed
        move[1] = y * diag_speed
    else:
        if x == 1:
            anim_state[1] = False
            anim_state[0] = 2
        elif x == -1:
            anim_state[1] = True
            anim_state[0] = 2
        elif y == 1:
            anim_state[0] = 0
        else:
            anim_state[0] = 4
        move[0] = x * speed
        move[1] = y * speed
    return move, anim_state

############################
# Filename: config.py
# Desc: Configuration and startup
# Date created: 04/22/2022
############################
import pygame as pg
import math
import os

pg.init()  # starts pygame and functions
pg.mixer.pre_init(44100, 16, 2, 4096)  # start sound
pg.mixer.init()
pg.font.init()
pg.mouse.set_visible(False)  # disables mouse to draw crosshair

screen = pg.display.set_mode(
    (0, 0), pg.HWSURFACE | pg.FULLSCREEN | pg.DOUBLEBUF, 16)  # preformance improvements
WIDTH, HEIGHT = pg.display.get_surface().get_size()  # screen width and height
IN_WIDTH, IN_HEIGHT = (448, 252)  # internal size
IN_RATIO = WIDTH / IN_WIDTH

pg.display.set_icon(pg.image.load(
    "sprites/icon.png").convert_alpha())  # set icon
pg.display.set_caption("Wendigo Forest")

# preformance improvements
pg.event.set_allowed([pg.KEYDOWN, pg.QUIT, pg.MOUSEBUTTONDOWN])

clock = pg.time.Clock()

FPS = 50
cam_pos = [0, 0]  # camera position
OFFSET_RAD = 100  # how far can the player go off-center **2
NPC_CLOSE_RAD = 70  # how far the npc can go from the player **2
PL_SPEED = 12  # pixels per frame
NPC_SPEED = 10
WD_SPEED = 14
GUN_SPEED = 24

nomove_frames = [0]

s = os.sep  # linux use slashes, windows use backslashes
pg.mixer.music.load(f"sounds{s}music{s}opening.ogg")
pl_run = pg.mixer.Sound(f"sounds{s}sfx{s}player_run.ogg")
gun_sound = pg.mixer.Sound(f"sounds{s}sfx{s}gun1.ogg")

# obsolete run

# run_sounds = []
# for i in range(1, 4):
#     run_sounds.append([pg.mixer.Sound(f"sounds{s}sfx{s}run{i}.ogg"), False])

screams = []
for i in range(1, 6):
    screams.append(pg.mixer.Sound(f"sounds{s}sfx{s}scream{i}.ogg"))


def image(file):  # imports images with alpha
    img = pg.image.load(f"sprites/{file}.png").convert_alpha()
    img = pg.transform.scale(
        img, (img.get_width()*IN_RATIO, img.get_height()*IN_RATIO))
    return img


def image_no_alpha(file):  # imports images without alpha
    img = pg.image.load(f"sprites/{file}.png")
    img = pg.transform.scale(
        img, (img.get_width()*IN_RATIO, img.get_height()*IN_RATIO))
    return img

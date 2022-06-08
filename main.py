############################
# Filename: main.py
# Desc: Main game loop
# Date created: 04/22/2022
############################
import config as c
import pygame as pg
import ground
import player
import wd
import npc
import obst
import sys

black = c.image("black")
mask = c.image("mask")
ground.make()
pl = player.Player()
npc1 = npc.NPC()
all_sprites = pg.sprite.Group()
all_sprites.add(pl)
all_sprites.add(npc1)
font = pg.font.SysFont("Metal Macabre", 50)
red = (255, 0, 0)


def set_text(string, coordx, coordy, fontSize):  # Function to set text

    font = pg.font.SysFont("calibri", fontSize)
    text = font.render(string, True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return (text, textRect)


def next():  # updates frame
    pg.display.update()
    c.clock.tick(100)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            exit(0)
    pg.event.clear()


img_title = c.image("logo")
# c.screen, WIDTH, HEIGHT
while True:
    c.screen.blit(img_title, (c.WIDTH/4, c.HEIGHT/3))
    msg = font.render("Press any key to start.. ", True, red)
    c.screen.blit(msg, (0, 0))
    next()


def keys():
    x = 0
    y = 0
    keys = pg.key.get_pressed()  # x is always inverted for some reason
    if keys[pg.K_w]:
        y += 1
    if keys[pg.K_s]:
        y -= 1
    if keys[pg.K_a]:
        x -= 1
    if keys[pg.K_d]:
        x += 1
    pl.move(x, y)


def draw():
    ground.draw()
    all_sprites.draw(c.screen)
    npc1.check_move(pl)
    c.screen.blit(mask, (0, 0))
    c.screen.blit(black, (0, 0))
    txt = set_text(pl.anim_state.__str__(), 100, 100, 25)
    c.screen.blit(txt[0], txt[1])


while True:
    c.nomove_frames[0] += 1
    if c.nomove_frames[0] >= 10:
        c.nomove_frames[0] = 0
        pl.update()
        npc1.update()

    keys()
    ground.move()
    draw()
    next()

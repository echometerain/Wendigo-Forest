############################
# Filename: main.py
# Desc: Main game loop
# Date created: 04/22/2022
############################
import config as c
import pygame as pg
import random
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
npcs = []
sprites = [pl]
font = pg.font.SysFont("Metal Macabre", 50)


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


# img_title = c.image("logo")
# # c.screen, WIDTH, HEIGHT
# while True:
#     c.screen.blit(img_title, (c.WIDTH/4, c.HEIGHT/3))
#     msg = font.render("Press any key to start.. ", True, (128, 0, 0))
#     c.screen.blit(msg, ((c.WIDTH/5)*2 - 50, (c.HEIGHT/3)*2))
#     next()


def keys():
    x = 0
    y = 0
    keys = pg.key.get_pressed()
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
    sprites.sort(key=lambda x: x.pos[1], reverse=True)
    queue = pg.sprite.OrderedUpdates()
    for e in sprites:
        queue.add(e)
    queue.draw(c.screen)
    for e in npcs:
        e.check_move(pl)
    c.screen.blit(mask, (0, 0))
    c.screen.blit(black, (0, 0))


while True:
    c.nomove_frames[0] += 1
    if c.nomove_frames[0] >= 10:
        if random.randint(1, 20) == 1:
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)
            t = npc.NPC([x*1000+c.cam_pos[0], y*1000+c.cam_pos[1]])
            npcs.append(t)
            sprites.append(t)
        c.nomove_frames[0] = 0
        for e in sprites:
            e.update()
        pl.update()

    keys()
    ground.move()
    draw()
    next()

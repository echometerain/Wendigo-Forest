############################
# Filename: main.py
# Desc: Main game loop
# Date created: 04/22/2022
############################
import config as c
import pygame as pg
import os
import random
import ground
import player
import wd
import npc
import sys

pg.mouse.set_visible(False)
black = c.image("black")
cursor = c.image("crosshair")
cursor_rect = cursor.get_rect()
gray = c.image("mask")
ground.make()
pl = player.Player()
sprites = [pl]
npcs = []
wendigos = []
font = pg.font.Font("MetalMacabre.ttf", 50)
maroon = (128, 0, 0)
black = (0, 0, 0)
s = os.sep
openSFX = pg.mixer.Sound(f"sounds{s}music{s}opening.mp3")
openSFX.set_volume(0.5)
mask = pg.mask.from_surface(gray)


def set_text(font, string, coordx, coordy):  # Function to set text
    text = font.render(string, True, maroon)
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
while True:
    keys = pg.key.get_pressed()
    openSFX.play(0)
    if keys[pg.K_SPACE]:
        break
    c.screen.blit(img_title, (c.WIDTH/4, c.HEIGHT/3))
    txt = set_text(font, "Press space to start.. ",
                   c.WIDTH/2 + 50, c.HEIGHT/2 + 200)
    c.screen.blit(txt[0], txt[1])
    next()


def gun():
    True


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

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            gun()


def rmWd(w):
    if w in sprites:
        sprites.remove(w)
    if w in wendigos:
        wendigos.remove(w)


def rmNPC(e):
    if e in sprites:
        sprites.remove(e)
    if e in npcs:
        npcs.remove(e)


def draw():
    overlap = []
    ground.draw()
    c.screen.blit(gray, (0, 0))
    sprites.sort(key=lambda x: x.pos[1], reverse=True)
    queue = pg.sprite.OrderedUpdates()
    for e in sprites:
        queue.add(e)
    queue.draw(c.screen)
    for i, e in enumerate(npcs):
        e.check_move(pl)

    for w in wendigos:
        w.check_move(pl)
        for e in npcs:
            if w.rect.colliderect(e):
                rmNPC(e)
                # rmWd(w)
                wd.run = True
        if w.rect.colliderect(pl.rect):
            return True
    # if len(npcs) > 0:
    #     txt = set_text(npcs[0].anim_state.__str__(), 100, 100, 25)
    #     c.screen.blit(txt[0], txt[1])

    c.screen.blit(black, (0, 0))
    cursor_rect.center = pg.mouse.get_pos()
    c.screen.blit(cursor, cursor_rect)
    return False


def main():
    while True:
        c.nomove_frames[0] += 1
        if c.nomove_frames[0] >= 10:
            if random.randint(1, 30) == 1:
                x = random.randint(-1, 1)
                y = random.randint(-1, 1)
                t = npc.NPC([x*1000+c.cam_pos[0], y*1000+c.cam_pos[1]])
                npcs.append(t)
                sprites.append(t)
            if random.randint(1, 35) == 1:
                x = random.randint(-1, 1)
                y = random.randint(-1, 1)
                t = wd.Wendigo([x*1000+c.cam_pos[0], y*1000+c.cam_pos[1]])
                sprites.append(t)
                wendigos.append(t)
            c.nomove_frames[0] = 0
            for e in npcs:
                e.update()
            pl.update()

        keys()
        ground.move()
        ended = draw()
        if ended:
            break
        next()


def end():
    c.screen.fill((0, 0, 0))
    while True:
        keys = pg.key.get_pressed()
        openSFX.play(0)
        # anyKey()
        if keys[pg.K_SPACE]:
            break

        c.screen.blit(img_title, (c.WIDTH/4+25, c.HEIGHT/3))
        txt = set_text(font, "You died",
                       c.WIDTH/2 + 50, c.HEIGHT/2 + 200)
        c.screen.blit(txt[0], txt[1])
        txt = set_text(font, "Press space to continue",
                       c.WIDTH/2 + 50, c.HEIGHT/2 + 260)
        c.screen.blit(txt[0], txt[1])
        next()


while True:
    main()
    sprites = [pl]
    c.cam_pos[0] = 0
    c.cam_pos[1] = 0
    npcs = []
    wendigos = []
    pl.pos = [0, 0]
    end()

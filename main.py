############################
# Filename: main.py
# Desc: Main game loop
# Date created: 04/22/2022
############################
import config as c
import pygame as pg
import time
import os
import sys
import remains
import random
import ground
import player
import wd
import npc
import gun

black = c.image("black")
cursor = c.image("crosshair")
cursor_rect = cursor.get_rect()
gray = c.image("mask")
ground.make()
pl = player.Player()
sprites = [pl]
npcs = []
wendigos = []
carnage = []
bullets = []
font = pg.font.Font("MetalMacabre.ttf", 50)
cali = pg.font.SysFont("calibri", 50)
maroon = (128, 0, 0)
s = os.sep
pg.mixer.music.load(f"sounds{s}music{s}opening.mp3")
pg.mixer.music.set_volume(0.5)
mask = pg.mask.from_surface(gray)
gun_time = time.time()


def set_text(font, string, coordx, coordy):  # Function to set text
    text = font.render(string, True, maroon)
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return (text, textRect)


def next():  # updates frame
    global gun_time
    pg.display.update()
    c.clock.tick(c.FPS)
    temp_time = time.time()
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            #gun_time = temp_time
            bullets.append(gun.Gun(pl.pos[0], pl.pos[1]))
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            exit(0)
    pg.event.clear()


img_title = c.image("logo2")
pg.mixer.music.play(-1)
while True:

    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        break
    c.screen.blit(img_title, (c.WIDTH/4, c.HEIGHT/3))
    txt = set_text(font, "Press space to start.. ",
                   c.WIDTH/2 + 50, c.HEIGHT/2 + 200)
    c.screen.blit(txt[0], txt[1])
    next()


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


def logic():
    global sprites
    global bullets
    global wendigos
    global npcs
    ground.move()
    for e in carnage:
        e.re_position()
    for e in bullets:
        e.move()
        for n in npcs:
            if n.hitbox.collidepoint(e.screen_pos[0], e.screen_pos[1]):
                carnage.append(remains.Remains(n.pos[0], n.pos[1], "npc"))
                e.rm = True
                n.rm = True
        for w in wendigos:
            if w.hitbox.collidepoint(e.screen_pos[0], e.screen_pos[1]):
                carnage.append(remains.Remains(w.pos[0], w.pos[1], "wd"))
                e.rm = True
                w.rm = True
    for i, e in enumerate(npcs):
        e.check_move(pl)

    for w in wendigos:
        w.check_move(pl)
        for e in npcs:
            if w.hitbox.colliderect(e.hitbox):
                e.rm = True
                w.run = True
        if w.hitbox.colliderect(pl.hitbox):
            return True

    bullets = [x for x in bullets if not x.rm]
    sprites = [x for x in sprites if not x.rm]
    wendigos = [x for x in wendigos if not x.rm]
    npcs = [x for x in npcs if not x.rm]
    bullets = [x for x in bullets if not x.rm]


def draw():
    global sprites
    global bullets
    global wendigos
    global npcs
    ground.draw()
    for e in carnage:
        c.screen.blit(e.image, e.rect)
    c.screen.blit(gray, (0, 0))
    sprites.sort(key=lambda x: x.pos[1], reverse=True)
    ysort = pg.sprite.OrderedUpdates()
    for e in sprites:
        ysort.add(e)
        # pg.draw.rect(c.screen, (255, 0, 0), e.hitbox)
    ysort.draw(c.screen)
    for e in bullets:
        pg.draw.line(c.screen, (255, 255, 0), (e.screen_pos[0], e.screen_pos[1]),
                     (e.screen_pos[0]+e.vector[0], e.screen_pos[1]-e.vector[1]))
    c.screen.blit(black, (0, 0))
    cursor_rect.center = pg.mouse.get_pos()
    c.screen.blit(cursor, cursor_rect)
    # if len(bullets) > 0:
    #     txt = set_text(
    #         cali, bullets[len(bullets)-1].screen_pos.__str__(), 200, 100)
    #     c.screen.blit(txt[0], txt[1])
    return False


def spawn():
    if random.randint(1, 30) == 1:
        x = random.randint(-1, 1)
        y = random.randint(-1, 1)
        t = npc.NPC([x*c.WIDTH//2+c.cam_pos[0], y*c.HEIGHT//2+c.cam_pos[1]])
        npcs.append(t)
        sprites.append(t)
    if random.randint(1, 50) == 1:
        x = random.randint(-1, 1)
        y = random.randint(-1, 1)
        t = wd.Wendigo([x*c.WIDTH//2+c.cam_pos[0], y*c.HEIGHT//2+c.cam_pos[1]])
        sprites.append(t)
        wendigos.append(t)
    c.nomove_frames[0] = 0


def main():
    while True:

        c.nomove_frames[0] += 1
        if c.nomove_frames[0] >= 5:
            print(len(bullets))
            spawn()
            for e in npcs:
                e.update()
            pl.update()

        keys()
        ended = logic()
        if ended:
            break
        draw()
        next()


def end():
    c.screen.fill((0, 0, 0))
    while True:
        keys = pg.key.get_pressed()
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
    carnage = []
    pl.pos[0] = 0
    pl.pos[1] = 0
    pl.re_position()
    end()

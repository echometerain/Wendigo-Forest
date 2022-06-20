############################
# Filename: main.py
# Desc: Main game loop
# Date created: 04/22/2022
############################
import config as c
import pygame as pg
import time
import sys
import remains
import random
import ground
import player
import wd
import npc
import gun

black = c.image("black")  # non viewable area
cursor = c.image("crosshair")
cursor_rect = cursor.get_rect()
gray = c.image("mask")  # grey area
ground.make()  # makes the infinitely generating ground
pl = player.Player()
sprites = [pl]
npcs = []
wendigos = []
carnage = []
bullets = []
font = pg.font.Font("MetalMacabre.ttf", 50)
cali = pg.font.SysFont("calibri", 50)
maroon = (128, 0, 0)
pg.mixer.music.set_volume(0.5)
gun_time = time.time()  # gun cooldown


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
        # works best when here, still doesn't work sometimes somehow
        if event.type == pg.MOUSEBUTTONDOWN and temp_time-gun_time > 0.5 and pl.ammo_count > 0:
            gun_time = temp_time
            bullets.append(gun.Gun(pl.pos[0], pl.pos[1]))
            pl.ammo_count -= 1
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            exit(0)
    pg.event.clear()


# start screen
img_title = c.image("logo2")
pg.mixer.music.play(-1, 0, 500)  # play on loop
while True:

    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        break
    c.screen.blit(img_title, (c.WIDTH/4, c.HEIGHT/3))
    txt = set_text(font, "Press space to start.. ",
                   c.WIDTH/2 + 50, c.HEIGHT/2 + 200)
    c.screen.blit(txt[0], txt[1])
    next()


def keys():  # interprets wasd player movement
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


def logic():  # most of the game logic
    global sprites  # I just call global when it doesn't work
    global bullets
    global wendigos
    global npcs
    ground.move()
    for e in carnage:  # moves the remains of entities
        e.re_position()
    for e in bullets:
        e.move()  # move bullet
        for n in npcs:  # check bullet kill npc
            if n.hitbox.collidepoint(e.screen_pos[0], e.screen_pos[1]):
                carnage.append(remains.Remains(n.pos[0], n.pos[1], "npc"))
                e.rm = True
                n.rm = True
        for w in wendigos:  # check bullet kill wendigo
            if w.hitbox.collidepoint(e.screen_pos[0], e.screen_pos[1]):
                carnage.append(remains.Remains(w.pos[0], w.pos[1], "wd"))
                e.rm = True
                w.rm = True
    for i, e in enumerate(npcs):  # npc-to-npc collision and move
        collide = False
        for e2 in npcs[i+1:]:
            if e.hitbox.colliderect(e2.hitbox):
                collide = True
                break
        if not collide:
            e.check_move(pl)

    for i, w in enumerate(wendigos):  # wendigo move and kill
        collide = False
        for e2 in wendigos[i+1:]:  # wendigo-to-wendigo collision
            if w.hitbox.colliderect(e2.hitbox):
                collide = True
                break
        if not collide:
            w.check_move(pl)
        for e in npcs:  # check kill npc
            if w.hitbox.colliderect(e.hitbox):
                e.rm = True
                w.run = True  # wendigo goes into "run away" mode
                rand = random.randint(0, 5)
                if rand < len(c.screams):
                    c.screams[rand].play()
        if w.hitbox.colliderect(pl.hitbox):
            return True  # check kill you

    # the dumbest memory manager
    # guess it's not dumb if it works
    bullets = [x for x in bullets if not x.rm]
    sprites = [x for x in sprites if not x.rm]
    wendigos = [x for x in wendigos if not x.rm]
    npcs = [x for x in npcs if not x.rm]
    bullets = [x for x in bullets if not x.rm]


def draw():
    global sprites  # same
    global bullets
    global wendigos
    global npcs
    ground.draw()
    for e in carnage:  # draws remains
        c.screen.blit(e.image, e.rect)
    c.screen.blit(gray, (0, 0))  # draws gray area
    sprites.sort(key=lambda x: x.pos[1], reverse=True)
    ysort = pg.sprite.OrderedUpdates()  # sorts sprite draw order based on y-position
    for e in sprites:
        ysort.add(e)
    ysort.draw(c.screen)  # draw sprites
    for e in bullets:  # draw bullets
        pg.draw.line(c.screen, (255, 255, 0), (e.screen_pos[0], e.screen_pos[1]),
                     (e.screen_pos[0]+e.vector[0], e.screen_pos[1]-e.vector[1]))
    c.screen.blit(black, (0, 0))  # draws non-viewable area
    cursor_rect.center = pg.mouse.get_pos()
    c.screen.blit(cursor, cursor_rect)  # draws cursor
    txt = set_text(font, str(pl.ammo_count), c.WIDTH//2-20, 75)
    c.screen.blit(txt[0], txt[1])  # draw ammo amount
    return False


def spawn():
    if random.randint(1, 30) == 1:  # spawns every 3 seconds on average
        x = random.randint(-1, 1)
        y = random.randint(-1, 1)  # spawns it just outside the screen
        pos = [x*c.WIDTH//2+c.cam_pos[0], y*c.HEIGHT//2+c.cam_pos[1]]
        if random.randint(0, 2) == 1:  # I don't need to use == but uhhhh
            t = wd.Wendigo(pos)
            wendigos.append(t)
        else:
            t = npc.NPC(pos)
            npcs.append(t)
        sprites.append(t)


def main():  # main game loop
    c.pl_run.play(-1)
    while True:
        # animations only update at 10 fps instead of 50
        c.nomove_frames[0] += 1
        if c.nomove_frames[0] >= 5:
            c.nomove_frames[0] = 0
            spawn()
            for e in npcs:  # draws you and all the npcs
                e.update()
            pl.update()
        keys()
        ended = logic()  # check whether you're dead
        if ended:
            break
        draw()
        next()
    c.pl_run.stop()


def end():  # end screen
    c.screen.fill((0, 0, 0))
    while True:
        keys = pg.key.get_pressed()
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


while True:  # meta game loop
    main()

    # resets the game state
    sprites = [pl]
    c.cam_pos[0] = 0
    c.cam_pos[1] = 0
    npcs = []
    wendigos = []
    carnage = []
    pl.pos[0] = 0
    pl.pos[1] = 0
    pl.re_position()
    pl.ammo_count = 3

    end()

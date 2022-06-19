############################
# Filename: entity.py
# Desc: Abstract class for npc, player, and wendigo
# Date created: 05/29/2022
############################
import pygame as pg
import config as c


class Entity(pg.sprite.Sprite):
    rm = False  # whether entity should be deleted
    hitbox: pg.Rect
    moving = True
    dir_images = 0  # images per direction
    anim_state = [4, False, 3]  # turn number, flip, running frame (3 is idle)
    pos = [0, 0]  # in-game position, not screen position
    speed = 0
    diag_speed = 0  # diagonal speed

    # constructor
    def __init__(self, sheet, numImages, dir_images, speed, pos, hitbox_w, hitbox_h):
        super().__init__()
        self.pos = pos
        self.hitbox = pg.Rect(0, 0, hitbox_w, hitbox_h)
        self.spritesheet = c.image(sheet)
        self.rect = self.spritesheet.get_rect()
        self.sheetWidth = self.rect.width
        self.numImages = numImages
        self.rect.width = self.sheetWidth//numImages
        self.speed = speed
        self.dir_images = dir_images
        self.diag_speed = int(speed/1.414)  # sqrt 2
        self.update()
        self.re_position()

    def get_anim(self):  # get spritesheet animation frame
        return (self.anim_state[0]*self.dir_images)+self.anim_state[2]+1
        # +1 is needed here to not glitch the spritesheet clip

    def update(self):  # updates animation
        self.spritesheet.set_clip(
            self.rect.width*self.get_anim(), 0, self.rect.width, self.rect.height)
        self.image = self.spritesheet.subsurface(self.spritesheet.get_clip())
        if self.anim_state[1]:  # flips image
            self.image = pg.transform.flip(self.image, True, False)
        if self.anim_state[2] < 0:  # loop through animations frames
            self.anim_state[2] = 4
        self.anim_state[2] -= 1

    def re_position(self):  # converts in-game position to screen position
        self.rect = self.image.get_rect(
            center=(c.WIDTH//2-(c.cam_pos[0]-self.pos[0]), c.HEIGHT//2+(c.cam_pos[1]-self.pos[1])))
        # hitbox is always centered
        self.hitbox.center = (self.rect.center[0], self.rect.center[1])

    def move_anim(self, x, y):  # draws animation
        move = [0, 0]
        # sprite directions (anim_state[0])
        # 0. up
        # 1. diagonal up
        # 2. horizontal
        # 3. diagonal down
        # 4. down
        if (x != 0) and (y != 0):
            if x == -1:
                self.anim_state[1] = True  # flips spirte
            else:
                self.anim_state[1] = False
            if y == 1:
                self.anim_state[0] = 1
            else:
                self.anim_state[0] = 3
            move[0] = x * self.diag_speed
            move[1] = y * self.diag_speed
        else:
            if x != 0:
                self.anim_state[0] = 2
                if x == 1:
                    self.anim_state[1] = False
                else:
                    self.anim_state[1] = True
            elif y == 1:
                self.anim_state[1] = False
                self.anim_state[0] = 0
            else:
                self.anim_state[1] = False
                self.anim_state[0] = 4
            move[0] = x * self.speed
            move[1] = y * self.speed
        return move

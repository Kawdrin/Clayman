from pygame import Rect
from pygame.sprite import Sprite, spritecollide
from pygame.transform import scale, flip
from pygame.locals import K_a, K_w, K_s, K_d
from pygame.key import get_pressed

from src.sprite_sheet import SpriteSheet
from src.groups import colisionsGroup, EntidadesGroup


class Hero(Sprite):
    def __init__(self, pos,*groups):
        super().__init__(*groups)
        spr = SpriteSheet("res/CreyMan.png")
        self.rect = Rect(pos[0], pos[1], 32, 32)
        self.idle_sprites = [
            scale(spr.clip_sprite(16, 16, 16, 16), (32, 32)),
            scale(spr.clip_sprite(32, 16, 16, 16), (32, 32)),
            scale(spr.clip_sprite(48, 16, 16, 16), (32, 32)),
            scale(spr.clip_sprite(64, 16, 16, 16), (32, 32))]

        self.run_sprites = [
            scale(spr.clip_sprite(16, 32, 16, 16), (32, 32)),
            scale(spr.clip_sprite(32, 32, 16, 16), (32, 32)),
            scale(spr.clip_sprite(48, 32, 16, 16), (32, 32)),
            scale(spr.clip_sprite(48, 32, 16, 16), (32, 32)),
            scale(spr.clip_sprite(32, 32, 16, 16), (32, 32)),
            scale(spr.clip_sprite(16, 32, 16, 16), (32, 32))]

        self.grab_item_idle_sprite = [
            scale(spr.clip_sprite(80, 16, 16, 16), (32, 32)),
            scale(spr.clip_sprite(96, 16, 16, 16), (32, 32)),
            scale(spr.clip_sprite(112, 16, 16, 16), (32, 32)),
            scale(spr.clip_sprite(128, 16, 16, 16), (32, 32))]

        self.grab_item_run_sprites = [
            scale(spr.clip_sprite(304, 16, 16, 16), (32, 32)),
            scale(spr.clip_sprite(320, 16, 16, 16), (32, 32)),
            scale(spr.clip_sprite(336, 16, 16, 16), (32, 32)),
            scale(spr.clip_sprite(336, 16, 16, 16), (32, 32)),
            scale(spr.clip_sprite(320, 16, 16, 16), (32, 32)),
            scale(spr.clip_sprite(304, 16, 16, 16), (32, 32))]

        self.hitbox = Sprite()
        self.hitbox.rect = Rect(self.rect.x+8, self.rect.y+16, 14, 16)


        self.pos_x = [True, True]
        self.pos_y = [True, True]
        self.sprite_change = 0
        self.current_sprites = self.idle_sprites

        self.flipped = False

        self.item_grab = False
        self.item = None

        self.parar = 3

        self.image = self.idle_sprites[0]

    def colision_check(self):
        for bloco in spritecollide(self.hitbox, colisionsGroup, False):
            if self.hitbox.rect.bottom- bloco.rect.top == 2:
                self.hitbox.rect.bottom = bloco.rect.top
                self.pos_y = [False, True]
                self.pos_x = [True, True]

            if bloco.rect.bottom - self.hitbox.rect.top == 2:
                self.hitbox.rect.top = bloco.rect.bottom
                self.pos_y = [True, False]
                self.pos_x = [True, True]

            if self.hitbox.rect.right - bloco.rect.left == 2:
                self.hitbox.rect.right = bloco.rect.left
                self.pos_x = [False, True]
                self.pos_y = [True, True]

            if bloco.rect.right - self.hitbox.rect.left == 2:
                self.hitbox.rect.left = bloco.rect.right
                self.pos_x = [True, False]
                self.pos_y = [True, True]

            self.rect.x = self.hitbox.rect.x - 8
            self.rect.y = self.hitbox.rect.y - 16


    def soltar_item(self):
        if self.item_grab:
            self.item_grab = False
            self.item.grab = False
            self.item.rect.y = self.hitbox.rect.top+11

    def grab_item(self):
        if self.item_grab == False:
            for item in spritecollide(self.hitbox, EntidadesGroup, False):
                if item == self:
                    continue
                self.item_grab = True
                self.item = item
                item.grab = not item.grab
                break

    def move(self, keys):
        if keys[K_a] and self.pos_x[1]:
            self.rect.x -= 2
            self.flipped = True
            self.parar = 3
        if keys[K_s] and self.pos_y[0]:
            self.rect.y += 2
            self.parar = 3
        if keys[K_w] and self.pos_y[1]:
            self.rect.y -= 2
            self.parar = 3
        if keys[K_d] and self.pos_x[0]:
            self.rect.x += 2
            self.flipped = False
            self.parar = 3

        self.hitbox.rect.x = self.rect.x+8
        self.hitbox.rect.y = self.rect.y+16

    def update(self):
        if self.item_grab:
            self.item.equanto_pego(self)

        self.move(get_pressed())

        if self.parar == 3:
            if self.item_grab:
                self.current_sprites = self.grab_item_run_sprites
            else:
                self.current_sprites = self.run_sprites

        self.sprite_change += 0.1
        self.parar -= 0.5


        if self.parar <= 0:
            if self.item_grab:
                self.current_sprites = self.grab_item_idle_sprite
            else:
                self.current_sprites = self.idle_sprites

        if self.sprite_change >= len(self.current_sprites):
            self.sprite_change = 0

        self.image = flip(self.current_sprites[int(self.sprite_change)], self.flipped, False)

        self.pos_x = [True, True]
        self.pos_y = [True, True]

        self.colision_check()

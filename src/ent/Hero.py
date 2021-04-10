from arcade import Sprite, load_texture

from PIL import Image

class Hero(Sprite):
    def __init__(self):
        super().__init__()
        spritesheet = "res/CreyMan.png"
        self.position = [32*7, 32*6]
        self.idle_sprites = [load_texture(spritesheet, 16, 16, 16, 16), load_texture(spritesheet, 32, 16, 16, 16),
                             load_texture(spritesheet, 48, 16, 16, 16), load_texture(spritesheet, 64, 16, 16, 16)]

        self.run_sprites = [load_texture(spritesheet, 16, 32, 16, 16), load_texture(spritesheet, 32, 32, 16, 16),
                            load_texture(spritesheet, 48, 32, 16, 16), load_texture(spritesheet, 48, 32, 16, 16),
                            load_texture(spritesheet, 32, 32, 16, 16), load_texture(spritesheet, 16, 32, 16, 16)]

        self.run_sprites_flipped = [load_texture(spritesheet, 16, 32, 16, 16, flipped_horizontally = True), load_texture(spritesheet, 32, 32, 16, 16, flipped_horizontally = True),
                            load_texture(spritesheet, 48, 32, 16, 16, flipped_horizontally = True), load_texture(spritesheet, 48, 32, 16, 16, flipped_horizontally = True),
                            load_texture(spritesheet, 32, 32, 16, 16, flipped_horizontally = True), load_texture(spritesheet, 16, 32, 16, 16, flipped_horizontally = True)]

        self.texture = self.idle_sprites[0]
        self.scale = 2
        self.current_sprite_list = self.idle_sprites
        self.flipped = False
        self.current_sprite = 0
        self.velocity = 2
        self.parar = 2

        self.hitbox = Sprite(center_x = self.center_x, center_y = self.center_y)
        self.hitbox.texture = load_texture(spritesheet, 19, 72, 8,8)
        self.hitbox.scale= 2

        self.controle = {97:False, 119:False, 115:False, 100:False}
        self.pos_x = [True, True]
        self.pos_y = [True, True]

    def verifica_colisao(self, controle):
        from src.Groups import ForegroundGroup
        for wall in self.hitbox.collides_with_list(ForegroundGroup):
            if wall.top - self.hitbox.bottom == 2:
                self.hitbox.bottom = wall.top
                self.pos_x = [True, True]
                self.pos_y = [False, True]

            if self.hitbox.top - wall.bottom == 2:
                self.hitbox.top = wall.bottom
                self.pos_x = [True, True]
                self.pos_y = [True, False]
            if self.hitbox.right - wall.left == 2:
                self.hitbox.right = wall.left
                self.pos_x = [False, True]
                self.pos_y = [True, True]
            if wall.right - self.hitbox.left == 2:
                self.hitbox.left = wall.right
                self.pos_x = [True, False]
                self.pos_y = [True, True]

            self.center_x = self.hitbox.center_x
            self.center_y = self.hitbox.center_y+8

    def movimento(self):
        if self.controle[97] and self.pos_x[1]:
            self.center_x -= self.velocity
            self.flipped = True
            self.flip(self.run_sprites, self.run_sprites_flipped)
            self.parar = 3

        if self.controle[119] and self.pos_y[1]:
            self.center_y += self.velocity
            self.flip(self.run_sprites, self.run_sprites_flipped)
            self.parar = 3

        if self.controle[115] and self.pos_y[0]:
            self.center_y -= self.velocity
            self.flip(self.run_sprites, self.run_sprites_flipped)
            self.parar = 3

        if self.controle[100] and self.pos_x[0]:
            self.center_x += self.velocity
            self.flipped = False
            self.flip(self.run_sprites, self.run_sprites_flipped)
            self.parar = 3

        self.hitbox.set_position(self.center_x, self.center_y-8)

    def flip(self, sprite_list, sprite_list_flipped):
        if self.flipped:
            self.current_sprite_list = sprite_list_flipped
        else:
            self.current_sprite_list = sprite_list

    def update(self):
        self.current_sprite += 0.1
        self.parar -= 0.5

        if self.current_sprite >= len(self.current_sprite_list):
            self.current_sprite = 0

        self.texture = self.current_sprite_list[int(self.current_sprite)]

        if self.parar <= 0:
            self.current_sprite_list = self.idle_sprites

        self.movimento()
        self.pos_x = [True, True]
        self.pos_y = [True, True]
        self.verifica_colisao(self.controle)

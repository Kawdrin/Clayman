from pygame import Rect
from pygame.sprite import Sprite
from pygame.transform import scale

from src.sprite_sheet import SpriteSheet

class Argila(Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        sprite_sheet = SpriteSheet("res/CreyMan.png")
        self.image = scale(sprite_sheet.clip_sprite(72, 48, 8, 8), (16, 16))
        self.rect = Rect(x+8, y+8, 16, 16)
        self.grab = False

    def equanto_pego(self, pos):
        if self.grab:
            self.rect.x = pos.rect.x + 8
            self.rect.y = pos.rect.y - 11

    def update(self):
        ...

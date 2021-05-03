from pygame import Surface
from pygame.locals import SRCALPHA
from pygame.image import load

class SpriteSheet:
    def __init__(self, img):
        self.img = load(img)

    def clip_sprite(self, x, y, largura, altura):
        forma = Surface((largura, altura), SRCALPHA)
        forma.blit(self.img, (0,0), (x, y, largura, altura))
        return forma

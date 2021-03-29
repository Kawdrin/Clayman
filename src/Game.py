from arcade import Window

from src.Groups import HeroGroup

from pyglet.gl import glTexParameteri, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_2D, GL_NEAREST, GL_TEXTURE_MAG_FILTER

def cooked_resolution_draw(sprite):
    sprite.draw()

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)


class Game(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_update(self, dt):
        HeroGroup.update()

    def on_draw(self):
        cooked_resolution_draw(HeroGroup)

from arcade import Window

from src.Groups import BackgroundGroup, ForegroundGroup, HighgroundGroup

from src.ent.Hero import Hero

from pyglet.gl import glTexParameteri, GL_TEXTURE_MIN_FILTER, GL_TEXTURE_2D, GL_NEAREST, GL_TEXTURE_MAG_FILTER

def cooked_resolution_draw(sprite):
    sprite.draw()

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

class Game(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Hero = Hero()

    def on_key_press(self, key, mod):
        self.Hero.controle[key] = True

    def on_key_release(self, key, mod):
        self.Hero.controle[key] = False

    def on_update(self, dt):
        self.Hero.update()

    def on_draw(self):
        cooked_resolution_draw(BackgroundGroup)
        cooked_resolution_draw(ForegroundGroup)
        cooked_resolution_draw(self.Hero)
        cooked_resolution_draw(HighgroundGroup)

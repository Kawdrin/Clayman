from arcade import Sprite, load_texture



class Hero(Sprite):
    def __init__(self):
        super().__init__()
        spritesheet = "res/CreyMan.png"
        self.position = [330, 300]
        self.idle_sprites = [load_texture(spritesheet, 17, 16, 13, 16), load_texture(spritesheet, 33, 16, 13, 16),
                             load_texture(spritesheet, 49, 16, 13, 16), load_texture(spritesheet, 65, 16, 13, 16)]
        self.texture = self.idle_sprites[0]
        self.run_sprites = []
        self.scale = 4
        self.current_sprite = 0

    def update(self):
        self.current_sprite += 0.1
        if self.current_sprite >= len(self.idle_sprites):
            self.current_sprite = 0
        self.texture = self.idle_sprites[int(self.current_sprite)]

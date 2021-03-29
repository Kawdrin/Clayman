from arcade import load_texture, Sprite

class Map:
    def __init__(self):
        self.levels = [load_texture("res/CreyMan.png", 128, 16, 16,16)]
        self.tiles = {'Bloco': load_texture("res/CreyMan.png", 96, 48, 16,16),
                      "Wall":load_texture("res/CreyMan.png", 112, 48, 16,16)}
        self.list = []

    def create_level(self, level_number):
        level = self.levels[level_number]
        for y in range(0, 16):
            for x in range(0, 16):
                if level.image.getpixel(xy=(x,y)) == (0,0,0,255):
                    self.list.append(self.colocar_bloco("Bloco", x, y))
                if level.image.getpixel(xy=(x,y)) == (255,255,255,255):
                    self.list.append(self.colocar_bloco("Wall", x,y))
        return self.list

    def colocar_bloco(self, bloco_name, x, y):
        bloco = Sprite(center_x=x*64, center_y=y*64)
        bloco.scale = 4
        bloco.texture = self.tiles[bloco_name]
        return bloco

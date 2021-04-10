from arcade import load_texture, Sprite

class Map:
    def __init__(self):
        self.levels = [load_texture("res/CreyMan.png", 126, 14, 20,20)]
        self.tiles = {'Bloco': load_texture("res/CreyMan.png", 96, 48, 16,16),
                      'bloco_7': load_texture("res/CreyMan.png", 128, 80,16, 16),
                      'bloco_8': load_texture("res/CreyMan.png", 144, 80, 16, 16),
                      'bloco_9': load_texture("res/CreyMan.png", 160, 80,16, 16),
                      'bloco_verde': load_texture("res/CreyMan.png", 208, 80,16, 16),
                      "Wall":load_texture("res/CreyMan.png", 80, 96, 16,16),
                      "Wall_full":load_texture("res/CreyMan.png", 96, 80, 16,16)}

    def create_level(self, level_number, list_tiles):
        lista_sprites = []
        level = self.levels[level_number]
        for y in range(0, 20):
            for x in range(0, 20):
                if level.image.getpixel(xy=(x,y)) == (0,0,0,255) and "Bloco" in list_tiles:
                    lista_sprites.append(self.colocar_bloco("Bloco", x, y))
                if level.image.getpixel(xy=(x,y)) == (255,255,255,255)and "Wall" in list_tiles:
                    lista_sprites.append(self.colocar_bloco("Wall", x,y))
                if level.image.getpixel(xy=(x,y)) == (158,38,68,255)and "bloco_7" in list_tiles:
                    lista_sprites.append(self.colocar_bloco("bloco_7", x,y))
                if level.image.getpixel(xy=(x,y)) == (135,29,80,255)and "bloco_8" in list_tiles:
                    lista_sprites.append(self.colocar_bloco("bloco_8", x,y))
                if level.image.getpixel(xy=(x,y)) == (181,50,53,255)and "bloco_9" in list_tiles:
                    lista_sprites.append(self.colocar_bloco("bloco_9", x,y))
                if level.image.getpixel(xy=(x,y)) == (39,55,69,255)and "bloco_verde" in list_tiles:
                    lista_sprites.append(self.colocar_bloco("bloco_verde", x,y))
                if level.image.getpixel(xy=(x,y)) == (0,0,255,255)and "Wall_full" in list_tiles:
                    lista_sprites.append(self.colocar_bloco("Wall_full", x,y))

        return lista_sprites

    def colocar_bloco(self, bloco_name, x, y):
        bloco = Sprite(center_x=x*32+16, center_y=640-(y*32+16))
        bloco.scale = 2
        bloco.texture = self.tiles[bloco_name]
        return bloco

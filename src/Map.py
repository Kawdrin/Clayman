from arcade import load_texture, Sprite
import json

class Map:
    def __init__(self):
        with open("res/map/NewLevel0.json", "r") as mapa_novo:
            self.mapa_atual = json.load(mapa_novo)

        self.layers = len(self.mapa_atual["layers"])

    def entidades(self):
        ...

    def tile(self, lista, mapa):
        index_item = 0
        for item in mapa:
            index_item += 1
            if item == [-1]:
                continue

            y = index_item // 21 -1
            x = index_item % 21

            bloco = Sprite(center_x=x*32+16, center_y=640-(y*32+16))
            bloco.texture = load_texture("res/CreyMan.png", item[0]*16, item[1]*16, 16, 16)
            bloco.scale = 2

            lista.append(bloco)
        return lista

    def grid(self):
        ...

    def create_level(self, level_number, name):
        lista_sprites = []
        for layer in self.mapa_atual["layers"]:
            if "dataCoords" in layer and name == layer["name"]:
                lista_sprites = self.tile(lista_sprites, layer["dataCoords"])
            elif "grid" in layer:
                mapa = layer["grid"]

        return lista_sprites

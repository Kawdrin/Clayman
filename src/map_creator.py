from pygame import Rect
from pygame.sprite import Sprite
from pygame.transform import scale

import json

from src.sprite_sheet import SpriteSheet


class OgmoMap:
    def __init__(self, level, tilemap_file):
        with open(level, "r") as mapa_novo:
            self.mapa_atual = json.load(mapa_novo)

        self.tilemap_level = SpriteSheet("res/CreyMan.png")


    def create_tile(self, layer_id, group):
        layer_level = self.mapa_atual["layers"][layer_id]
        index_item = -1
        for celula in layer_level["dataCoords"]:
            index_item += 1
            if celula == [-1]:
                continue

            y = index_item // layer_level["gridCellsY"]
            x = index_item % layer_level["gridCellsX"]
            celula_bloco = Sprite(group)
            celula_bloco.image = scale(self.tilemap_level.clip_sprite(celula[0]*16, celula[1]*16, 16, 16), (32, 32))
            celula_bloco.rect = Rect(x*32, y*32, 32, 32)

    def create_grid(self, layer_id, group):
        layer_level = self.mapa_atual["layers"][layer_id]
        index_item = -1
        for celula in layer_level["grid"]:
            index_item += 1
            if celula == '0':
                continue

            y = index_item // layer_level["gridCellsY"]
            x = index_item % layer_level["gridCellsX"]
            celula_bloco = Sprite(group)
            celula_bloco.image = scale(self.tilemap_level.clip_sprite(0, 0, 16, 16), (32, 32))
            celula_bloco.rect = Rect(x*32, y*32, 32 ,32)

    def spawn_entities(self, layer_id, group, scale=1):
        from src.ent.hero import Hero
        from src.ent.argila import Argila
        entidades = self.mapa_atual["layers"][layer_id]["entities"]
        for ent in entidades:
            if ent["name"] == "Argila":
                Argila(ent["x"]*scale, ent["y"]*scale, group)

    def get_pos_entitie(self, name_entitie, layer_id, scale=1):
        from src.ent.hero import Hero
        entidades = self.mapa_atual["layers"][layer_id]["entities"]
        for ent in entidades:
            if ent["name"] == name_entitie:
                return (ent["x"]*scale, ent["y"]*scale)
        return (0, 0)

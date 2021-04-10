from arcade import SpriteList

from src.ent.Hero import Hero
from src.Map import Map

Mapa = Map()
BackgroundGroup = SpriteList(is_static=True)
BackgroundGroup.extend(Mapa.create_level(0, ["Bloco", 'bloco_7','bloco_8', 'bloco_9', 'bloco_verde']))

ForegroundGroup = SpriteList(is_static=True)
ForegroundGroup.extend(Mapa.create_level(0, ["Wall"]))

HighgroundGroup = SpriteList(is_static=True)
HighgroundGroup.extend(Mapa.create_level(0, ["Wall_full"]))

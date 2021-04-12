from arcade import SpriteList

from src.ent.Hero import Hero
from src.Map import Map

Mapa = Map()
BackgroundGroup = SpriteList(is_static=True)
BackgroundGroup.extend(Mapa.create_level(0, "Back"))

ForegroundGroup = SpriteList(is_static=True)
ForegroundGroup.extend(Mapa.create_level(0, "Fore"))

HighgroundGroup = SpriteList(is_static=True)
HighgroundGroup.extend(Mapa.create_level(0, "High"))

ColisionGroup = 0
DetalhesGroup = 0
EntsGroup = 0

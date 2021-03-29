from arcade import SpriteList

from src.ent.Hero import Hero
from src.Map import Map

HeroGroup = SpriteList()
HeroGroup.append(Hero())
Mapa = Map()
BackgroundGroup = SpriteList(is_static=True)
BackgroundGroup.extend(Mapa.create_level(0))
ForegroundGroup = SpriteList()

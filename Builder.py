from src.Game import Game
from arcade import run

engine = Game(640,640, "ClayMan", update_rate=1/60)
run()

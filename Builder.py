from arcade import run

from src.Game import Game

engine = Game(640,640, "ClayMan", update_rate=1/60)
run()

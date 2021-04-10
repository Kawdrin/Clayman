from arcade import run
from src import Game

if __name__ == "__main__":
    engine = Game(640,640, "ClayMan", update_rate=1/60)
    run()

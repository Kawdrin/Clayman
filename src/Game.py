from arcade import Window

class Game(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_update(self, dt):
        ...

    def on_draw(self):
        ...

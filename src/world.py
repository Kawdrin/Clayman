from pygame import display, fastevent, time
from pygame.locals import QUIT, K_f, KEYDOWN
from pygame.key import get_pressed
from pygame.sprite import spritecollide
from src.groups import colisionsGroup, HighGround, ForeGround, BackGround, DetalhesGroup, EntidadesGroup

from src.ent.hero import Hero
from src.map_creator import OgmoMap

class World:
    def __init__(self):
        display.init()
        fastevent.init()
        self.tela = display.set_mode((640,640))
        display.set_caption("ClayMan")
        self.FPS_TICK = time.Clock()
        self.GAMELOOP = True
        self.map_generator = OgmoMap("res/map/NewLevel0.json", "res/CreyMan.png")

    def new_game(self):
        self.map_generator.create_grid(0, colisionsGroup)

        self.map_generator.create_tile(1, HighGround)

        self.map_generator.create_tile(2, ForeGround)

        self.map_generator.create_tile(5, BackGround)
        self.map_generator.create_tile(4, DetalhesGroup)

        self.map_generator.spawn_entities(3, EntidadesGroup, 2)

        self.hero = Hero(self.map_generator.get_pos_entitie("Hero", 3, 2), EntidadesGroup)

    def run(self):
        self.new_game()
        while self.GAMELOOP:
            self.verifica_evento()
            self.update()
            self.draw()
            self.FPS_TICK.tick(60)

    def verifica_evento(self):
        for event in fastevent.get():
            if event.type == QUIT:
                self.GAMELOOP = False

            if event.type == KEYDOWN and event.key == K_f:
                if self.hero.item_grab:
                    self.hero.soltar_item()
                else:
                    self.hero.grab_item()

    def update(self):
        EntidadesGroup.update()
        display.flip()

    def organizar_ordem_de_sprites(self):
        for item in spritecollide(self.hero.hitbox, EntidadesGroup, False):
            if item == self.hero:
                continue
            if self.hero.rect.bottom <= item.rect.bottom-4:
                lista_sprites  = EntidadesGroup.sprites()
                EntidadesGroup.empty()

                heroi_index = lista_sprites.index(self.hero)
                lista_sprites.remove(item)
                lista_sprites.insert(heroi_index+1, item)

                EntidadesGroup.add(lista_sprites)
                break

            if self.hero.rect.bottom >= item.rect.bottom-4:
                lista_sprites  = EntidadesGroup.sprites()
                EntidadesGroup.empty()

                heroi_index = lista_sprites.index(self.hero)
                lista_sprites.remove(item)
                lista_sprites.insert(heroi_index-1, item)

                EntidadesGroup.add(lista_sprites)


    def draw(self):
        BackGround.draw(self.tela)
        ForeGround.draw(self.tela)
        self.organizar_ordem_de_sprites()
        DetalhesGroup.draw(self.tela)
        EntidadesGroup.draw(self.tela)
        HighGround.draw(self.tela)

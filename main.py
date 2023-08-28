import pygame as pg
from setting import *
import sys
from map import *
from player import *
from raycasting import *
from object_render import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *

class game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(res)
        self.clock = pg.time.Clock()
        self.delta_t = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event,40)
        self.new_game()
    
    def new_game(self):
        self.map = map(self)
        self.player = player(self)
        self.object = objectrender(self)
        self.ray=ray(self)
        self.object_handler=objecthandler(self)
        self.weapon=weapon(self)
        self.sound =Sound(self)
        self.pathfinding=PathFinding(self)


    def update(self):
        self.player.update()
        self.ray.update()
        pg.display.flip()
        self.delta_t = self.clock.tick(fps)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
        self.object_handler.update()
        self.weapon.update()
        self.sound.theme.play()

    
    def draw(self):
        self.object.draw()
        self.weapon.draw()

    def event_checker(self):
        self.global_trigger=False
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif e.type == self.global_event:
                self.global_trigger=True
        
        
            self.player.single_fire_event(e)
    
    def runner(self):
        while True:
            self.event_checker()
            self.update()
            self.draw()
            if self.player.killed == self.object_handler.npc_no():
                self.object.victory()


if __name__ == '__main__':
    g=game()
    g.runner()

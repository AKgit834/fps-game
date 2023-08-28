from sprite import *
from npc import *

class objecthandler:
    def __init__(self,game):
        self.game=game
        self.sprite_list=[]
        self.npc_list = []
        self.npc_sprite_path= 'resources/sprites/npc'
        add_npc = self.add_npc
        self.npc_positions = {}

        self.static_sprite_path= 'resources/sprites/static_sprites/'
        self.animated_sprite_path= 'resources/sprites/animated_sprite/'
        add_sprite=self.add_sprite

        # add_sprite(sprite(game,pos=(3,2)))
        # add_sprite(sprite(game,pos=(3.5,9)))
        add_sprite(sprite(game,pos=(11,7.5)))


        #npc
        add_npc(NPC(game))
        add_npc(NPC(game,pos=(11,6.3)))
        add_npc(NPC(game,pos=(8,3.5)))
        add_npc(NPC(game,pos=(6,2.5)))
        add_npc(NPC(game,pos=(16,4.5)))

        add_npc(boss(game,pos=(10,12.5)))
        add_npc(boss(game,pos=(7,12.5)))
        add_npc(boss(game,pos=(14,12.5)))

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprites.update() for sprites in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_sprite(self,sprite):
        self.sprite_list.append(sprite)

    def add_npc(self,npc):
        self.npc_list.append(npc)

    def npc_no(self):
        return len(self.npc_list)
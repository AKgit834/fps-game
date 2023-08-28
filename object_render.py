import pygame as pg
from setting import *

class objectrender:
    def __init__(self,game):
        self.game=game
        self.screen=game.screen
        self.wall_tex = self.load_wall()
        self.sky_img = self.get_texture('resources/texture/sky.png',(WIDTH,HALF_HEIGHT))
        self.sky_offset=0
        self.blood_screen = self.get_texture('resources/texture/blood_screen.png',res)

        self.digit_size=90
        self.digit_images = [self.get_texture(f'resources/texture/digits/{i}.png',[self.digit_size]*2)
                             for i in range(11)]
        self.digits = dict(zip(map(str,range(11)),self.digit_images))

        self.game_over_image = self.get_texture('resources/texture/game_over.png',res)

        self.victory_image = self.get_texture('resources/texture/win.png',res)

    def draw(self):
        self.draw_bg()
        self.render_game_objects()
        self.draw_player_health()

    def draw_player_health(self):
        health=str(self.game.player.health)
        for i,char in enumerate(health):
            self.screen.blit(self.digits[char],(i*self.digit_size,0))
        self.screen.blit(self.digits['10'],((i+1)*self.digit_size,0))

    def player_damage(self):
        self.screen.blit(self.blood_screen,(0,0))

    def game_over(self):
        self.screen.blit(self.game_over_image,(0,0))

    def victory(self):
        self.screen.blit(self.victory_image,(0,0))
        for e in pg.event.get():
            if e.type == pg.KEYDOWN and e.key == pg.K_z:
                self.game.new_game()
            if e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                pg.quit()
    
    def draw_bg(self):
        self.sky_offset=(self.sky_offset+4.5*self.game.player.rel)%WIDTH
        self.screen.blit(self.sky_img,(-self.sky_offset,0))
        self.screen.blit(self.sky_img,(-self.sky_offset+WIDTH,0))
        pg.draw.rect(self.screen,'black',(0,HALF_HEIGHT,WIDTH,HEIGHT))


    def render_game_objects(self):
        list_objects=sorted(self.game.ray.object_to_render,key=lambda t:t[0],reverse=True)
        for depth,image,pos in list_objects:
            self.screen.blit(image,pos)

    @staticmethod
    def get_texture(path,res=(TEXTURE_SIZE,TEXTURE_SIZE)):
        tex = pg.image.load(path).convert_alpha()
        return pg.transform.scale(tex,res)
    
    def load_wall(self):
        return{
            1: self.get_texture('resources/texture/1.png'),
            2: self.get_texture('resources/texture/2.png'),
            3: self.get_texture('resources/texture/3.png'),
            4: self.get_texture('resources/texture/4.png'),
            5: self.get_texture('resources/texture/5.png'),
        }
    

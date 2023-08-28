import math
from setting import *
import pygame as pg

class player:
    def __init__(self,game):
        self.game=game
        self.x,self.y=player_pos
        self.angle=player_angle
        self.shot=False
        self.health=player_max_health
        self.rel=0
        self.killed=enemies_killed

    def check_game_over(self):
        if self.health<1:
            self.game.object.game_over()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.object.game_over()
            self.game.new_game()   

    def single_fire_event(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                self.game.sound.shotgun.play()
                self.shot=True
                self.game.weapon.reloading=True


    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = player_speed * self.game.delta_t
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        num_key_pressed = -1
        if keys[pg.K_w]:
            num_key_pressed += 1
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            num_key_pressed += 1
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            num_key_pressed += 1
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            num_key_pressed += 1
            dx += -speed_sin
            dy += speed_cos

        # diag move correction
        # if num_key_pressed:
        #     dx *= self.diag_move_corr
        #     dy *= self.diag_move_corr

        self.collision_checker(dx, dy)
        self.angle %= math.tau

    # def movement(self):
    #     sin_a = math.sin(self.angle)
    #     cos_a = math.cos(self.angle)
    #     dx,dy=0,0
    #     speed = player_speed * self.game.delta_t
    #     sin_speed=speed*sin_a
    #     cos_speed=speed*cos_a

    #     keys=pg.key.get_pressed()
    #     if keys[pg.K_w]:
    #         dy += sin_speed
    #         dx += cos_speed
    #     if keys[pg.K_s]:
    #         dy += -sin_speed
    #         dx += -cos_speed
    #     if keys[pg.K_a]:
    #         dy += -sin_speed
    #         dx += cos_speed
    #     if keys[pg.K_d]:
    #         dy += sin_speed
    #         dx += -cos_speed
        
    #     self.collision_checker(dx,dy)
    #     self.angle %= math.tau


    def get_damage(self,damage):
        self.health -= damage
        self.game.object.player_damage()
        self.game.sound.player_pain.play()
        self.check_game_over()


    def wall_checker(self,x,y):
        return (x,y) not in self.game.map.wm
    
    def collision_checker(self,dx,dy):
        scale=player_size_scale/self.game.delta_t
        if self.wall_checker(int(self.x+dx*scale),int(self.y)):
            self.x+=dx
        if self.wall_checker(int(self.x),int(self.y+dy*scale)):
            self.y+=dy

    def draw(self):
        pg.draw.circle(self.game.screen,'white',(self.x*100,self.y*100),15)

    def mouse_control(self):
        mx,my=pg.mouse.get_pos()
        if mx<MOUSE_BORDER_LEFT or mx>MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH,HALF_HEIGHT])
        self.rel=pg.mouse.get_rel()[0]
        self.rel=max(-MOUSE_MAX_REL,min(MOUSE_MAX_REL,self.rel))
        self.angle += self.rel*MOUSE_SENSITIVITY*self.game.delta_t 

    def update(self):
        self.movement()
        self.mouse_control()
        
    @property
    def pos(self):
        return self.x,self.y
    @property
    def mpos(self):
        return int(self.x),int(self.y)

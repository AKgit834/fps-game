import math
from setting import *
import pygame as pg

class ray:
    def __init__(self,game):
        self.game = game
        self.ray_result=[]
        self.object_to_render=[]
        self.tex=self.game.object.wall_tex

    def get_objects_to_render(self):
        self.object_to_render=[]
        for ray,values in enumerate(self.ray_result):
            depth,proj_height,texture,offset=values
            if proj_height < HEIGHT:
                wall_column = self.tex[texture].subsurface(
                    offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE
                )
                wall_column = pg.transform.scale(wall_column, (SCALE, proj_height))
                wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)
            else:
                texture_height = TEXTURE_SIZE * HEIGHT / proj_height
                wall_column = self.tex[texture].subsurface(
                    offset * (TEXTURE_SIZE - SCALE), HALF_TEXTURE_SIZE - texture_height // 2,
                    SCALE, texture_height
                )
                wall_column = pg.transform.scale(wall_column, (SCALE, HEIGHT))
                wall_pos = (ray * SCALE, 0)
            self.object_to_render.append((depth,wall_column,wall_pos))

    def ray_casting(self):
        ox,oy=self.game.player.pos
        mx,my=self.game.player.mpos
        texture_vert,texture_hor=1,1
        ray_angle = self.game.player.angle-HALF_FOV+0.0001
        self.ray_result=[]

        for rays in range(NUM_RAYS):
            sin_a=math.sin(ray_angle)
            cos_a=math.cos(ray_angle)

            #HORIZONTAL
            y_hor,dy=(my+1,1) if sin_a>0 else (my-1e-6,-1)
            depth_hor = (y_hor-oy)/sin_a
            x_hor=ox+depth_hor*cos_a
            delta_depth=dy/sin_a
            dx=delta_depth*cos_a
            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor),int(y_hor)
                if tile_hor in self.game.map.wm:
                    texture_hor=self.game.map.wm[tile_hor]
                    break
                x_hor+=dx
                y_hor+=dy
                depth_hor+=delta_depth


            #VERTICAL
            x_vert,dx=(mx+1,1) if cos_a>0 else (mx-1e-6,-1)

            depth_vert=(x_vert-ox)/cos_a
            y_vert=depth_vert*sin_a+oy

            delta_depth = dx/cos_a
            dy=delta_depth*sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert),int(y_vert)
                if tile_vert in self.game.map.wm:
                    texture_vert=self.game.map.wm[tile_vert]
                    break
                x_vert+=dx
                y_vert+=dy
                depth_vert+=delta_depth

            if depth_hor > depth_vert:
                depth,texture=depth_vert,texture_vert
                y_vert %= 1
                offset=y_vert if cos_a>0 else (1-y_vert)
            else:
                depth,texture=depth_hor,texture_hor
                x_hor %= 1
                offset=(1-x_hor) if sin_a>0 else x_hor

            depth *= math.cos(self.game.player.angle - ray_angle)

            # #projection
            proj_height=SCREEN_DIST/(depth + 0.0001)

            self.ray_result.append((depth,proj_height,texture,offset))

            ray_angle += DELTA_ANGLE



    def update(self):
        self.ray_casting()
        self.get_objects_to_render()

import math


res = WIDTH ,HEIGHT =1600,900
HALF_HEIGHT=HEIGHT//2
HALF_WIDTH=WIDTH//2
fps=60

player_pos = 2,2
player_speed=0.004
player_angle = 0
player_rot_speed = 0.002
player_size_scale = 60
player_max_health = 100

MOUSE_SENSITIVITY = 0.0003
MOUSE_MAX_REL=40
MOUSE_BORDER_LEFT=100
MOUSE_BORDER_RIGHT=WIDTH-MOUSE_BORDER_LEFT



FOV = math.pi/3
HALF_FOV=FOV/2
NUM_RAYS=WIDTH//2
HALF_NUM_RAYS=NUM_RAYS//2
DELTA_ANGLE=FOV/NUM_RAYS
MAX_DEPTH=20


SCREEN_DIST=HALF_WIDTH/math.tan(HALF_FOV)
SCALE=WIDTH//NUM_RAYS


TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = 256 // 2

enemies_killed = 0
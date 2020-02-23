"""
Constants here
"""
import pygame as pg
pg.font.init()

DEFAULT_FONT = "PressStart2P.ttf"  # To instantiate a font use pygame.font.Font(DEFAULT_FONT, font size)
# ------------------------COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK_HIGHLIGHT = (0, 0, 0, 150)

# ------------------------BUTTON SIZE
BUTTON_WIDTH = 220
BUTTON_HEIGHT = 60

# ------------------------SCENE SIZES
M_SCREEN_WIDTH = 800
M_SCREEN_HEIGHT = 600

G_SCREEN_WIDTH = 1200
G_SCREEN_HEIGHT = 800

S_SCREEN_WIDTH = 1280
S_SCREEN_HEIGHT = 720

R_SCREEN_WIDTH = 1200
R_SCREEN_HEIGHT = 800

# ------------------------SOUNDS
HOVER_SOUND = "blipshort1.wav"

# ------------------------PYMUNK
FPS = 60
EARTH_GRAVITY = 0, -700
TERRAIN_THICKNESS = 100
TERRAIN_FRICTION = 1.
SEGMENT_LENGTH = 75

ANTI_SPACECRAFT_WHEEL_SIZE = 15
ANTI_SPACECRAFT_MOVE_FORCE = 35
ANTI_SPACECRAFT_CHASSIS = (50, 15)
ANTI_SPACECRAFT_CANNON = (50, 5)
DEFAULT_FORCE = (0, 0)
DEFAULT_MOMENT = 1
DEFAULT_MASS = 1
DEFAULT_FRICTION = .5
DEFAULT_CONTROLS = ['A', 'W', 'D', 'Left', 'Up', 'Right', 'Down', 'Space']

CONTROL_DICT = {
        'Z': pg.K_z,
        'X': pg.K_x,
        'C': pg.K_c,
        'Up': pg.K_UP,
        'Down': pg.K_DOWN,
        'Space': pg.K_SPACE,
        'Left': pg.K_LEFT,
        'Right': pg.K_RIGHT
}
import os

RESOLUTION = (1020, 720)
FRAMERATE = 60
STATIC_ROOT = os.path.join(os.path.dirname(__file__), "static")
IMAGE_ROOT = os.path.join(STATIC_ROOT, "img")
MAP_ROOT = os.path.join(STATIC_ROOT, "maps")

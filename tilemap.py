import pygame as pg
from settings import *


class Map:
    def __init__(self, filename):
        # Loading map txt file
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tile_width = len(self.data[0])
        self.tile_height = len(self.data)
        self.width = self.tile_width * Tilesize
        self.height = self.tile_height * Tilesize

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        # Limit
        x = min(0, x)
        x = max(-(self.width - WIDTH), x)
        y = min(0, y)
        y = max(-(self.height - HEIGHT), y)
        self.camera = pg.Rect(x, y, self.width, self.height)

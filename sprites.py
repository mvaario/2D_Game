#  Sprite classes

import pygame as pg
from settings import *

vec = pg.math.Vector2

class player(pg.sprite.Sprite):
    # Sprite for player
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((Tilesize, Tilesize))
        self.image.fill(Red)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
            return False


    def update(self):
        self.rect.x = self.x * Tilesize
        self.rect.y = self.y * Tilesize

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((Tilesize, Tilesize))
        self.image.fill(Green)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * Tilesize
        self.rect.y = y * Tilesize

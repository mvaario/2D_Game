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
        self.image.fill(Green)
        self.rect = self.image.get_rect()
        self.vx, self.vt = 0, 0
        self.x = x * Tilesize
        self.y = y * Tilesize

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx = -Player_speed
        elif keys[pg.K_RIGHT]:
            self.vx = Player_speed
        if keys[pg.K_UP]:
            self.vy = -Player_speed
        elif keys[pg.K_DOWN]:
            self.vy = Player_speed


    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x

        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y




    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((Tilesize, Tilesize))
        self.image.fill(Orange)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * Tilesize
        self.rect.y = y * Tilesize

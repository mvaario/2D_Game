# Pygame template
# Made by mvaario
# inspired by KidsCanCode

import pygame as pg
import sys
import random
from sprites import *
from settings import *
from tilemap import *
from os import path


class game:
    def __init__(self):
        # Initialize game window, etc
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(TITLE)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.key.set_repeat(500,100)
        self.clock = pg.time.Clock()
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, 'map.txt'))

    def new(self):
        # Start a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'p':
                    self.player = player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)


    def run(self):
        # Game loop
        self.clock.tick(FPS)
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game loop - update
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, Tilesize):
            pg.draw.line(self.screen, LightGray, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, Tilesize):
            pg.draw.line(self.screen, LightGray, (0, y), (WIDTH, y))

    def draw(self):
        # Game loop draw
        self.screen.fill(BGColor)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        # Game loop events
        for event in pg.event.get():
            # closing the window
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    self.quit()


    def show_start_screen(self):
        # Shows screen
        pass

    def show_go_screen(self):
        # Game over
        pass



    def quit(self):
        pg.quit()
        sys.exit()


g = game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()

pg.quit()

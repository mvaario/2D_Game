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
        self.clock = pg.time.Clock()
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, 'map.txt'))

    def new(self):
        # Start a new game
        for row, tiles in enumerate(g.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(g, col, row)
                if tile == 'p':
                    g.player = player(g, col, row)
        g.camera = Camera(g.map.width, g.map.height)


    def run(self):
        # Game loop
        g.clock.tick(FPS)
        g.playing = True
        while g.playing:
            g.dt = g.clock.tick(FPS) / 1000
            g.events()
            g.update()
            g.draw()

    def update(self):
        # Game loop - update
        g.all_sprites.update()
        g.camera.update(g.player)

    def draw_grid(self):
        for x in range(0, WIDTH, Tilesize):
            pg.draw.line(g.screen, LightGray, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, Tilesize):
            pg.draw.line(g.screen, LightGray, (0, y), (WIDTH, y))

    def draw(self):
        # Game loop draw
        g.screen.fill(BGColor)
        g.draw_grid()
        for sprite in g.all_sprites:
            g.screen.blit(sprite.image, g.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        # Game loop events
        for event in pg.event.get():
            # closing the window
            if event.type == pg.QUIT:
                g.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    g.quit()


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


pg.quit()

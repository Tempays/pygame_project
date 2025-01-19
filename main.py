import os
import sys

import pygame

FPS = 144
clock = pygame.time.Clock()

size = WIDTH, HEIGHT = 500, 500

player = None

tiles_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
tile_width = tile_height = 50


class RhombusSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, length):
        super().__init__(tiles_group, all_sprites)
        self.x = x * length
        self.y = y * length
        self.diagonal = (2 * length ** 2) ** 0.5
        self.image = (load_image('stone_tile.png')).convert_alpha()
        self.image = pygame.transform.rotate(self.image, 120)
        self.image = pygame.transform.scale(self.image, (132, 78))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


def load_image(name, colorkey=None):
    fullname = "data/" + name
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    if colorkey is None:
        return pygame.image.load(fullname)
    return pygame.image.load(fullname, colorkey)


def load_level(filename):
    filename = "data/" + filename
    if not os.path.isfile(filename):
        return None
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    return level_map


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                RhombusSprite(1.5 * x + y, y - 0.5 * x, tile_width)
    return x, y, level


def terminate():
    pygame.quit()
    sys.exit()


def play_cycle():
    clock.tick(FPS)
    screen.fill('black')
    pygame.display.flip()
    level = load_level('map.txt')
    if level is None:
        print('Этого файла не существует')
        terminate()

    pygame.display.flip()
    generate_level(level)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

        screen.fill('black')
        all_sprites.draw(screen)
        pygame.display.flip()


pygame.init()
size = WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode(size)
play_cycle()

import os
import sys

import pygame

FPS = 144
clock = pygame.time.Clock()

size = WIDTH, HEIGHT = 500, 500

player = None

tiles_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
right_walls = pygame.sprite.Group()
special = pygame.sprite.Group()
tile_width = 70
wall_hight = 50


class RhombusSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, length):
        super().__init__(tiles_group, all_sprites)
        self.x = x * length
        self.y = y * length
        self.diagonal = (2 * length ** 2) ** 0.5
        self.image = load_image('stone_tile.png')
        self.image = pygame.transform.rotate(self.image, 135)
        self.image = pygame.transform.scale(self.image, (tile_width * 2.04, tile_width * 1.04))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class RightWallSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, length):
        super().__init__(tiles_group, all_sprites, right_walls)
        self.image = load_image('right_wall.png')
        self.image = pygame.transform.scale(self.image, (tile_width * 1.1, tile_width * 1.5))
        self.image = pygame.transform.rotate(self.image, -1)
        self.rect = self.image.get_rect()
        self.rect.x = x * length
        self.rect.y = y * length


class LeftWallSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, length):
        super().__init__(tiles_group, all_sprites, right_walls)
        self.image = load_image('right_wall.png')
        self.image = pygame.transform.scale(self.image, (tile_width * 1.1, tile_width * 1.5))
        self.image = pygame.transform.rotate(self.image, -1)
        self.image = pygame.transform.flip(self.image, 1, 0)
        self.rect = self.image.get_rect()
        self.rect.x = x * length
        self.rect.y = y * length


def load_image(name, colorkey=None):
    fullname = "data/" + name
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    filename = "data/" + filename
    if not os.path.isfile(filename):
        return None
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    return level_map


def set_right_wall(x, y):
    return RightWallSprite(x + y, 0.5 * y - 0.5 * x - 0.007 * tile_width, tile_width)


def set_left_wall(x, y):
    return LeftWallSprite(x + y + 0.014 * tile_width, 0.5 * y - 0.5 * x - 0.007 * tile_width, tile_width)


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                RhombusSprite(x + y, 0.5 * y - 0.5 * x, tile_width)
            elif level[y][x] == 'R':
                set_right_wall(x, y)
    for y in range(len(level) - 1, -1, -1):
        for x in range(len(level[y]) - 1, -1, -1):
            if level[y][x] == 'L':
                set_left_wall(x, y)
            elif level[y][x] == 'W':
                set_right_wall(x, y)
                set_left_wall(x, y)
            elif level[y][x] == 'M':
                wall = set_right_wall(x, y)
                special.add(wall)
                set_left_wall(x, y - 1)
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
        right_walls.draw(screen)
        special.draw(screen)
        pygame.display.flip()


pygame.init()
size = WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode(size)
play_cycle()

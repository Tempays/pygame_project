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
player_group = pygame.sprite.Group()
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
        self.image = load_image('isometric_0055.png')
        self.image = pygame.transform.scale(self.image, (tile_width * 2.4, tile_width * 2))
        self.image = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect()
        self.rect.x = x * length
        self.rect.y = y * length


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, length):
        super().__init__(all_sprites, player_group)
        self.x_init = x
        self.y_init = y
        self.x = x + y
        self.y = 0.5 * y - 0.5 * x - tile_width * 0.02
        self.length = length
        self.image = load_image('Protect.png')
        self.image = pygame.transform.scale(self.image, (tile_width * 3.5, tile_width * 3.5))
        self.image = pygame.transform.flip(self.image, 1, 0)
        self.image = pygame.transform.rotate(self.image, -20)
        self.rect = self.image.get_rect()
        self.rect.x = self.x * length
        self.rect.y = self.y * length

    def ok_pos(self):
        if 0 > self.x_init > 1:
            pass

    def move(self, x, y):
        self.x_init += x
        self.y_init += y

    def update(self):
        self.x = self.x_init + self.y_init - 1.5
        self.y = 0.5 * self.y_init - 0.5 * self.x_init - 3.5
        self.rect.x = self.x * self.length
        self.rect.y = self.y * self.length


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


def set_wall(x, y):
    RightWallSprite(x + y - 0.001 * tile_width, 0.5 * y - 0.5 * x - 0.013 * tile_width, tile_width)
    RightWallSprite(x + y - 0.001 * tile_width, 0.5 * y - 0.5 * x - 0.027 * tile_width, tile_width)


def generate_level(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                RhombusSprite(x + y, 0.5 * y - 0.5 * x, tile_width)
            elif level[y][x] == 'R':
                set_wall(x, y)
            elif level[y][x] == 'P':
                RhombusSprite(x + y, 0.5 * y - 0.5 * x, tile_width)
                player = Player(x, y, tile_width)
    for y in range(len(level) - 1, -1, -1):
        for x in range(len(level[y]) - 1, -1, -1):
            if level[y][x] == 'L':
                set_wall(x, y)
    return player


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
    player = generate_level(level)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player.move(0, 1)
                elif event.key == pygame.K_UP:
                    player.move(0, -1)
                elif event.key == pygame.K_LEFT:
                    player.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    player.move(1, 0)

        screen.fill('black')
        all_sprites.draw(screen)
        right_walls.draw(screen)
        special.draw(screen)
        player.update()
        player_group.draw(screen)
        pygame.display.flip()


pygame.init()
size = WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode(size)
play_cycle()

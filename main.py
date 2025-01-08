import os
import sys

import pygame

FPS = 144
clock = pygame.time.Clock()

player = None

tiles_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
tile_width = tile_height = 50


class RhombusSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, length, color):
        super().__init__(tiles_group, all_sprites)
        self.x = x * length
        self.y = y * length
        self.diagonal = (2 * length ** 2) ** 0.5
        self.color = color
        self.image = pygame.image

    def draw(self, surface):
        points = [
            (self.x, self.y),
            (self.x + self.diagonal / 2 + 20, self.y - self.diagonal / 2),
            (self.x + self.diagonal + 40, self.y),
            (self.x + self.diagonal / 2 + 20, self.y + self.diagonal / 2)
        ]
        pygame.draw.polygon(surface, self.color, points)
        # Отрисовка ромба в зависимости от карты нуждается в доработке


def load_image(name, colorkey=None):
    fullname = os.path.join('../../Desktop/task/data', name)
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
                RhombusSprite(x, y, tile_width, pygame.Color('brown'))
    return x, y, level


def terminate():
    pygame.quit()
    sys.exit()


def play_cycle():
    clock.tick(FPS)
    screen.fill('black')
    pygame.display.flip()
    level = load_level(input())
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
        for sprite in all_sprites:
            sprite.draw(screen)
        pygame.display.flip()


pygame.init()
# size = WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
size = WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode(size)
play_cycle()

import os
import sys

import pygame

FPS = 144
clock = pygame.time.Clock()

player = None


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
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

        screen.fill('black')
        pygame.display.flip()


pygame.init()
size = WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode(size)
play_cycle()

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
doors_group = pygame.sprite.Group()
torch_group = pygame.sprite.Group()
tile_width = 70
wall_hight = 50

doors = dict()
doors['map.txt'] = '1', 'map_2.txt'


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
        self.rect = self.image.get_rect()
        self.rect.x = x * length
        self.rect.y = y * length


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, length):
        super().__init__(tiles_group, all_sprites, right_walls)
        self.image = load_image('door.png', -1)
        self.image = pygame.transform.rotate(self.image, 20)
        self.image = pygame.transform.scale(self.image, (tile_width * 2.4, tile_width * 3.4))
        self.rect = self.image.get_rect()
        self.rect.x = x * length
        self.rect.y = y * length


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

    def cut_sheet(self, sheet, columns, rows):
        self.frames = []
        self.rect = pygame.Rect(0, 0, self.image.get_width() // columns,
                                self.image.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class DoorSprite(AnimatedSprite):
    def __init__(self, x, y, length):
        self.image = load_image('door.png')
        self.frames = []
        self.cut_sheet(self.image, 6, 1)
        super().__init__()
        for i in range(len(self.frames)):
            self.frames[i] = pygame.transform.scale(self.frames[i], (2.2 * length, 3 * length))
            self.frames[i] = pygame.transform.rotate(self.frames[i], -4)
        self.rect.x = x * length
        self.rect.y = y * length
        right_walls.add(self)
        doors_group.add(self)


class TorchSprite(AnimatedSprite):
    def __init__(self, image, x, y, length):
        self.x, self.y = x, y
        self.length = length
        self.image = load_image(image)
        self.cut_sheet(self.image, 4, 2)
        super().__init__()
        for i in range(len(self.frames)):
            self.frames[i] = pygame.transform.rotate(pygame.transform.scale(self.frames[i], (1.25 * length, 1.25 * length)), 20)
        self.rect.x = (x + y - 0.2) * length
        self.rect.y = (0.5 * y - 0.5 * x - 1.5) * length
        torch_group.add(self)


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
        self.image = pygame.transform.rotate(self.image, -22)
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
    return (RightWallSprite(x + y - 0.001 * tile_width, 0.5 * y - 0.5 * x - 0.013 * tile_width, tile_width),
            RightWallSprite(x + y - 0.001 * tile_width, 0.5 * y - 0.5 * x - 0.027 * tile_width, tile_width))


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
            elif level[y][x] == 'T':
                set_wall(x, y)
                TorchSprite('torch.png', x, y, tile_width)
    for y in range(len(level) - 1, -1, -1):
        for x in range(len(level[y]) - 1, -1, -1):
            if level[y][x] == 'L':
                set_wall(x, y)
            elif level[y][x] == 'l':
                special.add(set_wall(x, y))
            elif level[y][x].isdigit():
                DoorSprite(x + y - 0.4 + 0.5, 0.5 * (y - 0.4) - 0.5 * x - 1.8, tile_width)
    return player


def terminate():
    pygame.quit()
    sys.exit()


def play_cycle():
    torch_count = 0
    clock.tick(FPS)
    screen.fill('black')
    level = load_level('map.txt')
    if level is None:
        print('Этого файла не существует')
        terminate()

    player = generate_level(level)
    door_intersection = False
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
                    door_intersection = True


        if door_intersection:
            for sprite in all_sprites:
                sprite.kill()
            level = load_level('map_2.txt')
            player = generate_level(level)
            door_intersection = False


        torch_count = (torch_count + 1) % (FPS / 2)
        if not torch_count:
            torch_group.update()
            doors_group.update()



        screen.fill('black')
        all_sprites.draw(screen)
        right_walls.draw(screen)
        player.update()
        torch_group.draw(screen)
        player_group.draw(screen)
        special.draw(screen)
        pygame.display.flip()


pygame.init()
size = WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode(size)
play_cycle()

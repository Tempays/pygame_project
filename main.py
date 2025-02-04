import os
import sys

import pygame

FPS = 144
clock = pygame.time.Clock()

pygame.init()
size = WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

player = None

tiles_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
right_walls = pygame.sprite.Group()
special = pygame.sprite.Group()
player_group = pygame.sprite.Group()
doors_group = pygame.sprite.Group()
torch_group = pygame.sprite.Group()
floor = pygame.sprite.Group()
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
        self.mask = pygame.mask.from_surface(self.image)


class RightWallSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, length):
        super().__init__(tiles_group, all_sprites, right_walls)
        self.image = load_image('isometric_0055.png')
        self.image = pygame.transform.scale(self.image, (tile_width * 2.4, tile_width * 2))
        self.rect = self.image.get_rect()
        self.rect.x = x * length
        self.rect.y = y * length
        self.mask = pygame.mask.from_surface(self.image)


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
        self.number = None
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
            self.frames[i] = pygame.transform.rotate(pygame.transform.scale(self.frames[i],
                                                                            (1.25 * length, 1.25 * length)), 20)
        self.rect.x = (x + y - 0.2) * length
        self.rect.y = (0.5 * y - 0.5 * x - 1.5) * length
        torch_group.add(self)


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, length):
        super().__init__(all_sprites)
        self.x_init = x
        self.y_init = y
        self.x = x + y
        self.y = 0.5 * y - 0.5 * x - tile_width * 0.02
        self.length = length

        self.image = load_image('knight_sprites/idle.png')
        self.image = pygame.transform.scale(self.image, (tile_width * 3.5, tile_width * 3.5))
        self.image = pygame.transform.flip(self.image, 1, 0)
        self.image = pygame.transform.rotate(self.image, 0)

        self.rect = self.image.get_rect()
        self.rect.x = self.x * length
        self.rect.y = self.y * length

        self.animation_init()

        self.direction = 'forward'
        self.look_direction = 'forward'

        self.anim_number = 0
        self.shadow = None
        self.mask = pygame.mask.from_surface(self.image)
        self.attack = False

    def animation_init(self):
        self.moving = False
        self.stop_anim = self.animation_list('knight_sprites/Idle.png', 4, 1)
        self.walking_anim = self.animation_list('knight_sprites/Walk.png', 8, 1)
        self.def_anim = self.animation_list('knight_sprites/Defend.png', 5, 1)
        self.death_anim = self.animation_list('knight_sprites/Dead.png', 6, 1)
        self.hurt_anim = self.animation_list('knight_sprites/Hurt.png', 2, 1)
        self.attack_anim = self.animation_list('knight_sprites/Attack 2.png', 4, 1)
        self.new_list = []
        for i in range(len(self.stop_anim)):
            self.new_list += [self.stop_anim[i]] + [self.stop_anim[i]] + [self.stop_anim[i]]
        self.stop_anim = self.new_list[:]

    def animation_list(self, image, columns, rows):
        image = load_image(image)
        frames = []
        rect = pygame.Rect(0, 0, image.get_width() // columns, image.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (rect.w * i, rect.h * j)
                frames.append(pygame.transform.scale(pygame.transform.rotate(
                    image.subsurface(pygame.Rect(frame_location, rect.size)), 0),
                    (3.5 * self.length, 3.5 * self.length)))
        return frames

    def update(self):
        self.x = self.x_init + self.y_init + 0.5
        self.y = 0.5 * self.y_init - 0.5 * self.x_init - 2.5

        if self.moving:
            self.anim_number = self.anim_number % len(self.walking_anim)
            self.image = self.walking_anim[self.anim_number]
            if self.look_direction == 'forward':
                self.image = pygame.transform.flip(self.image, 1, 0)
                self.x -= 1.7
        if not self.moving:
            self.anim_number = self.anim_number % len(self.stop_anim)
            self.image = self.stop_anim[self.anim_number]
            if self.look_direction == 'forward':
                self.image = pygame.transform.flip(self.image, 1, 0)
                self.x -= 1.7
        if self.attack:
            if self.anim_number == len(self.attack_anim):
                self.anim_number -= 1
                self.attack = False
                pass
            self.image = self.attack_anim[self.anim_number]
            if self.look_direction == 'forward':
                self.image = pygame.transform.flip(self.image, 1, 0)
                # self.x += 1


        self.rect.x = self.x * self.length
        self.rect.y = self.y * self.length


class Shadow(pygame.sprite.Sprite):
    def __init__(self, owner):
        self.owner = owner
        super().__init__(all_sprites, player_group)
        self.image = pygame.transform.scale(load_image('shadow.png', -1), (tile_width, tile_width))
        self.rect = self.image.get_rect()
        self.image.set_alpha(160)
        self.x_init, self.y_init = self.owner.x_init, self.owner.y_init
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.x = self.x_init + self.y_init + 0.9
        self.y = 0.5 * self.y_init - 0.5 * self.x_init + 0.45
        self.rect.y = self.y * tile_width
        self.rect.x = self.x * tile_width


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
                RhombusSprite(x + y - 3, 0.5 * (y + 3) - 0.5 * (x - 6), tile_width)
            elif level[y][x] == 'R':
                set_wall(x - 6, y + 3)
            elif level[y][x] == 'r':
                floor_piece = RhombusSprite(x + y - 3, 0.5 * (y + 3) - 0.5 * (x - 6), tile_width)
                floor_piece.image.set_alpha(0)
                right_walls.add(floor_piece)
            elif level[y][x] == 'P':
                RhombusSprite(x - 3 + y, 0.5 * (y + 3) - 0.5 * (x - 6), tile_width)
                player = Player(x - 6, y + 3, tile_width)
                player.shadow = Shadow(player)
                player_group.add(player.shadow)
                player_group.add(player)
            elif level[y][x] == 'T':
                set_wall(x - 6, y + 3)
                TorchSprite('torch.png', x - 6, y + 3, tile_width)
    for y in range(len(level) - 1, -1, -1):
        for x in range(len(level[y]) - 1, -1, -1):
            if level[y][x] == 'L':
                set_wall(x - 6, y + 3)
            elif level[y][x].isdigit():
                door = DoorSprite(x - 3 + y - 0.4 + 0.5, 0.5 * (y + 2.6) - 0.5 * (x - 6) - 1.8, tile_width)
                door.number = level[y][x]
    return player


def terminate():
    pygame.quit()
    sys.exit()


def play_cycle():
    torch_count = 0
    door_count = 0
    player_count = 0
    clock.tick(FPS)
    screen.fill('black')
    level = load_level('map.txt')
    if level is None:
        print('Этого файла не существует')
        terminate()

    player = generate_level(level)
    door_intersection = False
    down_hold = up_hold = right_hold = left_hold = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if not player.moving:
                if event.type == pygame.KEYDOWN:
                    if not player.attack:
                        match event.key:
                            case pygame.K_DOWN:
                                player.direction = 'back'
                                player.look_direction = 'back'
                                down_hold = True
                                player.moving = True
                                player.anim_number = 0
                            case pygame.K_UP:
                                player.direction = 'forward'
                                player.look_direction = 'forward'
                                up_hold = True
                                player.moving = True
                                player.anim_number = 0
                            case pygame.K_LEFT:
                                player.direction = 'left'
                                player.look_direction = 'forward'
                                left_hold = True
                                player.moving = True
                                player.anim_number = 0
                            case pygame.K_RIGHT:
                                player.direction = 'right'
                                player.look_direction = 'back'
                                right_hold = True
                                player.moving = True
                                player.anim_number = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    match event.button:
                        case 1:
                            player.anim_number = 0
                            player.attack = True
                        case 3:
                            print('пкм')
            else:
                if event.type == pygame.KEYUP:
                    match event.key:
                        case pygame.K_DOWN:
                            if down_hold:
                                player.moving = False
                                down_hold = False
                                player.anim_number = 0
                        case pygame.K_UP:
                            if up_hold:
                                player.moving = False
                                up_hold = False
                                player.anim_number = 0
                        case pygame.K_LEFT:
                            if left_hold:
                                player.moving = False
                                left_hold = False
                                player.anim_number = 0
                        case pygame.K_RIGHT:
                            if right_hold:
                                player.moving = False
                                right_hold = False
                                player.anim_number = 0

        if door_intersection:
            for sprite in all_sprites:
                if isinstance(sprite, DoorSprite):
                    number = sprite.number
                sprite.kill()
            if number == '1':
                level = load_level('map_2.txt')
            elif number == '2':
                level = load_level('map_3.txt')
            player = generate_level(level)
            door_intersection = False

        if player.moving:
            move = (0, 0)
            match player.direction:
                case 'forward':
                    player.y_init -= 0.01
                    player.shadow.y_init -= 0.01
                    move = (0, -0.01)
                case 'back':
                    player.y_init += 0.01
                    player.shadow.y_init += 0.01
                    move = (0, 0.01)
                case 'left':
                    player.x_init -= 0.01
                    player.shadow.x_init -= 0.01
                    move = (-0.01, 0)
                case 'right':
                    player.x_init += 0.01
                    player.shadow.x_init += 0.01
                    move = (0.01, 0)

            for sprite in doors_group:
                if pygame.sprite.collide_mask(player.shadow, sprite):
                    door_intersection = True

            for sprite in right_walls:
                if pygame.sprite.collide_mask(player.shadow, sprite):
                    player.x_init -= 10 * move[0]
                    player.y_init -= 10 * move[1]
                    player.shadow.x_init -= 10 * move[0]
                    player.shadow.y_init -= 10 * move[1]
                    move = (0, 0)
                    player.moving = False
                    break

        torch_count = (torch_count + 1) % (FPS / 2)
        door_count = (door_count + 1) % (FPS / 4)
        player_count = (player_count + 1) % (FPS / 4)
        if not torch_count:
            torch_group.update()
        if not door_count:
            doors_group.update()
        if not player_count:
            player.anim_number += 1

        screen.fill('black')

        all_sprites.draw(screen)
        # right_walls.draw(screen)
        player_group.update()
        torch_group.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()


screen = pygame.display.set_mode(size)
play_cycle()

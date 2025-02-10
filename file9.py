import os
import sys
import math

import pygame

# счетчик попадпний
count_to_death = 0
total = 0
kills_count = 0
full_map = 0

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
fiends = pygame.sprite.Group()
tile_width = 70
wall_hight = 50

doors = dict()
doors['map.txt'] = '1', 'map_2.txt'


def grades():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Pygame Кликабельная кнопка')
    font = pygame.font.Font(None, 24)
    button_surface = pygame.Surface((600, 100))
    text = font.render("Пройдите все комнаты.", True, (0, 0, 0))
    text_rect = text.get_rect(
        center=(button_surface.get_width() / 2,
                button_surface.get_height() / 2))
    button_rect = pygame.Rect(250, 100, 600, 100)
    button_surface2 = pygame.Surface((600, 100))
    text2 = font.render("Пройдите все комнаты, убив всех врагов.", True, (0, 0, 0))
    text_rect2 = text.get_rect(
        center=(button_surface.get_width() / 2,
                button_surface.get_height() / 2))
    button_rect2 = pygame.Rect(250, 250, 600, 100)
    button_surface3 = pygame.Surface((700, 100))
    text3 = font.render("Пройдите все комнаты, не убив при этом ни одного врага.", True, (0, 0, 0))
    text_rect3 = text.get_rect(
        center=(button_surface.get_width() / 2,
                button_surface.get_height() / 2))
    button_rect3 = pygame.Rect(250, 400, 700, 100)
    button_surface4 = pygame.Surface((150, 50))
    text4 = font.render("Выход", True, (0, 0, 0))
    text_rect4 = text4.get_rect(
        center=(button_surface4.get_width() / 2,
                button_surface4.get_height() / 2))
    button_rect4 = pygame.Rect(600, 600, 150, 50)
    running = True

    while running:
        clock.tick(60)
        screen.fill((100, 125, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect4.collidepoint(event.pos):
                    main_window()
        pygame.draw.rect(button_surface, (255, 255, 255), (0, 0, 600, 100))
        button_surface.blit(text, text_rect)
        screen.blit(button_surface, (button_rect.x, button_rect.y))
        pygame.draw.rect(button_surface2, (255, 255, 255), (0, 0, 600, 100))
        button_surface2.blit(text2, text_rect2)
        screen.blit(button_surface2, (button_rect2.x, button_rect2.y))
        pygame.draw.rect(button_surface3, (255, 255, 255), (0, 0, 700, 100))
        button_surface3.blit(text3, text_rect3)
        screen.blit(button_surface3, (button_rect3.x, button_rect3.y))
        if button_rect4.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface4, (255, 215, 0), (0, 0, 148, 48))
        else:
            pygame.draw.rect(button_surface4, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface4, (255, 255, 255), (0, 0, 148, 48))
        button_surface4.blit(text4, text_rect4)
        screen.blit(button_surface4, (button_rect4.x, button_rect4.y))
        first_p = pygame.image.load("data/passive3_2.png")
        second_p = pygame.image.load("data/passive4_2.png")
        third_p = pygame.image.load("data/active7_2.png")
        screen.blit(first_p, (100, 100))
        screen.blit(second_p, (100, 250))
        screen.blit(third_p, (100, 400))
        pygame.display.update()


def main_window():
    button_surface = pygame.Surface((150, 50))
    button_font = pygame.font.Font(None, 24)
    button_text = button_font.render("Играть", True, (0, 0, 0))
    text_coord = button_text.get_rect(center=(button_surface.get_width() / 2, button_surface.get_height() / 2))
    button_coord = pygame.Rect((WIDTH - 150) // 2, (HEIGHT - 50) // 2 - 75, 150, 50)
    button_surface2 = pygame.Surface((150, 50))
    button_coord2 = pygame.Rect((WIDTH - 150) // 2, (HEIGHT - 50) // 2, 150, 50)
    button_text2 = button_font.render("Выход", True, (0, 0, 0))
    text_coord2 = button_text.get_rect(center=(button_surface2.get_width() / 2, button_surface2.get_height() / 2))
    button_surface3 = pygame.Surface((170, 50))
    button_coord3 = pygame.Rect((875, 590, 170, 50))
    button_text3 = button_font.render("Достижения", True, (0, 0, 0))
    text_coord3 = button_text.get_rect(center=(button_surface2.get_width() / 2, button_surface2.get_height() / 2))

    if __name__ == '__main__':
        pygame.init()
        pygame.display.set_caption('Игра')
        screen = pygame.display.set_mode(size)
        screen.fill((155, 255, 155))
        fps = 144
        running = True
        background = load_image("Battleground3_3.png")

        while running:
            screen.fill('black')
            screen.fill((155, 255, 155))
            screen.blit(background, ((WIDTH - background.get_rect()[2]) // 2, (HEIGHT - background.get_rect()[3]) // 2))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if button_coord.collidepoint(event.pos):
                        print("play")
                        for sprite in all_sprites:
                            sprite.kill()
                        play_cycle()
                    if button_coord2.collidepoint(event.pos):
                        running = False
                        pygame.quit()
                    if button_coord3.collidepoint(event.pos):
                        grades()
            if button_coord.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(button_surface, (255, 215, 0), (0, 0, 148, 48))
            else:
                pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
                pygame.draw.rect(button_surface, (255, 255, 255), (0, 0, 148, 48))
            button_surface.blit(button_text, text_coord)
            screen.blit(button_surface, (button_coord.x, button_coord.y))
            if button_coord2.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(button_surface2, (255, 215, 0), (0, 0, 148, 48))
            else:
                pygame.draw.rect(button_surface2, (0, 0, 0), (0, 0, 150, 50))
                pygame.draw.rect(button_surface2, (255, 255, 255), (0, 0, 148, 48))
            button_surface2.blit(button_text2, text_coord2)
            screen.blit(button_surface2, (button_coord2.x, button_coord2.y))
            if button_coord3.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(button_surface3, (255, 215, 0), (0, 0, 168, 48))
            else:
                pygame.draw.rect(button_surface3, (0, 0, 0), (0, 0, 170, 50))
                pygame.draw.rect(button_surface3, (255, 255, 255), (0, 0, 168, 48))
            button_surface3.blit(button_text3, text_coord3)
            screen.blit(button_surface3, (button_coord3.x, button_coord3.y))
            pygame.display.flip()


def final_window():
    global total
    button_surface = pygame.Surface((150, 50))
    button_font = pygame.font.Font(None, 24)
    total_str = "Счет: " + str(total)
    button_text = button_font.render(total_str, True, (0, 0, 0))
    text_coord = button_text.get_rect(center=(button_surface.get_width() / 2, button_surface.get_height() / 2))
    button_coord = pygame.Rect(240, 150, 150, 50)
    button_surface2 = pygame.Surface((150, 50))
    button_coord2 = pygame.Rect(240, 220, 150, 50)
    button_text2 = button_font.render("В меню", True, (0, 0, 0))
    text_coord2 = button_text.get_rect(center=(button_surface2.get_width() / 2, button_surface2.get_height() / 2))
    button_surface3 = pygame.Surface((500, 120))
    button_text3 = button_font.render("", True, (0, 0, 0))
    text_coord3 = button_text.get_rect(center=(button_surface.get_width() / 2, button_surface.get_height() / 2))
    button_coord3 = pygame.Rect(100, 300, 500, 120)


    if __name__ == '__main__':
        pygame.init()
        pygame.display.set_caption('Игра')
        screen = pygame.display.set_mode(size)
        screen.fill("#fafad2")
        fps = 144
        running = True
        background = load_image("Battleground4_2.png")

        while running:
            screen.blit(background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if button_coord2.collidepoint(event.pos):
                        running = False
                        global count_to_death
                        count_to_death = 0
                        main_window()
            pygame.draw.rect(button_surface, (255, 255, 255), (0, 0, 150, 50))
            button_surface.blit(button_text, text_coord)
            screen.blit(button_surface, (button_coord.x, button_coord.y))
            if button_coord2.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(button_surface2, (255, 215, 0), (0, 0, 148, 48))
            else:
                pygame.draw.rect(button_surface2, (0, 0, 0), (0, 0, 150, 50))
                pygame.draw.rect(button_surface2, (255, 255, 255), (0, 0, 148, 48))
            button_surface2.blit(button_text2, text_coord2)
            screen.blit(button_surface2, (button_coord2.x, button_coord2.y))
            pygame.draw.rect(button_surface3, (255, 255, 255), (0, 0, 600, 120))
            button_surface3.blit(button_text3, text_coord3)
            screen.blit(button_surface3, (button_coord3.x, button_coord3.y))
            first_p = pygame.image.load("data/passive3_2.png")
            second_p = pygame.image.load("data/passive4_2.png")
            third_p = pygame.image.load("data/active7_2.png")
            global kills_count
            global full_map
            if full_map == 1:
                screen.blit(first_p, (120, 310))
            if kills_count == 4:
                screen.blit(second_p, (270, 310))
            if kills_count == 0 and full_map == 1:
                screen.blit(third_p, (400, 310))
            pygame.display.flip()


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
        super().__init__(tiles_group, all_sprites)
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


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, length, image_path, animation_paths):
        super().__init__(all_sprites)
        self.x_init = x
        self.y_init = y
        self.x = x + y
        self.y = 0.5 * y - 0.5 * x - tile_width * 0.02
        self.length = length

        self.image = load_image(image_path)

        self.rect = self.image.get_rect()
        self.rect.x = self.x * length
        self.rect.y = self.y * length

        self.animation_init(animation_paths)

        self.direction = 'forward'
        self.look_direction = 'forward'

        self.anim_number = 0
        self.shadow = None
        # self.mask = pygame.mask.from_surface(self.image)
        self.attack = False

        self.hp = 3

    def animation_init(self, animation_paths):
        self.moving = False
        self.stop_anim = self.animation_list(animation_paths['idle'], 4, 1)
        self.walking_anim = self.animation_list(animation_paths['walk'], 8, 1)
        self.def_anim = self.animation_list(animation_paths['defend'], 5, 1)
        self.death_anim = self.animation_list(animation_paths['death'], 6, 1)
        self.hurt_anim = self.animation_list(animation_paths['hurt'], 2, 1)
        self.attack_anim = self.animation_list(animation_paths['attack'], 4, 1)
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
            stop = False
            if self.anim_number == len(self.attack_anim):
                self.anim_number -= 1
                self.attack = False
                stop = True
            if not stop:
                self.image = self.attack_anim[self.anim_number]
                if self.look_direction == 'forward':
                    self.image = pygame.transform.flip(self.image, 1, 0)

        self.rect.x = self.x * self.length
        self.rect.y = self.y * self.length
        self.mask = pygame.mask.from_surface(self.image)


class Player(Character):
    def __init__(self, x, y, length):
        self.x = x + y
        self.y = 0.5 * y - 0.5 * x - tile_width * 0.02
        global x_p
        x_p = self.x
        global y_p
        y_p = self.y

        animation_paths = {
            'idle': 'knight_sprites/Idle.png',
            'walk': 'knight_sprites/Walk.png',
            'defend': 'knight_sprites/Defend.png',
            'death': 'knight_sprites/Dead.png',
            'hurt': 'knight_sprites/Hurt.png',
            'attack': 'knight_sprites/Attack 2.png'
        }
        super().__init__(x, y, length, 'knight_sprites/Idle.png', animation_paths)
        self.image = pygame.transform.scale(self.image, (tile_width * 3.5, tile_width * 3.5))
        self.image = pygame.transform.flip(self.image, 1, 0)
        self.image = pygame.transform.rotate(self.image, 0)

        self.attack_stop = False


class Fiend(Character):
    def __init__(self, x, y, length):
        self.x = x + y
        self.y = 0.5 * y - 0.5 * x - tile_width * 0.02
        animation_paths = {
            'idle': 'fiend_sprites/Idle.png',
            'walk': 'fiend_sprites/Walk.png',
            'defend': 'fiend_sprites/Attack.png',
            'death': 'fiend_sprites/Dead.png',
            'hurt': 'fiend_sprites/Hurt.png',
            'attack': 'fiend_sprites/Attack.png'
        }
        super().__init__(x, y, length, 'fiend_sprites/Idle.png', animation_paths)
        # self.image = pygame.transform.scale(self.image, (tile_width, tile_width))
        self.image = pygame.transform.flip(self.image, 1, 0)
        self.image = pygame.transform.rotate(self.image, 0)
        self.speed = 0.005  # Скорость перемещения
        self.target_x = x
        self.target_y = y
        self.attack = False
        self.first = True

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

    def set_target(self, player):
        self.target_x = player.x_init
        self.target_y = player.y_init

    def update(self):
        dx = self.target_x - self.x_init
        dy = self.target_y - self.y_init

        distance = math.hypot(dx, dy)

        if distance > 1:
            dx /= distance
            dy /= distance

            self.x_init += dx * self.speed
            self.y_init += dy * self.speed
            self.shadow.x_init += dx * self.speed
            self.shadow.y_init += dy * self.speed
            self.moving = True
            self.look_direction = 'forward' if self.x_init > self.target_x else 'back'
        elif 0 < distance <= 1:
            self.moving = False
            if not self.attack:
                self.anim_number = 0
                self.attack = True
                global count_to_death
                # попадание
                count_to_death += 1
        super().update()


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
                floor_piece = RhombusSprite(x + y - 3, 0.5 * (y + 3) - 0.5 * (x - 6), tile_width)
                floor_piece.image.set_alpha(0)
                right_walls.add(floor_piece)
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
                floor_piece = RhombusSprite(x + y - 3, 0.5 * (y + 3) - 0.5 * (x - 6), tile_width)
                floor_piece.image.set_alpha(0)
                right_walls.add(floor_piece)
            elif level[y][x] == 'F':
                RhombusSprite(x - 3 + y, 0.5 * (y + 3) - 0.5 * (x - 6), tile_width)
                fiend = Fiend(x - 6, y + 3, tile_width)
                fiends.add(fiend)
                fiend.shadow = Shadow(fiend)
                player_group.add(fiend.shadow)
                player_group.add(fiend)
    for y in range(len(level) - 1, -1, -1):
        for x in range(len(level[y]) - 1, -1, -1):
            if level[y][x] == 'L':
                set_wall(x - 6, y + 3)
                floor_piece = RhombusSprite(x + y - 3, 0.5 * (y + 3) - 0.5 * (x - 6), tile_width)
                floor_piece.image.set_alpha(0)
                right_walls.add(floor_piece)
            elif level[y][x].isdigit():
                door = DoorSprite(x - 3 + y - 0.4 + 0.5, 0.5 * (y + 2.6) - 0.5 * (x - 6) - 1.8, tile_width)
                door.number = level[y][x]
    return player


def terminate():
    pygame.quit()
    sys.exit()


def play_cycle():
    global full_map
    global kills_count
    full_map = 0
    kills_count = 0
    global total
    total = 0
    running = True
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
    while running:
        global count_to_death
        if count_to_death == 7:
            # переход к финальному окну
            running = False
            count_to_death = 0
            total //= 2
            final_window()
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
                            if not player.attack:
                                player.attack_stop = False
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
                count_to_death = 0
            elif number == '2':
                level = load_level('map_3.txt')
                count_to_death = 0
            elif number == '3':
                full_map = 1
                final_window()
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

        for sprite in fiends:
            # print(fiend.hp)
            if player.attack:
                if pygame.sprite.collide_mask(player, sprite):
                    if not player.attack_stop:
                        sprite.hp -= 1
                        player.attack_stop = True
                if sprite.hp <= 0:
                    total += 300
                    sprite.shadow.kill()
                    sprite.kill()
                    kills_count += 1
            if not sprite.attack:
                sprite.set_target(player)

        torch_count = (torch_count + 1) % (FPS / 2)
        door_count = (door_count + 1) % (FPS / 4)
        player_count = (player_count + 1) % (FPS / 4)
        if not torch_count:
            torch_group.update()
        if not door_count:
            doors_group.update()
        if not player_count:
            player.anim_number += 1
            for fiend in fiends:
                fiend.anim_number += 1

        screen.fill('black')

        all_sprites.draw(screen)
        # right_walls.draw(screen)
        player_group.update()
        torch_group.draw(screen)
        sprites = player_group.sprites()
        sprites = sorted(sprites, key=lambda x: (x.y_init, x.x_init))
        player_group.empty()
        player_group.add(sprites)
        player_group.draw(screen)
        pygame.display.flip()


screen = pygame.display.set_mode(size)
main_window()
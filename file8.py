import pygame


def load_image(name):
    image = pygame.image.load(name)
    return image


if __name__ == '__main__':
    clock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('Игра')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    attak = [pygame.image.load("wolf_attack/Attack_1.png"),
             pygame.image.load("wolf_attack/Attack_2.png"),
             pygame.image.load("wolf_attack/Attack_3.png"),
             pygame.image.load("wolf_attack/Attack_4.png"),
             pygame.image.load("wolf_attack/Attack_5.png"),
             pygame.image.load("wolf_attack/Attack_6.png"),
             ]
    walk = [pygame.image.load("wolf_walk/walk.png"),
            pygame.image.load("wolf_walk/walk2.png"),
            pygame.image.load("wolf_walk/walk3.png"),
            pygame.image.load("wolf_walk/walk4.png"),
            pygame.image.load("wolf_walk/walk5.png"),
            pygame.image.load("wolf_walk/walk6.png"),
            pygame.image.load("wolf_walk/walk7.png"),
            pygame.image.load("wolf_walk/walk8.png"),
            pygame.image.load("wolf_walk/walk9.png"),
            pygame.image.load("wolf_walk/walk10.png"),
            pygame.image.load("wolf_walk/walk11.png"),
            ]

    count = 0
    count2 = 0
    f = False
    running = True
    while running:
        screen.blit(attak[count], (250, 250))
        screen.blit(walk[count2], (100, 250))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                f = True

        if count2 == 10:
            count2 = 0
            screen.fill((0, 0, 0))
        else:
            count2 += 1
            screen.fill((0, 0, 0))
        if f:
            if count == 5:
                count = 0
                f = False
                screen.fill((0, 0, 0))
            else:
                count += 1
                screen.fill((0, 0, 0))
        clock.tick(13)

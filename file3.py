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
    attak = [pygame.image.load("attack/Attack 6.png"),
             pygame.image.load("attack/Attack 2.png"),
             pygame.image.load("attack/Attack 3.png"),
             pygame.image.load("attack/Attack 4.png"),
             pygame.image.load("attack/Attack 5.png"),
             ]
    attak_2 = [pygame.image.load("attack/Attack 6.png"),
               pygame.image.load("attack 3/Attack 3.png"),
               pygame.image.load("attack 3/Attack 4.png"),
               pygame.image.load("attack 3/Attack 5.png"),
               pygame.image.load("attack 3/Attack 6.png")
               ]
    count2 = 0
    f2 = False
    count = 0
    f = False
    a = "attak"
    running = True
    while running:
        if a == "attak":
            screen.blit(attak[count], (200, 200))
        else:
            screen.blit(attak_2[count2], (200, 200))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                f = True
                a = "attak"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                f2 = True
                a = "attak 2"
        if f:
            if count == 4:
                count = 0
                f = False
                screen.fill((0, 0, 0))
            else:
                count += 1
                screen.fill((0, 0, 0))
        if f2:
            if count2 == 3:
                count2 = 0
                f2 = False
                screen.fill((0, 0, 0))
            else:
                count2 += 1
                screen.fill((0, 0, 0))

        clock.tick(12)

import pygame


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
    hurt = [pygame.image.load("hero_hurt/Hurt.png"),
            pygame.image.load("hero_hurt/Hurt2.png")
            ]
    dead = [pygame.image.load("hero_dead/Dead.png"),
            pygame.image.load("hero_dead/Dead1.png"),
            pygame.image.load("hero_dead/Dead2.png"),
            pygame.image.load("hero_dead/Dead3.png"),
            pygame.image.load("hero_dead/Dead4.png"),
            pygame.image.load("hero_dead/Dead5.png"),
            ]
    character = pygame.image.load("attack/Attack 6.png")
    count = 0
    count2 = 0
    count3 = 0
    x = 100
    y = 250
    f = False
    running = True
    h = True
    while running:
        screen.fill((0, 0, 0))
        character2 = pygame.transform.flip(character, True, False)
        character3 = pygame.image.load("Attack 1_red.png")
        if h:
            screen.blit(character2, (300, 250))
        else:
            screen.blit(pygame.transform.flip(dead[0], True, False), (350, 250))
            screen.fill((0, 0, 0))
            screen.blit(pygame.transform.flip(dead[1], True, False), (350, 250))
            screen.fill((0, 0, 0))
            screen.blit(pygame.transform.flip(dead[2], True, False), (350, 250))
            screen.fill((0, 0, 0))
            screen.blit(pygame.transform.flip(dead[3], True, False), (350, 250))
            screen.fill((0, 0, 0))
            screen.blit(pygame.transform.flip(dead[4], True, False), (350, 250))
            screen.fill((0, 0, 0))
            screen.blit(pygame.transform.flip(dead[5], True, False), (350, 250))
        screen.blit(walk[count], (x, y))
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if x < 280:
            if count == 10:
                x += 10
                count = 0
                screen.fill((0, 0, 0))
                screen.blit(walk[count], (x, y))
                screen.blit(character2, (300, 250))
            else:
                x += 10
                count += 1
                screen.fill((0, 0, 0))
                screen.blit(walk[count], (x, y))
                screen.blit(character2, (300, 250))
        else:
            if count2 == 5:
                if count3 == 3:
                    count2 = 0
                    screen.fill((0, 0, 0))
                    screen.blit(attak[count2], (x, y))
                    screen.blit(pygame.transform.flip(hurt[0], True, False), (350, 250))
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.transform.flip(hurt[0], True, False), (350, 250))
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.transform.flip(hurt[0], True, False), (350, 250))
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.transform.flip(hurt[0], True, False), (350, 250))
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.transform.flip(hurt[0], True, False), (350, 250))
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.transform.flip(hurt[1], True, False), (350, 250))
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.transform.flip(hurt[1], True, False), (350, 250))
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.transform.flip(hurt[1], True, False), (350, 250))
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.transform.flip(hurt[1], True, False), (350, 250))
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.transform.flip(hurt[1], True, False), (350, 250))
                    count3 += 1
                    h = False
                elif count3 < 3:
                    count2 = 0
                    screen.fill((0, 0, 0))
                    screen.blit(attak[count2], (x, y))
                    screen.blit(pygame.transform.flip(hurt[0], True, False), (350, 250))
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.transform.flip(hurt[0], True, False), (350, 250))
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.transform.flip(hurt[0], True, False), (350, 250))
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.transform.flip(hurt[0], True, False), (350, 250))
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.transform.flip(hurt[0], True, False), (350, 250))
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.transform.flip(hurt[1], True, False), (350, 250))
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.transform.flip(hurt[1], True, False), (350, 250))
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.transform.flip(hurt[1], True, False), (350, 250))
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.transform.flip(hurt[1], True, False), (350, 250))
                    screen.fill((0, 0, 0))
                    screen.blit(pygame.transform.flip(hurt[1], True, False), (350, 250))
                    count3 += 1
            else:
                count2 += 1
                screen.fill((0, 0, 0))
                screen.blit(character2, (300, 250))
                screen.blit(attak[count2], (x, y))
        clock.tick(15)
        pygame.display.update()

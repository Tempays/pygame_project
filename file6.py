import pygame
import sys


def load_image(name):
    image = pygame.image.load(name)
    return image


pygame.init()
button_surface = pygame.Surface((150, 50))
button_font = pygame.font.Font(None, 24)
button_text = button_font.render("Играть", True, (0, 0, 0))
text_coord = button_text.get_rect(center=(button_surface.get_width() / 2, button_surface.get_height() / 2))
button_coord = pygame.Rect(170, 200, 150, 50)
button_surface2 = pygame.Surface((150, 50))
button_coord2 = pygame.Rect(170, 270, 150, 50)
button_text2 = button_font.render("Выход", True, (0, 0, 0))
text_coord2 = button_text.get_rect(center=(button_surface2.get_width() / 2, button_surface2.get_height() / 2))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Игра')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    screen.fill((155, 255, 155))
    fps = 144
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_coord.collidepoint(event.pos):
                    print('Играть')
                if button_coord2.collidepoint(event.pos):
                    running = False
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
        pygame.display.flip()
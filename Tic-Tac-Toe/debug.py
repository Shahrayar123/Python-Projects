import pygame

pygame.init()
font = pygame.font.Font(None, 30)


def debug(info, x, y=10):
    display_surf = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'Black')
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    display_surf.blit(debug_surf, debug_rect)


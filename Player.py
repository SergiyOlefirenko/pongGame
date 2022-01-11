import pygame


class Player():
    def __init__(self, x: int, y: int, width=20, height=40) -> None:
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.level = None
        self.points = 0

    def p_move(self, pressed_keys, mode, level):
        if mode == 'ws':
            if pressed_keys[pygame.K_s] and self.rect[1] < level.get_height() - (self.rect[3] + 5):
                self.rect.move_ip(0, +5)
            if pressed_keys[pygame.K_w] and self.rect[1] > 5:
                self.rect.move_ip(0, -5)
        elif mode == 'ud':
            if pressed_keys[pygame.K_DOWN] and self.rect[1] < level.get_height() - (self.rect[3] + 5):
                self.rect.move_ip(0, +5)
            if pressed_keys[pygame.K_UP] and self.rect[1] > 5:
                self.rect.move_ip(0, -5)

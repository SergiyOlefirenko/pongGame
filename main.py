import sys
import math
import random
import pygame
from pygame.locals import *


pygame.init()
FPS = 30
FramePerSecond = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

DISPLAYSURF = pygame.display.set_mode((300, 300))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Pong game")


class Player():
    def __init__(self, x: int, y: int, width=20, height=40) -> None:
        self.rect = pygame.rect.Rect(x, y, width, height)

    def p_move(self, pressed_keys, mode):
        if mode == 'ws':
            if pressed_keys[pygame.K_s] and self.rect[1] < DISPLAYSURF.get_height() - (self.rect[3] + 5):
                self.rect.move_ip(0, +5)
            if pressed_keys[pygame.K_w] and self.rect[1] > 5:
                self.rect.move_ip(0, -5)
        elif mode == 'ud':
            if pressed_keys[pygame.K_DOWN] and self.rect[1] < DISPLAYSURF.get_height() - (self.rect[3] + 5):
                self.rect.move_ip(0, +5)
            if pressed_keys[pygame.K_UP] and self.rect[1] > 5:
                self.rect.move_ip(0, -5)


class Ball():
    def __init__(self, surface: pygame.Surface, color, startX, startY, radius, speed, angle=random.randint(-45, 45)) -> None:
        self.surface = surface
        self.color = color
        self.angle = math.radians(angle)
        self.rect = pygame.rect.Rect(startX, startY, radius*2, radius*2)
        self.speed = speed
        self.pos = self.rect.center
        self.radius = radius

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.rect.center, int(self.rect.width/2))
    
    def update(self):
        delta_x = self.speed * math.cos(self.angle)
        delta_y = self.speed * math.sin(self.angle)
        self.pos = (round(self.pos[0] + delta_x), round(self.pos[1] + delta_y))
        self.rect.center = self.pos[0], self.pos[1]
        border = 5
        if self.rect.right >= self.surface.get_width()-border or self.rect.left <= border:
            # self.angle = math.pi - self.angle
            pass
        elif self.rect.top < border or self.rect.bottom > self.surface.get_height() - border:
            self.angle = -self.angle
        print(f"rect right: {self.rect.right}, rect left: {self.rect.left}, rect top: {self.rect.top}, rect bottom {self.rect.bottom}")
        print(f"position: {self.pos} and angle {self.angle}")
        print(f"surface {self.surface.get_width()} and {self.surface.get_height()}")



left_player = Player(5, 5)
right_player = Player(275, 5)
ball = Ball(DISPLAYSURF, GREEN, 150, 150, 5, 5)

print(DISPLAYSURF.get_height())

is_ball_in_game = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    left_player.p_move(pygame.key.get_pressed(), 'ws')
    right_player.p_move(pygame.key.get_pressed(), 'ud')
    DISPLAYSURF.fill(WHITE)
    pygame.draw.rect(DISPLAYSURF, BLACK, right_player)
    pygame.draw.rect(DISPLAYSURF, BLACK, left_player)
    ball.draw()

    if is_ball_in_game:
        ball.update()

    if ball.rect.colliderect(right_player.rect) or ball.rect.colliderect(left_player.rect):
        ball.angle = math.pi - ball.angle
        print(ball.angle)

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        is_ball_in_game = True
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        is_ball_in_game = False
        ball.pos = 150, 150


    # print(f"player rect: {P1.rect}")

    pygame.display.update()
    FramePerSecond.tick(FPS)
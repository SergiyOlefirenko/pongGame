import sys
import math
import random
import pygame
from pygame.locals import *
from Player import Player
from Ball import Ball


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

left_player = Player(5, 5)
right_player = Player(275, 5)
ball = Ball(DISPLAYSURF, GREEN, 150, 150, 5, 5)
is_ball_in_game = False


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    left_player.p_move(pygame.key.get_pressed(), 'ws', DISPLAYSURF)
    right_player.p_move(pygame.key.get_pressed(), 'ud', DISPLAYSURF)
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
        ball.reset_ball_pos((150, 150))

    if ball.rect.right > 295:
        is_ball_in_game = False
        left_player.points += 1
        print(f"Left player points: {left_player.points}")
        ball.reset_ball_pos((150, 150))

    if ball.rect.left < 5:
        is_ball_in_game = False
        right_player.points += 1
        print(f"Right player points: {right_player.points}")
        ball.reset_ball_pos((150, 150))

    # print(f"player rect: {P1.rect}")

    pygame.display.update()
    FramePerSecond.tick(FPS)

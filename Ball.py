import pygame
import random
import math

class Ball():
    def __init__(self, surface: pygame.Surface, color, startX, startY, radius, speed, angle=random.randint(-45, 45)):
        self.surface = surface
        self.color = color
        self.angle = math.radians(angle)
        self.rect = pygame.rect.Rect(startX, startY, radius*2, radius*2)
        self.speed = speed
        self.radius = radius
        print(self.angle)

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.rect.center, int(self.rect.width/2))
    
    def update(self):
        delta_x = self.speed * math.cos(self.angle)
        delta_y = self.speed * math.sin(self.angle)
        self.rect.center = (round(self.rect.center[0] + delta_x), round(self.rect.center[1] + delta_y))
        border = 5
        if self.rect.right >= self.surface.get_width()-border or self.rect.left <= border:
            # self.angle = math.pi - self.angle
            pass
        elif self.rect.top < border or self.rect.bottom > self.surface.get_height() - border:
            self.angle = -self.angle
        print(f"rect right: {self.rect.right}, rect left: {self.rect.left}, rect top: {self.rect.top}, rect bottom {self.rect.bottom}")
        print(f"position: {self.rect.center} and angle {self.angle}")
        print(f"surface {self.surface.get_width()} and {self.surface.get_height()}")
    
    def reset_ball_pos(self, level_center):
        self.rect.center = level_center
        self.angle = random.randint(-45, 45)


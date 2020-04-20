# Работа с графической библиотекой для игр и окон PyGame
# Cнежинки на экране

import pygame
import random
import sys
import time

MAX_X = 800
MAX_Y = 600
MAX_SHOW = 100
SHOW_SIZE = 64

class Show():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 3)
        self.img_num = random.randint(1, 4)
        self.image_filename = "show" + str(self.img_num) + ".png"
        self.image = pygame.image.load(self.image_filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (SHOW_SIZE, SHOW_SIZE))

    def move_show(self):
        self.y = self.y + self.speed
        if self.y > MAX_Y:
            self.y = (0 - SHOW_SIZE)

        i = random.randint(1, 3)
        if i == 1:     # Move RIGHT
            self.x += 1
            if self.x > MAX_X:
                self.x =(0-SHOW_SIZE)
        elif i == 2:   # Move LEFT
            self.x -= 1
            if self.x < (0-SHOW_SIZE):
                self.x = MAX_X

    def draw_show(self):
        screen.blit(self.image, (self.x, self.y))


def initilize_show(max_show, showfall):
    for i in range(0, max_show):
        xx = random.randint(0, MAX_X)
        yy = random.randint(0, MAX_Y)
        showfall.append(Show(xx, yy))


def check_for_exit():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()

# ---------------------- MAIN -----------------------------------
pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
bg_color = (0, 0, 0)
showfall = []

initilize_show(MAX_SHOW, showfall)

while True:
    screen.fill(bg_color)
    check_for_exit()
    for i in showfall:
        i.move_show()
        i.draw_show()
    time.sleep(0.010)
    pygame.display.flip()


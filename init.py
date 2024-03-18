import pygame

from pygame import mixer

mixer.init()

cell_size = 25
cell_number = 20

screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption("Python")

background = pygame.image.load('graphics/background.png').convert()

lives = 0


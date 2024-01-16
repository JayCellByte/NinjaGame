import pygame
import sys

pygame.init()

pygame.display.set_caption('Ninja Man')
icon = pygame.image.load('Icon.png') 
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Exits the window
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
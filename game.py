import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()

        #Sets game icon, window title, and makes window
        pygame.display.set_caption('Ninja Man')
        icon = pygame.image.load('Icon.png') 
        pygame.display.set_icon(icon)
        self.screen = pygame.display.set_mode((640, 480))

        #Sets FPS at 60
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #Exits the window
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)


Game().run()
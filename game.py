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

        #Loads Img on screen
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0, 0, 0))
        self.img_pos = [160, 260]
        self.movement = [False, False]

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))
            self.img_pos[1] += self.movement[1] - self.movement[0]
            self.screen.blit(self.img, self.img_pos)

            #Exits the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #Moves Item
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.movement[0] = True
                    if event.key == pygame.K_s:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.movement[0] = False
                    if event.key == pygame.K_s:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)


Game().run()
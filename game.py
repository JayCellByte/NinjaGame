import pygame
import sys
from scripts.entities import PhysicsEntity
from scripts.utils import load_image, load_images
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds
class Game:
    def __init__(self):
        pygame.init()

        #Sets game icon, window title, and makes window
        pygame.display.set_caption('Ninja Man')
        icon = pygame.image.load('Icon.png') 
        pygame.display.set_icon(icon)
        self.screen = pygame.display.set_mode((1200, 680))
        self.display = pygame.Surface((320, 240))

        #Sets FPS at 60
        self.clock = pygame.time.Clock()

       #Movement
        self.movement = [False, False]

        self.collision_area = pygame.Rect(50, 50, 300, 50)

        #Load assets
        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png'),
            'background': load_image('background.png'),
            'clouds': load_images('clouds')
        }

        #Spawns Clouds
        self.clouds = Clouds(self.assets['clouds'], count=16)

        #Spawns Player
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

        #Loads TileMap
        self.tilemap = Tilemap(self, tile_size=16)

        #Moves Camera
        self.scroll = [0, 0]

    def run(self):
        while True:
            self.display.blit(self.assets['background'], (0, 0))
            
            #Player Camera
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) /30
            self.scroll[1] += (self.player.rect().centery - self.display.get_width() / 2 - self.scroll[1]) /30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            #Renders Clouds
            self.clouds.update()
            self.clouds.render(self.display, offset=render_scroll)

            #Renders behind player
            self.tilemap.render(self.display, offset=render_scroll)
            
            #Player Movemet
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)

            #Exits the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #Moves Player
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_SPACE:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)


Game().run()
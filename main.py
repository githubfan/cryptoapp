import pygame
import sys
from settings import *
from level import Level
#from debug import debug


class Game:
    def __init__(self):
        pygame.init()
<<<<<<< HEAD
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        
        #This is where we need to add the name once we come up with it
        pygame.display.set_caption('GAME NAME HERE')
=======
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
>>>>>>> 802683f03f2fd9b214c4731e02d0bd6f6a3d2b1f
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            #debug('Hi')
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
      game = Game()
      game.run()
    


        




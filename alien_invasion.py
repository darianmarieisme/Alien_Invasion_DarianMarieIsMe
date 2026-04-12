'''
Final Project: Alien Invasion (Milestone 1)
Darian Marie Bruce
04/12/2026
The purpose of this milestone is to modify the base
game to change the ship's orientation and movement'''

import sys
import pygame

class AlienInvasion:
    def __init__ (self) -> None: 
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        self.running = True

    def run_game(self):
        # Game Loop

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

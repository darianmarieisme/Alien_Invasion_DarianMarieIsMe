'''
Final Project: Alien Invasion (Milestone 1)
Darian Marie Bruce
04/12/2026
this module defines the bullet class'''

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    '''Represents a projectile fired by the ship that moves across the screen'''
    def __init__(self, game: 'AlienInvasion') -> None:
        '''Initializes the bullet, sets its starting position and loads its image'''
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.bullet_w, self.settings.bullet_h)
            )
        
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        '''Updates the bullets position as it moves across the screen'''
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        '''draws the bullet on the screen'''
        self.screen.blit(self.image, self.rect)
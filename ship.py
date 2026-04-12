'''
Final Project: Alien Invasion (Milestone 1)
Darian Marie Bruce
04/12/2026
This module defines the ship class'''

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    '''This class represents the player's ship'''
    def __init__(self, game: "AlienInvasion", arsenal: 'Arsenal') -> None:
        '''Initializes the ship, loads its image, sets starting position'''
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_w, self.settings.ship_h)
            )
        

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)
        self.arsenal = arsenal

    def update(self):
        '''updates the ship's position and handles movement and weapon updates'''
        self.arsenal.update_arsenal()

        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x


    def draw(self) -> None:
        '''Draws the ship and its projectiles'''
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        '''attempts to fire bullet
        returns: true or false staus of bullet success'''
        return self.arsenal.fire_bullet()
'''
Final Project: Alien Invasion (Milestone 2)
Darian Marie Bruce
04/12/2026
This module defines the ship class'''

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    '''This class represents the player's ship and draws the ship starting on the center left of screen'''
    def __init__(self, game: "AlienInvasion", arsenal: 'Arsenal') -> None:
        '''Initializes the ship, loads its image, sets starting position'''
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.rotate(self.image, -90)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_h, self.settings.ship_w)
            )
        

        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_up = False
        self.moving_down = False
        self.arsenal = arsenal

    def _center_ship(self):
        self.rect.midleft = self.boundaries.midleft
        self.y = float(self.rect.y)

    def update(self):
        '''updates the ship's position and handles movement and weapon updates'''
        self.arsenal.update_arsenal()
        self._update_ship_movement()

    def _update_ship_movement(self) -> None:
        temp_speed = self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= temp_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed

        self.rect.y = self.y


    def draw(self) -> None:
        '''Draws the ship and its projectiles'''
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        '''attempts to fire bullet
        returns: true or false staus of bullet success'''
        return self.arsenal.fire_bullet()
    
    def check_collisions(self, other_group) -> bool:
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False
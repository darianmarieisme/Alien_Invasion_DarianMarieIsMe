'''
Final Project: Alien Invasion (Milestone 2)
Darian Marie Bruce
04/23/2026
This module defines the ship class'''

import pygame
from settings import Settings
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    '''This class represents the player's ship and draws the ship starting on the center left of screen'''
    def __init__(self, game: "AlienInvasion", arsenal: 'Arsenal') -> None:
        '''Initializes the ship, loads its image, sets starting position'''
        self.game: AlienInvasion = game
        self.settings: Settings = game.settings
        self.screen: pygame.Surface = game.screen
        self.boundaries: pygame.Rect = self.screen.get_rect()

        self.image: pygame.Surface = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.rotate(self.image, -90)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_h, self.settings.ship_w)
            )
        

        self.rect: pygame.Rect = self.image.get_rect()
        self._center_ship()
        self.moving_up: bool = False
        self.moving_down: bool = False
        self.arsenal: Arsenal = arsenal

    def _center_ship(self) -> None:
        '''Positions the ship at the vertical center of the left edge of the screen
        '''
        self.rect.midleft = self.boundaries.midleft
        self.y = float(self.rect.y)

    def update(self) -> None:
        '''updates the ship's position and handles movement and weapon updates'''
        self.arsenal.update_arsenal()
        self._update_ship_movement()

    def _update_ship_movement(self) -> None:
        '''Updates the ship's position based on player input while staying within bounds'''
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = int(self.y)


    def draw(self) -> None:
        '''Draws the ship and its projectiles'''
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        '''attempts to fire bullet
        returns: true or false staus of bullet success'''
        return self.arsenal.fire_bullet()
    
    def check_collisions(self, other_group) -> bool:
        '''Checks for a collision between the ship and another sprite group
        if a collision is detected, the ship is repositioned and true is returned
        '''
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False
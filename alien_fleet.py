'''
'''

import pygame
import random
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:

    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        # self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed
        

        self.create_fleet()

    def create_fleet(self):
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)

        x_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)


        self._create_rectangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset)

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset):
        max_cols = 8
        screen_h = self.settings.screen_h
        padding = 50
        usable_height = screen_h - 2 * padding
        spacing = alien_h * 2
        fleet_height_pixels = (fleet_h - 1) * spacing
        y_offset = (screen_h - fleet_height_pixels) // 2

        for row in range(fleet_h):
            for col in range(min(fleet_w, max_cols)):
                current_x = x_offset - alien_w * col
                current_y = padding + row * spacing

                if col % 2 == 0 or random.random() < 0.2:
                    continue

                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        screen_h = self.settings.screen_h
        half_screen = self.settings.screen_h//2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = screen_w
        return x_offset

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h) -> int:
        fleet_w = (screen_w//alien_w)
        fleet_h = ((screen_h /2)//alien_h)
        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h  % 2 == 0:
            fleet_h -=1
        else:
            fleet_h -= 2

        return int(fleet_w), int(fleet_h)
    
    def _create_alien(self, current_x: int, current_y: int) -> None:
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def _drop_alien_fleet(self) -> None:
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed  

    def update_fleet(self) -> None:
        self.fleet.update()

    def draw(self) -> None:
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group) -> dict[any, list]:
        return pygame.sprite.groupcollide(other_group, self.fleet, True, True)
    
    def check_fleet_bottom(self) -> bool:
        alien: Alien
        if not self.fleet:
            return False

        leftmost = min(self.fleet, key=lambda alien: alien.rect.left)
        return leftmost.rect.left <= 0
        
    def check_destroyed_status(self):
        return not self.fleet
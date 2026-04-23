'''
Final Project: Alien Invasion (Milestone 2)
Darian Marie Bruce
04/23/2026
This is the settings used across the project'''

from pathlib import Path

class Settings:
    '''Stores all configuration values for the game'''
    
    def __init__(self):
        '''initializes all game settings'''

        # general

        self.name: str = "Alien Invasion"
        self.screen_w: int = 1200
        self.screen_h: int = 800
        self.FPS: int = 60
        self.bg_file: Path = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        # Ship

        self.ship_file: Path = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w: int = 40
        self.ship_h: int = 60
        self.ship_speed: int = 5
        self.starting_ship_count: int = 3

        # Bullet

        self.bullet_file: Path = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound: Path = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound: Path = Path.cwd() / 'Assets' / 'sound' / 'ImpactSound.mp3'
        self.bullet_speed: float = 7
        self.bullet_w: int = 25
        self.bullet_h: int = 80
        self.bullet_amount: int = 5

        # Alien

        self.alien_file: Path = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w: int = 40
        self.alien_h: int = 40
        self.fleet_speed: float = 0.5
        self.fleet_direction: int = 1
        self.fleet_drop_speed: int = 40
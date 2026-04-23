'''
Final Project: Alien Invasion (Milestone 2)
Darian Marie Bruce
04/23/2026
this module keeps track of the stats used in the game
'''

class GameStats():
    '''This class represents the stats being kept track of in the game'''
    def __init__(self, ships_left):
        '''This game initializes the stat variables'''
        self.ships_left: int = ships_left
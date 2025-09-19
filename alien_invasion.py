import sys
import pygame # type: ignore
from settings import Settings



class AlienInvasion:
    """Overall class to mnage the game's assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings() # Create the instance of settings 


        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height) # Create the screen 
        )

        # Create a display window with dimensions being 1200 by 800 pixels 
        # and assign it to self.screen
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color 
        self.bg_color = (230, 230, 230)
    # Game is controlled by this function 
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events and act as a listener 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Fill the screen with the background color with the fill() method 
            self.screen.fill(self.bg_color)

            # Access background color when filling up the screen 
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn game visible 
            pygame.display.flip()
            self.clock.tick(60)
if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()

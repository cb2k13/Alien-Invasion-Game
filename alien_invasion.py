import sys
import pygame # type: ignore
from settings import Settings
from ship import Ship


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

        self.ship = Ship(self) # Make instance of Ship 

        # Set the background color 
        self.bg_color = (230, 230, 230)
    # Game is controlled by this function 
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
            """Respond to keypresses and mouse events"""
            # Watch for keyboard and mouse events and act as a listener 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN: # Respond when key is actually pressed down 
                    if event.key == pygame.K_RIGHT: # Check whether the right key is pressed
                         self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                         self.ship.moving_left = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                          # Move ship to the right
                        self.ship.rect.x += 1 # If right key is pressed, ship moves to the right 
            # Fill the screen with the background color with the fill() method 
            self.screen.fill(self.bg_color)


    def _update_screen(self):
            """Update images on the screen and flip to the new """
            # Access background color when filling up the screen 
            self.screen.fill(self.settings.bg_color)

            self.ship.blitme()

            # Make the most recently drawn game visible 
            pygame.display.flip()
            self.clock.tick(60)
if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()

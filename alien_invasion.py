import sys
import pygame # type: ignore
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien 

class AlienInvasion:
    """Overall class to mnage the game's assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings() # Create the instance of settings 
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height) # Create the screen 
        )
        # Create a display window with dimensions being 1200 by 800 pixels 
        # and assign it to self.screen
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self) # Make instance of Ship 
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        # Set the background color 
        self.bg_color = (230, 230, 230)
    # Game is controlled by this function 
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            
            # Get rid of bullets that have disappeared
            for bullet in self.bullets.copy():
                 if bullet.rect.bottom <= 0: # If bullet has left off screen, remove from bullets list 
                      self.bullets.remove(bullet) 
            print(len(self.bullets)) # Print to show many bullets are currently in the game

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
            """Respond to keypresses and mouse events"""
            # Watch for keyboard and mouse events and act as a listener 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
    def _check_keydown_events(self, event):
            """Respond to keypresses"""
            if event.key == pygame.K_RIGHT:
                 self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                 sys.exit()
            elif event.key == pygame.K_SPACE: # Bullets are fired with spacebar
                 self._fire_bullet()

    def _check_keyup_events(self, event):
            """Responded to key releases"""
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False 
            # Fill the screen with the background color with the fill() method 
          

    def _fire_bullet(self):
         """Create a new bullet and add it to the bullets group"""
         if len(self.bullets) < self.settings.bullets_allowed:
              new_bullet = Bullet(self) # Make instance of bullet 
              self.bullets.add(new_bullet) # add method to add it to the group bullets

    def _update_bullets(self):
         """Update position of bullets and get rid of old ones"""
         self.bullets.update()

    def _create_fleet(self):
         """Create the fleet of aliens"""
         # Spacing between aliens is one alien width 
         # Make an alien
         alien = Alien(self)
         alien_width, alien_height = alien.rect.size

         current_x, current_y = alien_width, alien_height # set initial x and y values for placement of first alien 
         while current_y < (self.settings.screen_height - 3 * alien_height): # Keep adding rows as long as y value for next row is less than screen height 
              while current_x < (self.settings.screen_width - 2 * alien_width):
                   self._create_alien(current_x, current_y)
                   current_x += 2 * alien_width

                   # Finished a row reset x value, and increment y value
                   current_x = alien_width
                   current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):  # Specificies where the alien has to be placed 
         """Create an alien and place it in the row"""
         new_alien = Alien(self)
         new_alien.x = x_position
         new_alien.rect.x = x_position
         new_alien.rect.y = y_position
         self.aliens.add(new_alien)

    def _update_screen(self):
            """Update images on the screen and flip to the new """
            # Access background color when filling up the screen 
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():  # Loop through the sprites in bullets and call draw_bullet
                 bullet.draw_bullet()
            self.ship.blitme()
            self.aliens.draw(self.screen)

            # Make the most recently drawn game visible 
            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill(self.bg_color) 
            
if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()

import pygame  # type: ignore

class Ship:
    """Class to manage the ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen # Assign the screen to ship 
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() # Call the it and give location of ship 

        # Start each ship at the very bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exaact horizontal position
        self.x = float(self.rect.x)
        # Movement flag start with the ship not moving 
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right: # Move ship right if the flag is true 
            self.rect.x += self.settings.ship_speed
        if self.moving_left:
            self.rect.x -= self.settings.ship_speed
        
        self.rect.x = self.x

    # Define blitme method to draw the image to the screen at the position 
    # specified by self.rect
    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)

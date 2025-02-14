import pygame


class Ship():
    """Models the ship the user will play as"""

    def __init__(self, ai_settings, screen):
        """Initialize the ship and its starting position"""
        self.screen = screen
        self.speed_factor = ai_settings.ship_speed_factor

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        # Why store the ship center coordinates in dedicated variables?
        # A rect's attributes only store the integer portion of a numerical value.
        # A dedicated variable for decimal values (float), will store the value, all of it.

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the ships position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.speed_factor
        
        # Update the rect object from self.center attributes
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

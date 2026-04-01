import pygame
from pygame.sprite import Sprite

class Arrow(Sprite):
    """Tworzenie i konfiguracja strzały wystrzeliwanej przez elfa"""

    def __init__(self, gi_game):
        """Tworzy obiekt strzały w aktualnym położeniu elfa"""
        super().__init__()
        self.screen = gi_game.screen
        self.settings = gi_game.settings
        self.color = self.settings.arrow_color

        #Tworzenie strzały w punkcie (0,0)
        #następnie zdefiniowanie jej prawidłowego położenia
        self.rect = pygame.Rect(0, 0, self.settings.arrow_width, self.settings.arrow_height)
        self.rect.midtop = gi_game.elf.rect.midtop

        self.y = float(self.rect.y)
    
    def update(self):
        """Ruch strzały na ekranie"""
        #Aktualizacja położenia strzały
        self.y -= self.settings.arrow_speed
        #Aktualizacjja prostokąta strzały
        self.rect.y = self.y

    def draw_arrow(self):
        """Wyświetlanie strzały na ekranie"""
        pygame.draw.rect(self.screen, self.color, self.rect)
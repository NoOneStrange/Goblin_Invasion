import pygame
from pygame.sprite import Sprite

class Arrow(Sprite):
    """Tworzenie i konfiguracja strzały wystrzeliwanej przez elfa"""

    def __init__(self, gi_game):
        """Tworzy obiekt strzały w aktualnym położeniu elfa"""
        super().__init__()
        self.screen = gi_game.screen
        self.settings = gi_game.settings

        #Wczytanie grafiki strzały i dopasowanie do aktualnych wymiarów z ustawień.
        self.image = pygame.image.load('images/arrow.png')
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.arrow_width, self.settings.arrow_height)
        )

        #Tworzenie strzały w punkcie (0,0)
        #następnie zdefiniowanie jej prawidłowego położenia
        self.rect = self.image.get_rect()
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
        self.screen.blit(self.image, self.rect)
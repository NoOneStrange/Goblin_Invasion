import pygame

class Elf:
    """Klasa przeznaczona na modyfikacje statku gracza"""

    def __init__(self, gi_game):
        """Inicjalizacja statku i jego położenia"""
        self.screen = gi_game.screen
        self.settings = gi_game.settings
        self.screen_rect = gi_game.screen.get_rect()

        self.image = pygame.image.load('images/elf.bmp')
        self.rect = self.image.get_rect()

        #Każdy nowy statek będzie na środku dołu ekranu
        self.rect.midbottom = self.screen_rect.midbottom

        #Położenie poziome statku jest przechowywane w postaci liczby zmiennoprzecinkowej
        self.x = float(self.rect.x)

        #Opcje wskazujące na porszuanie się statku
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Aktualizacja położenia statku na podstawie flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.elf_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.elf_speed

        #Uaktualnienie obiektu rect na podstawie wartości self.x
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)



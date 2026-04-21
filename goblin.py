import pygame
from pygame.sprite import Sprite

class Goblin(Sprite):
    """Utworzenie pojedynczego przeciwnika."""

    def __init__(self, gi_game):
        """Inicjacja i początkowe położenie."""
        super().__init__()
        self.screen = gi_game.screen
        self.settings = gi_game.settings

        #Zaczytanie goblinów
        self.green_goblin()
        self.red_goblin()
        self.blue_goblin()

    def green_goblin(self):
        """Utworzenie goblina zielonego (standardowa punktacja)"""
        #Wczytanie obraazu i definicja atrybutu rect
        self.image = pygame.image.load('images/goblin_green.png')
        w, h = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (w / 4, h / 4))
        self.rect = self.image.get_rect()

        #Umieszczenie goblina w pobliżu lewego górnego rogu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Przechowywanie dokładnego poziomego położenia goblina
        self.x = float(self.rect.x)
    
    def red_goblin(self):
        """Utworzenie goblina czerwonego (standardowa punktacja pomnożona przez 2)"""
        #Wczytanie obraazu i definicja atrybutu rect
        self.image = pygame.image.load('images/goblin_red.png')
        w, h = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (w / 4, h / 4))
        self.rect = self.image.get_rect()

        #Umieszczenie goblina w pobliżu lewego górnego rogu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Przechowywanie dokładnego poziomego położenia goblina
        self.x = float(self.rect.x)
    
    def blue_goblin(self):
        """Utworzenie goblina niebieskiego (standardowa punktacja pomnożona przez 4)"""
        #Wczytanie obraazu i definicja atrybutu rect
        self.image = pygame.image.load('images/goblin_blue.png')
        w, h = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (w / 4, h / 4))
        self.rect = self.image.get_rect()

        #Umieszczenie goblina w pobliżu lewego górnego rogu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Przechowywanie dokładnego poziomego położenia goblina
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """Zwraca True jeżeli goblin dotrze do krawędzi ekranu"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0) 

    def update(self):
        """Przesuwanie goblina w prawo"""
        self.x += self.settings.goblin_speed * self.settings.army_direction
        self.rect.x = self.x
import pygame
from pygame.sprite import Sprite

class Goblin(Sprite):
    """Utworzenie pojedynczego przeciwnika."""

    def __init__(self, gi_game, goblin_type='green'):
        """Inicjacja i początkowe położenie."""
        super().__init__()
        self.screen = gi_game.screen
        self.settings = gi_game.settings
        self.points = self.settings.goblin_points
        self.hit_points = 1
        self.goblin_type = goblin_type

        #Zaczytanie wybranego typu goblina
        if self.goblin_type == 'red':
            self.red_goblin()
        elif self.goblin_type == 'blue':
            self.blue_goblin()
        else:
            self.green_goblin()

    def _load_goblin_image(self, image_path):
        """Wspólna inicjalizacja grafiki i prostokąta kolizji."""
        self.image = pygame.image.load(image_path)
        w, h = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (max(1, w // 4), max(1, h // 4)))
        self.rect = self.image.get_rect()

        #Umieszczenie goblina w pobliżu lewego górnego rogu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Przechowywanie dokładnego poziomego położenia goblina
        self.x = float(self.rect.x)

    def green_goblin(self):
        """Utworzenie goblina zielonego (standardowa punktacja)"""
        self._load_goblin_image('images/goblin_green.png')
        self.points = self.settings.goblin_points
        self.hit_points = 1
        self.goblin_type = 'green'
    
    def red_goblin(self):
        """Utworzenie goblina czerwonego (standardowa punktacja pomnożona przez 2)"""
        self._load_goblin_image('images/goblin_red.png')
        self.points = self.settings.red_goblin_points
        self.hit_points = 2
        self.goblin_type = 'red'
    
    def blue_goblin(self):
        """Utworzenie goblina niebieskiego (standardowa punktacja pomnożona przez 4)"""
        self._load_goblin_image('images/goblin_blue.png')
        self.points = self.settings.blue_goblin_points
        self.hit_points = 1
        self.goblin_type = 'blue'
    
    def check_edges(self):
        """Zwraca True jeżeli goblin dotrze do krawędzi ekranu"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0) 

    def update(self):
        """Przesuwanie goblina w prawo"""
        self.x += self.settings.goblin_speed * self.settings.army_direction
        self.rect.x = self.x
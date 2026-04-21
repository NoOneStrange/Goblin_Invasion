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

        #Ustawienie jednego typu goblina (zamiast nadpisywania 3 razy).
        self.set_type(goblin_type)

    def _load_goblin(self, image_path, points):
        """Wspólna inicjalizacja grafiki, rect i punktów goblina."""
        self.image = pygame.image.load(image_path)
        w, h = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (max(1, w // 4), max(1, h // 4)))
        self.rect = self.image.get_rect()

        #Umieszczenie goblina w pobliżu lewego górnego rogu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Przechowywanie dokładnego poziomego położenia goblina
        self.x = float(self.rect.x)
        self.points = points

    def set_type(self, goblin_type):
        """Ustawienie typu goblina na podstawie nazwy."""
        type_handlers = {
            'green': self.green_goblin,
            'red': self.red_goblin,
            'blue': self.blue_goblin,
        }
        type_handlers.get(goblin_type, self.green_goblin)()

    def green_goblin(self):
        """Utworzenie goblina zielonego (standardowa punktacja)"""
        self._load_goblin('images/goblin_green.png', self.settings.goblin_points)
    
    def red_goblin(self):
        """Utworzenie goblina czerwonego (standardowa punktacja pomnożona przez 2)"""
        self._load_goblin('images/goblin_red.png', self.settings.red_goblin_points)
    
    def blue_goblin(self):
        """Utworzenie goblina niebieskiego (standardowa punktacja pomnożona przez 4)"""
        self._load_goblin('images/goblin_blue.png', self.settings.blue_goblin_points)
    
    def check_edges(self):
        """Zwraca True jeżeli goblin dotrze do krawędzi ekranu"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0) 

    def update(self):
        """Przesuwanie goblina w prawo"""
        self.x += self.settings.goblin_speed * self.settings.army_direction
        self.rect.x = self.x
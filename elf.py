import pygame

class Elf:
    """Klasa przeznaczona na modyfikacje elfiego wojownika"""

    def __init__(self, gi_game):
        """Inicjalizacja statku i jego położenia"""
        self.screen = gi_game.screen
        self.settings = gi_game.settings
        self.screen_rect = gi_game.screen.get_rect()

        #Ładowanie obrazów elfa i ich transformacja
        self.image_alive = pygame.image.load('images/elf.png')
        self.image = self.image_alive
        base_w, base_h = self.image_alive.get_size()

        self.image_dead = pygame.image.load('images/dead_elf.png')
        self.image_dead = pygame.transform.scale(self.image_dead, (base_w * 1.5, base_h * 1.5))

        self.image_scared = pygame.image.load('images/elf_scared.png')
        self.image_scared = pygame.transform.scale(self.image_scared, (base_w * 1.5, base_h * 1.5))

        self.rect = self.image.get_rect()

        #Każdy nowy elf będzie na środku dołu ekranu
        self.rect.midbottom = self.screen_rect.midbottom

        #Położenie poziome elfa jest przechowywane w postaci liczby zmiennoprzecinkowej
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Opcje wskazujące na porszuanie się elfa
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False
    
    def update(self):
        """Aktualizacja położenia elfa na podstawie flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.elf_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.elf_speed
        if self.moving_top and self.rect.top > 0:
            self.y -= self.settings.elf_speed
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.elf_speed

        #Uaktualnienie obiektu rect na podstawie wartości self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_elf(self):
        """Umieszczenie elfa na środku dolnej części ekranu"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def reset_appearance(self):
        """Przywrócenie domyślnej grafiki elfa."""
        self.image = self.image_alive

    def killed_elf(self, pause_time=2, draw_callback=None):
        """Wyświetlenie grafiki martwego elfa przez czas pauzy"""
        self.image = self.image_dead
        if draw_callback is not None:
            draw_callback()
        else:
            self.blitme()
            pygame.display.flip()
        pygame.time.delay(int(pause_time * 1000))
        self.reset_appearance()

    def forest_lost(self, pause_time=2, draw_callback=None):
        """Wyświetlenie grafiki martwego elfa przez czas pauzy"""
        self.image = self.image_scared
        if draw_callback is not None:
            draw_callback()
        else:
            self.blitme()
            pygame.display.flip()
        pygame.time.delay(int(pause_time * 1000))
        self.reset_appearance()



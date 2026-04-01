import sys
import pygame
import math

from settings import Settings
from elf import Elf
from arrow import Arrow

class GoblinInvasion:
    """Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry."""

    def __init__(self):
        """Inicjalizacja i tworzenie zasobów"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        pygame.display.set_caption("Inwazja goblinów")

        # Wczytaj tło raz, aby nie ładować pliku w każdej klatce.
        self.bg = pygame.image.load('images/bg.png').convert()
        self.bg = pygame.transform.smoothscale(
            self.bg,
            (self.settings.screen_width, self.settings.screen_height)
        )

        #Zmienne gry
        self.scroll = 0
        self.tiles = math.ceil(self.settings.screen_height / self.bg.get_height()) + 1

        self.elf = Elf(self)
        self.arrow = pygame.sprite.Group()

    def run_game(self):
        """Rozpoczęcie pętli głównej gry"""
        while True:
            self._check_events()
            self.elf.update()
            self.arrow.update()
            self._update_arrows()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Reakcja na zdarzenia wynikające z kliknięcia klawaitury i myszy"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Reakcja na wciśnięcie klawisza"""
        if event.key == pygame.K_RIGHT:
            self.elf.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.elf.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_arrow()

    def _check_keyup_events(self, event):
        """Reakcja na puszczenie klawisza"""
        if event.key == pygame.K_RIGHT:
            self.elf.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.elf.moving_left = False

    def _fire_arrow(self):
        """Tworzy nową strzałę i dodaje ją do grupy"""
        if len(self.arrow) < self.settings.arrow_allowed:
            new_arrow = Arrow(self)
            self.arrow.add(new_arrow)

    def _update_arrows(self):
        """Uaktualnia położenie strzał i usuwa niewidoczne"""
        #Uaktualnienie
        self.arrow.update()

        #Usunięcie strzał, które są poza ekranem
        for arrow in self.arrow.copy():
            if arrow.rect.bottom <= 0:
                self.arrow.remove(arrow)
    
    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
        #Rysowanie przewijalnego tła
        for i in range(0, self.tiles):
            self.screen.blit(self.bg, (0, (i - 1) * self.bg.get_height() + self.scroll))
        
        #Przewijanie tła
        self.scroll += 2
        if self.scroll >= self.bg.get_height():
            self.scroll = 0

        self.elf.blitme()

        for arrow in self.arrow.sprites():
            arrow.draw_arrow()

        pygame.display.flip()

if __name__ == '__main__':
    gi = GoblinInvasion()
    gi.run_game()
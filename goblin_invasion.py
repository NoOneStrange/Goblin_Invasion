import sys
import pygame

from settings import Settings
from elf import Elf

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

        self.elf = Elf(self)

    def run_game(self):
        """Rozpoczęcie pętli głównej gry"""
        while True:
            self._check_events()
            self.elf.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Reakcja na zdarzenia wynikające z kliknięcia klawaitury i myszy"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.elf.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.elf.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.elf.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.elf.moving_left = False
    
    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
        self.screen.fill(self.settings.bg_color)
        self.elf.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    gi = GoblinInvasion()
    gi.run_game()
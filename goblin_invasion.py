import sys
import pygame
import math

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from elf import Elf
from arrow import Arrow
from goblin import Goblin

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

        #Utworzenie egzemplarza danych statystycznych oraz klasy Scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

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
        self.goblins = pygame.sprite.Group()

        self._create_army()

        #Uruchomienie gry w stanie aktywnym
        self.game_active = False

        #Utworzenie przycisku
        self.play_button = Button(self, "Zagraj")

    def run_game(self):
        """Rozpoczęcie pętli głównej gry"""
        while True:
            self._check_events()

            if self.game_active:
                self.elf.update()
                self.arrow.update()
                self._update_arrows()
                self._update_goblins()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Rozpoczęcie nowej gry"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            #Wyzerowanie danych statystycznych gry
            self.stats.reset_stats()
            self.sb. prep_score()
            self.game_active = True

            #Przywrócenie domyślnego wyglądu elfa po poprzedniej rozgrywce
            self.elf.reset_appearance()
    
            #Usunięcie zawartości list strzał i goblinów
            self.arrow.empty()
            self.goblins.empty()

            #Utworzenie nowej armi i wyśrodkowanie elfa
            self._create_army()
            self.elf.center_elf()

            #Ukrycie kursora
            #pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Reakcja na wciśnięcie klawisza"""
        if event.key == pygame.K_RIGHT:
            self.elf.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.elf.moving_left = True
        elif event.key == pygame.K_UP:
            self.elf.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.elf.moving_bottom = True
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
        elif event.key == pygame.K_UP:
            self.elf.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.elf.moving_bottom = False

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

        self._check_arrow_goblin_collisions()

    def _check_arrow_goblin_collisions(self):
        """Reakcja na kolizję między strzałą a goblinem"""
        #Sprawdzenie trafienia i jeżeli wystąpiło, usunięcie strzały i przeciwnika
        collisions = pygame.sprite.groupcollide(self.arrow, self.goblins, True, True)
    
        if not self.goblins:
            #Pozbycie się istniejących strzał i utworzenie nowej armi
            self.arrow.empty()
            self._create_army()

        if collisions:
            for goblins in collisions.values():
                self.stats.score += self.settings.goblin_points * len(goblins)
            self.sb.prep_score()
            self.sb.check_high_score()
 
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
        self.goblins.draw(self.screen)

        for arrow in self.arrow.sprites():
            arrow.draw_arrow()

        #Wyświetlanie punktacji
        self.sb.show_score()

        #Wyświetlenie przycisku jeżeli gra jest nieaktywna
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _elf_hit(self):
        """Reakcja na uderzenie goblina w elfa"""
        if self.stats.elfs_left > 0:
            self.stats.elfs_left -= 1

            self.elf.killed_elf(2, self._update_screen)

            self.arrow.empty()
            self.goblins.empty()

            self._create_army()
            self.elf.center_elf()
        else:
            self.elf.image = self.elf.image_dead
            self.game_active = False

    def _forest_lost(self):
        """Reakcja na przejęcie lasu"""
        if self.stats.elfs_left > 0:
            self.stats.elfs_left -= 1

            self.elf.forest_lost(2, self._update_screen)

            self.arrow.empty()
            self.goblins.empty()

            self._create_army()
            self.elf.center_elf()
        else:
            self.elf.image = self.elf.image_scared
            self.game_active = False

    def _check_goblins_bottom(self):
        """Sprawdzenie czy goblin dotarł do dolnej krawędzi ekranu"""
        for goblin in self.goblins.sprites():
            if goblin.rect.bottom >= self.settings.screen_height:
                self._forest_lost()
                break

    def _create_army(self):
        """Utworzenie armi goblinów"""
        goblin = Goblin(self)
        goblin_width, goblin_height = goblin.rect.size

        current_x, current_y = goblin_width, goblin_height
        while current_y < (self.settings.screen_height - 5 * goblin_height):
            while current_x < (self.settings.screen_width - 2 * goblin_width): #Gdyby ograniczyć się do pierwszej części nawiasu, jeden goblin będzie za prawą stroną ekranu, stąd margines
                self._create_goblin(current_x, current_y)
                current_x += 2 * goblin_width

            #Wyzerowanie x oraz zejście niżej y przy końcu rzędu
            current_x = goblin_width
            current_y += 2 * goblin_height

    def _create_goblin(self, x_position, y_position):
        """Tworzenie goblina w rzędzie"""
        new_goblin = Goblin(self)
        new_goblin.x = x_position
        new_goblin.rect.x = x_position
        new_goblin.rect.y = y_position
        self.goblins.add(new_goblin)
    
    def _update_goblins(self):
        """Uaktualnienie położenia goblinów"""
        self._check_army_edges()
        self.goblins.update()

        if pygame.sprite.spritecollideany(self.elf, self.goblins):
            print("Elfi łucznik został pokonany!!!")
            self._elf_hit()

        #Wyszukanie goblinów którzy przekroczą las
        self._check_goblins_bottom()

    def _check_army_edges(self):
        """Reakcja na dotarcie goblina do krawędzi"""
        for goblin in self.goblins.sprites():
            if goblin.check_edges():
                self._change_army_direction()
                break

    def _change_army_direction(self):
        """Przesunięcie armi w dó i zmiana kierunku jej poruszania się"""
        for goblin in self.goblins.sprites():
            goblin.rect.y += self.settings.army_drop_speed
        self.settings.army_direction *= -1

if __name__ == '__main__':
    gi = GoblinInvasion()
    gi.run_game()
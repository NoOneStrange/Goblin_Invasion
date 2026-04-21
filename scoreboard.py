import pygame.font

class Scoreboard:
    """Klasa przeznaczona do przedstawienia informacji o punktacji"""

    def __init__(self, gi_game):
        self.screen = gi_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = gi_game.settings
        self.stats = gi_game.stats

        #Czcionka
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #Początkowa punktacja
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Przekształcenie punktacji na wygenerowany obraz"""
        rounded_score = round(self.stats.score, -1) #Zaokrąglenie punktacji na wypadek edycji trudności i dodania mnożnika punktów z levela
        score_str = f'{rounded_score}'
        self.score_image = self.font.render(score_str, True, 
                                            self.text_color, self.settings.bg_color)
        
        #Wyświetlanie punktacji w prawym górnym rogu
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """"Konwersja najlepszego wyniku na wygenerowany obraz"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f'{high_score}'
        self.high_score_image = self.font.render(high_score_str, True, 
                                                 self.text_color, self.settings.bg_color)
        
        #Wyświetlanie najlepszego wyniku na środku przy górnej krawędzi
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Sprawdzenie czy wynik został pobity"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Konwersja numeru poziomu na wygenerowany obraz"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        #Numer poziomu wyświetlany pod aktualną punktacją
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        """Wyświetlanie punktacji na ekranie"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
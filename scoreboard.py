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

    def prep_score(self):
        """Przekształcenie punktacji na wygenerowany obraz"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, 
                                            self.text_color, self.settings.bg_color)
        
        #Wyświetlanie punktacji w prawym górnym rogu
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Wyświetlanie punktacji na ekranie"""
        self.screen.blit(self.score_image, self.score_rect)

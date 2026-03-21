class Settings:
    """Przchowywanie ustawień gry"""

    def __init__(self):
        """Inicjalizacja ustawień"""
        #Ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Ustawienia elfa
        self.elf_speed = 1.5

        #Ustawienia strzały
        self.arrow_speed = 2.0
        self.arrow_width = 3
        self.arrow_height = 15
        self.arrow_color = (60, 60, 60)


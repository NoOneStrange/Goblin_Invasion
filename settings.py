class Settings:
    """Przchowywanie ustawień gry"""

    def __init__(self):
        """Inicjalizacja ustawień"""
        #Ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 760
        self.bg_color = (34, 139, 34)

        #Ustawienia elfa
        self.elf_speed = 5.0

        #Ustawienia strzały
        self.arrow_speed = 6.0
        self.arrow_width = 3
        self.arrow_height = 15
        self.arrow_color = (150, 75, 0)
        self.arrow_allowed = 10


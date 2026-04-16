class Settings:
    """Przchowywanie ustawień gry"""

    def __init__(self):
        """Inicjalizacja ustawień"""
        #Ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 760
        self.bg_color = (34, 139, 34)

        #Ustawienia elfa
        self.elf_speed = 4.0
        self.elf_limit = 3

        #Ustawienia strzały
        self.arrow_speed = 6.0
        self.arrow_width = 6
        self.arrow_height = 20
        self.arrow_color = (150, 75, 0)
        self.arrow_allowed = 8

        #Ustawienia goblina
        self.goblin_speed = 1.5
        self.army_drop_speed = 20
        #direction 1 ruch w prawo, -1 ruch w lewo
        self.army_direction = 1

        #Inicjalizacja ustawień dynamicznych (m.in. punktacji)
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        
        #Punktacja
        self.goblin_points = 50






class GameStats:
    """Monitorowanie danych statystycznych w grze"""

    def __init__(self, gi_game):
        """Inicjalizacja danych statystycznych"""
        self.settings = gi_game.settings
        self.reset_stats()

    def reset_stats(self):
        """
        Inicjalizacja danych statystycznych, które mogą zmienić się w trakcie gry
        """
        self.elfs_left = self.settings.elf_limit
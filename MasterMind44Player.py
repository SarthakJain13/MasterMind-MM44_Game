class Mastermind44Player():
    """
    MasterMind44Player class is the sub-class MasterMind44 game of abstract class MasterMind.
    """
    def __init__(self, playerName, position, color):
        """
        """
        self.playerName = playerName
        self.position = position
        self.color = color
    attempts = []
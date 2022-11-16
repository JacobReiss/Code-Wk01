import random

class Puzzle:
    """The random word
    
    The purpose of the Puzzle is generate a random word to use for the game.
    
    Attributes:
        options (List): The list of words to pick from
        word (str): The word that is picked
    """
    
    def __init__(self):
        """Constructs a new Puzzle
        
        Args:
            self (Puzzle): An instance of Puzzle
        """
        self._options = []
        self._word = ""
    
    def get_word(self):
        """Constructs a new Puzzle

        Returns:
            string: This is the random number to be used
        """
        self._options = ["word", "pest", "main", "pack"]
        self._word = random.choice(self._options)
        return self._word


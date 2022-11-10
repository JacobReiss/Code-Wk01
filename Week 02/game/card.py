import random

class Card:
    """ The game for HiLo
    
    The responsibility of HiLo is to control the game and how it works
        
    Attributes:
        card1 (int): This is the value for card 1
        card2 (int): This is the value for card 2
        turn (int): This determines if card 1 will generate it's own number or if it will use card 2
    """
    
    def __init__(self):
        """Constructs a new Card.
        
        Args:
            self (Director): an instance of Card.
        """
        self.card1 = 0
        self.card2 = 0
        self.turn = 0
        
    def cardOne(self):
        """Constructs Card One. Takes Card Two's number after the first round
        
        Args:
            self (Director): an instance of Director.
        """
        if self.turn == 0:
            self.card1 = random.randint(1,13)
        else:
            self.card1 = self.card2
        
        
    def cardTwo(self):
        """Constructs Card Two. Sets turn to 1 so Card One will now use this output
        
        Args:
            self (Director): an instance of Director.
        """
        self.card2 = random.randint(1,13)
        self.turn = 1
        
    
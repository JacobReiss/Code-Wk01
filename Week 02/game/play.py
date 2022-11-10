from game.card import Card

class Hilo:
    """ The game for HiLo
    
    The responsibility of HiLo is to control the game and how it works
    
    Attributes:
        card (class): A call to the Card class in game.card.py
        choice (string): A string to signify the user's hilo preference
        score (int): The user's score, starting at 300
        isPlaying (string): Variable to determine if the game is still being played
    """
    
    
    def __init__(self):
        """Constructs a new Hilo.
        
        Args:
            self (Director): an instance of Hilo.
        """
        self.card = Card()
        self.choice = ""
        self.score = 300
        self.isPlaying = 1
        
    def playGame(self):
        """Starts the Hilo game.
        
        Args:
            self (Director): an instance of Director.
        """
        # Starts a loop so the game will end when the user says or runs out of points
        while self.isPlaying > 0:
            
            self.getCardOne()
            self.getInputs()
            self.getCardTwo()
            self.getCalculations()
            self.getOutputs()
            
    def getCardOne(self):
        """Constructs Card One.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card.cardOne()
        self.one = self.card.card1
        print (f"\n\nThe card is: {self.one}")
    
    def getInputs(self):
        """Gets the user input for High or Low.
        
        Args:
            self (Director): an instance of Director.
        """
        self.choice = input("High or Low (h/l) -> ")
        
    def getCardTwo(self):
        """Constructs Card Two.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card.cardTwo()
        self.two = self.card.card2
        print (f"Next card is: {self.two}")
    
    def getCalculations(self):
        """Calulates the new score based on the user input and card one compared to card two.
        
        Args:
            self (Director): an instance of Director.
        """
        if self.choice == "l":
            if self.one > self.two:
                self.score += 100
            else:
                self.score -= 75
            
        elif self.choice == "h":
            if self.one < self.two:
                self.score += 100
            else:
                self.score -= 75
    
    def getOutputs(self):
        """Complies the output of the game. Determines if the game will continue or not.
        
        Args:
            self (Director): an instance of Director.
        """
        print(self.score)
        if self.score <= 0:
            self.isPlaying = 0
            print ("You ran out of points... Game Over\n")
        else:
            cont = input("Keep playing (y/n) -> ")
            if cont == "y" or cont == "Y":
                pass
            else:
                self.isPlaying = 0
    
    
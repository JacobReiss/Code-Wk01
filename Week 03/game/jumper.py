from game.puzzle import Puzzle

class Jumper:
    """The jumper man.
    
    The responsibilty of the jumper is correctly guess the word before his parachute disappears
    
    Attributes:
        man (List): The list to store the jumper
        guess_list (List): The list to store the correct guesses
        puzzle (Puzzle): The Puzzle class
        word (str): The random word selected
    """
    def __init__(self):
        """Constructs a new Jumper
        
        Args:
            self (Jumper): An instance of Jumper
        """
        self._man = [
            "                         ___                          ", #0
            "                        /___\                         ", #1
            "                        \   /                         ", #2
            "                         \ /                          ", #3
            "                          O                           ", #4          
            "                         /|\                          ", #5
            "                         / \                          ", #6
            "                      ^^^^^^^^^                       ", #7
        ]
        self._guess_list = [" _ ", " _ ", " _ ", " _ "]
        self._puzzle = Puzzle()
        self._word = self._puzzle.get_word()
            
    def draw_man(self, list):
        """Constructs a new man
        
        Args:
            self (Jumper): An instance of Jumper
        """
        for i in range(len(list)):
            print (list[i])
            
    def check_answer(self, answer):
        """Checks the correct answer
        
        Args:
            self (Jumper): An instance of Jumper
            answer (str): The letter that has been guessed
        """
        word_list = list(self._word)
        if answer in self._word:
            print ("\nThat is in the word")
            index = word_list.index(answer)
            self._guess_list[index] = answer
            
            
        else:
            print ("\nNot in the word")
            self._man.pop(0)
            
    def is_out(self, list, answer):
        """Checks if the game is over
        
        Args:
            self (Jumper): An instance of Jumper
            list (List): The current guess list
            answer (str): The correct word

        Returns:
            boolean: Whether the game is over or not
        """
        concat_word = "".join(self._guess_list)
        if len(list) == 4:
            print (f"\nSorry, the word is {answer.upper()}\n")
            return True
        elif concat_word == answer:
            print (f"\nCongrats, the word is {answer.upper()}\n")
            return True
from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        puzzle (Puzzle): The game's random word.
        is_playing (boolean): Whether or not to keep playing.
        jumper (Jumper): The game's jumper.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._is_playing = True
        self._puzzle = Puzzle()
        self._terminal_service = TerminalService()
        self._x = 0
        self._letter = ""
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Gets the user's guess.

        Args:
            self (Director): An instance of Director.
        """
        
        if self._x == 0:
            self._jumper.draw_man(self._jumper._man)
            print ()
            print (*self._jumper._guess_list)
            self._x = 1
        self._letter = self._terminal_service.read_text("\nEnter a letter ->  ")
        
        
    def _do_updates(self):
        """Updates whether or not the guess is in the word.

        Args:
            self (Director): An instance of Director.
        """
        self._jumper.check_answer(self._letter)
        
        
    def _do_outputs(self):
        """Displays output.

        Args:
            self (Director): An instance of Director.
        """     
        self._jumper.draw_man(self._jumper._man)
        print ()
        print (*self._jumper._guess_list)
        if self._jumper.is_out(self._jumper._man, self._jumper._word):
            self._is_playing = False
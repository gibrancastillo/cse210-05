from game.parachute import Parachute
from game.puzzle import Puzzle
from game.seeker import Seeker
from game.terminal_service import TerminalService

class Director:
    """
    A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _game_over_message (str): Enhanced game over message.
        _game_play_message (str): Enhanced game play message.
        _is_playing (boolean): Whether or not to keep playing.
        _parachute (Parachute): The game's Parachute.
        _puzzle (Puzzle): The game's Puzzle.
        _seeker (Seeker): The game's Seeker.
        _terminal_service (TerminalService): For getting and displaying information on the terminal.
    """

    def __init__(self):
        """
        Constructs a new Director.
        
        Args:
            self (Director): An instance of Director.
        """
        self._game_over_message = "\n ------- Good game. Thanks for playing! -------\n"
        self._game_play_message = "\n ------- Have fun playing the 'Jumper Game' -------\n"
        self._is_playing = True
        self._parachute = Parachute()
        self._puzzle = Puzzle()
        self._seeker = Seeker()
        self._terminal_service = TerminalService()
    

    def start_game(self):
        """
        Starts the game by running the main game loop.
        
        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.write_text(self._game_play_message)
        self._display_guessed_letters()
        self._display_parachute()

        while self._is_playing:
            self._prompt_to_guess_a_letter()
            self._do_updates()
            self._display_guessed_letters()
            self._display_parachute()
            self._is_the_game_over()
        
        self._terminal_service.write_text(self._game_over_message)
    

    def _display_guessed_letters(self):
        """
        Display the chosen secret word place holders "_" with any of the letters that have been guessed correctly.
        
        Args:
            self (Director): An instance of Director.
        """
        self._puzzle.display_status()
    

    def _display_parachute(self):
        """
        Display the player's Parachute.
        
        Args:
            self (Director): An instance of Director.
        """
        self._parachute.draw_parachute()


    def _prompt_to_guess_a_letter(self):
        """
        Prompt the player to guess a letter.
        
        Args:
            self (Director): An instance of Director.
        """
        lowercase_alphabet_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        new_letter = self._terminal_service.read_letter("\nGuess a letter [a-z]: ")

        # Enhanced input validation.
        while(new_letter not in(lowercase_alphabet_letters)):
            new_letter = self._terminal_service.read_letter("\nGuess a letter [a-z], You must enter a letter from the alphabet: ")

        self._seeker.letter_guessed(new_letter)


    def _do_updates(self):
        """
        Guesses a letter in the Puzzle.
        
        Args:
            self (Director): An instance of Director.
        """
        self._puzzle.guess_a_letter(self._seeker, self._parachute)


    def _is_the_game_over(self):
        """
        Whether or not the Puzzle is solve or the player's Parachute is out of line.
        
        Args:
            self (Director): An instance of Director.
        """
        # Check if player has more parachute
        if self._parachute.is_out_of_line():
            self._is_playing = False
            self._game_over_message = "\n ------- Game Over: You Loose. Thanks for playing! -------\n"
        elif self._puzzle.is_solved():
            self._is_playing = False
            self._game_over_message = "\n ------- Game Over: Woot woot, You Win. Hooray!! Thanks for playing! -------\n"
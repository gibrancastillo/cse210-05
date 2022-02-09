from game.parachute import Parachute
from game.puzzle import Puzzle
from game.seeker import Seeker
from game.terminal_service import TerminalService

class Director:
    def __init__(self):
        self._is_playing = True
        self._parachute = Parachute()
        self._puzzle = Puzzle()
        self._seeker = Seeker()
        self._terminal_service = TerminalService()
    
    def start_game(self):
        while self._is_playing:
            self._display_guessed_letters()
            self._display_parachute()
            self._guess_a_letter()
            self._do_updates()
            self._do_outputs()

    def _display_guessed_letters(self):
        self._puzzle.get_guessed_letters()
    
    def _display_parachute(self):
        self._parachute.draw_parachute()

    def _guess_a_letter(self):
        new_letter = self._terminal_service.read_letter("\nGuess a letter [a-z]: ")
        self._seeker.set_guessed_letter(new_letter)

    def _do_updates(self):
        self._puzzle.guess_a_letter(self._seeker, self._parachute)

    def _do_outputs(self):
        # Check if player has more parachute
        if self._parachute.is_out_of_line():
            self._is_playing = False
        elif self._puzzle.is_solved():
            self._is_playing = False
        
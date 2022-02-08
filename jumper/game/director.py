<<<<<<< HEAD
import imp
from parachute import Parachute
from puzzle import Puzzle
from seeker import Seeker
from terminal_service import TerminalService

class Director:
    def __init__(self):
        self._is_playing = True
        self._parachute = Parachute()
        self._puzzle = Puzzle()
        self._seeker = Seeker()
        self._terminal_service = TerminalService()
    
    def start_game(self):
        while self._is_playing:
            self._display_parachute()
            self._guess_a_letter()
            self._do_updates()
            self._do_outputs()

    def _display_parachute(self):
        self._parachute.draw_parachute()

    def _guess_a_letter(self):
        new_letter = self._terminal_service.read_letter("\nGuess a letter [a-z]: ")
        self._seeker (new_letter)

    def _do_updates(self):
        pass

    def _do_outputs(self):
        pass
=======
class Director:
    def __init__(self):
        pass

    def start_game(self):
        print("Start Jumper Game")
>>>>>>> 40ce55f94584420cbb1ad2ed5e5f6d4d04e9a3fa

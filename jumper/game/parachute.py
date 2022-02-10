from game.terminal_service import TerminalService

class Parachute:
    """
    The player's parachute lines.
    
    The responsibility of Parachute is to draw the parachute, 
    keep track of its lines, and cut them when appropriate.

    Attributes:
        _is_out_of_line (boolean): The flag to determine if the parachute has no more parachute.
        _parachute_list (List[str]): The parachute lines and the person.
        _terminal_service (TerminalService): For getting and displaying information on the terminal.
    """
    

    def __init__(self):
        """
        Constructs a new Parachute.

        Args:
            self (Parachute): An instance of Parachute.
        """
        self._is_out_of_line = False
        self._parachute_list = [ "  ___   ", 
                                 " /___\\ ", 
                                 " \   /  ", 
                                 "  \ /   ", 
                                 "   O    ", 
                                 "  /|\\  ", 
                                 "  / \\  ", 
                                 "        ",
                                 "^^^^^^^ " ]
        self._terminal_service = TerminalService()
    

    def draw_parachute(self):
        """
        Draws the player's parachute.

        Args:
            self (Parachute): An instance of Parachute.
        """
        self._terminal_service.write_text("")

        if self._parachute_list[0] == "   O    ":
            # replace first value
            self._parachute_list[0] = "   x    "

        for parachute in self._parachute_list:
            self._terminal_service.write_text(parachute)
    

    def cut_line(self):
        """
        Cuts the top line on the player's parachute.

        Args:
            self (Parachute): An instance of Parachute.
        """
        if self._parachute_list[0] == "   x    ":
            self._is_out_of_line = True
        self._parachute_list.pop(0)
    
    
    def is_out_of_line(self):
        """
        Whether or not the player's Parachute is out of line.

        Args:
            self (Parachute): An instance of Parachute.
        
        Returns:
            boolean: True if the player's parachute is out line; false if otherwise.
        """
        if self._parachute_list[0] == "   x    ":
            self._is_out_of_line = True
        return self._is_out_of_line
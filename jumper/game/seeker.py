import random

class Seeker:
    """
    The player trying to solve the Puzzle. 
    
    The responsibility of a Seeker is to solve the Puzzle before he runs out of Parachute line.
    
    Attributes:
        _guessed_letter (str): The guessed letter of the Seeker (a-z).
    """

    
    def __init__(self):
        """
        Constructs a new Seeker.
        
        Args:
            self (Seeker): An instance of Seeker.
        """
        self._guessed_letter = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    

    def get_guessed_letter(self):
        """
        Gets the current guessed letter.
        
        Args:
            self (Seeker): An instance of Seeker.

        Returns:
            letter: The current guessed letter.
        """
        return self._guessed_letter


    def letter_guessed(self, guessed_letter):
        """
        Guesses a letter.
        
        Args:
            self (Seeker): An instance of Seeker.
            guessed_letter (str): The guessed letter.
        """
        self._guessed_letter = guessed_letter
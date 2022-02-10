import random
from game.terminal_service import TerminalService

class Puzzle:
    """
    The Puzzle hiding the secret word from the Seeker. 
    
    The responsibility of Puzzle is to keep track of the letters the secret word has 
    and let the Seeker see words that already have been guessed correctly. 
    
    Attributes:
        _chosen_secret_word (str): The secret word to be use for the Puzzle.
        _guessed_letters (List[str]): A list of letters guessed by the Seeker.
        _place_holders (List[str]): A list of "-" lines that hide the secret word with any guessed letter.
        _terminal_service (TerminalService): For getting and displaying information on the terminal.
        _wrong_guesses (int): A counter to keep track of the incorrect guesses.
    """


    def __init__(self):
        """
        Constructs a new Puzzle.
        
        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self._chosen_secret_word = random.choice(["charity", "honesty", "integrity", "patience", "forgiveness", "friendship", "service"])
        self._guessed_letters = []
        self._place_holders = []
        self._terminal_service = TerminalService()
        self._wrong_guesses = 0
        
        self._build_letters_place_holders()
    

    def _build_letters_place_holders(self):
        """
        Build the chosen secret word hidding place holder.
        
        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self._terminal_service.write_text("")

        #The following line and a block will be used to show place holders for the randomly chosen word
        self._list_chosen_words = list(self._chosen_secret_word)
        for i in self._list_chosen_words:
            self._place_holders.append("_")
    

    def display_status(self):
        """
        Display the chosen secret word place holders "_" with any of the letters that have been guessed correctly.
        
        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self._terminal_service.write_text("")
        # Convert the chosen secret word string into a list of letters.
        chosen_secret_word = list(self._chosen_secret_word)
        index = 0 # keep track of the for loop and the list index too.

        for i in chosen_secret_word:
            for j in self._guessed_letters:
                if i == j:
                    self._place_holders[index] = j
            index += 1
        
        for holder in self._place_holders:
            self._terminal_service.write_text_without_newline(holder)
        self._terminal_service.write_text("")
    

    def guess_a_letter(self, seeker, parachute):
        """
        The player guesses a letter in the Puzzle; in other words, uses the letter chosen by the player then
        if necessary it updates the Parachute lines and keeps track of how many wrong letters have been guessed.
        
        Args:
            self (Puzzle): An instance of Puzzle.
            seeker (pass by reference): A reference of Seeker.
            parachute (pass by reference): A reference of Parachute.
        """
        guessed_letter = seeker.get_guessed_letter()

        if guessed_letter not in self._chosen_secret_word:
            self._wrong_guesses += 1
            parachute.cut_line()
        
        self._guessed_letters.append(guessed_letter)
    

    def is_solved(self):
        """
        Whether or not the Puzzle is solve.
        
        Args:
            self (Puzzle): An instance of Puzzle.
        
        Returns:
            boolean: True if the Puzzle is solved; false if otherwise.
        """
        count = 0
        
        for i in self._place_holders:
            if i == "_":
                count += 1
           
        if count == 0:
            return True
        else:
            return False
    
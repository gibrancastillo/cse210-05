import random
from game.terminal_service import TerminalService

class Puzzle:
    """

    This Class holds all the puzzle that will be in the game 

    """

    def __init__(self):
        self._chosen_secret_word = random.choice(["charity", "honesty", "integrity", "patience", "forgiveness", "friendship", "service"])
        self._guessed_letters = []
        self._place_holders = []
        self._terminal_service = TerminalService()
        self._wrong_guesses = 0
        
        self._build_letters_place_holders()

        
    def _build_letters_place_holders(self):
        self._terminal_service.write_text("")

        #The following line and a block will be used to show place holders for the randomly chosen word
        self._list_chosen_words = list(self._chosen_secret_word)
        for i in self._list_chosen_words:
            self._place_holders.append("_")
    

    def get_guessed_letters(self):
        """

        This function helps the player know how many letters the word has and let them see words
        that already have been guessed correctly

        """
        self._terminal_service.write_text("")

        #the following line makes the chosen word into a list of letters
        chosen_secret_word = list(self._chosen_secret_word)

        #index is for keeping track of the for loop and the list index too
        index = 0 
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

        This function helps the player to choose a letter then it updates the parachute lines 
        and keeps track of how many wrong letters have been guessed

        """
        guessed_letter = seeker.get_guessed_letter()
        if guessed_letter not in self._chosen_secret_word:
            self._wrong_guesses += 1
            parachute.cut_line()
        self._guessed_letters.append(guessed_letter)
    
    def is_solved(self):
        """

        This function checks if the game has been won or not
        
        Return: Boolean

        """
        #The nested loop is for checking if the game has been won
        count = 0
        
        for i in self._place_holders:
            if i == "_":
                count += 1
           
        if count == 0:
            return True
        else:
            return False
    
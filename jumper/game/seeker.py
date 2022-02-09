import random

class Seeker:
    def __init__(self):
        self._gussed_letter = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    
    def get_guessed_letter(self):
        return self._gussed_letter

    def set_guessed_letter(self, gussed_letter):
        self._gussed_letter = gussed_letter
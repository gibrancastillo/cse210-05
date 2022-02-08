import random

class Puzzle:
    def __init__(self):
        self._secret_word = random.choice(["charity", "honesty", "integrity", "patience", "forgiveness", "friendship", "service"])
        #self._revealed_letters = 
    
    def _chosen_secret_word(self):
        print(f"self._secret_word: {self._secret_word}")
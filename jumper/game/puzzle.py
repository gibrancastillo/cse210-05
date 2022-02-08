import random

# class Puzzle:
#     def __init__(self):
#         self._secret_word = random.choice(["charity", "honesty", "integrity", "patience", "forgiveness", "friendship", "service"])
#         #self._revealed_letters = 
    
#     def _chosen_secret_word(self):
#         print(f"self._secret_word: {self._secret_word}")

class Puzzle:

    def __init__(self):
        self._words = ["charity", "honesty", "integrity", "patience", "forgiveness", "friendship", "service"]
        self._parachute_list = [ "  ___",  " /___\\", " \   /", "  \ /", "   O", "  /|\\", "  / \\", "     ", "^^^^^^^" ]
        self._gussed_letters = []
        self._chosen_secret_word = random.choice(self._words)
        self._wrong_guesses = 0
        self._place_holders = []
        list_chosen_words = list(self._chosen_secret_word)
        for i in list_chosen_words:
            self._place_holders.append("_")
        self._parachute_list = [ "  ___", 
                                 " /___\\", 
                                 " \   /", 
                                 "  \ /", 
                                 "   O", 
                                 "  /|\\", 
                                 "  / \\", 
                                 "     ",
                                 "^^^^^^^" ]

    def draw_parachute(self):
        """description Coming soon"""
        
        if len(self._parachute_list) > 0:

            if self._parachute_list[0] == "O":
                self._parachute_list[0] == "x"
        for i in self._parachute_list:
            print(i)
    
    def place_holders(self):
        """description Coming soon"""
        chosen_secret_word = list(self._chosen_secret_word)
        index = 0 
        for i in chosen_secret_word:
            for j in self._gussed_letters:
                if i == j:
                    self._place_holders[index] = j
            index += 1
        
        for i in self._place_holders:
            print(i, end=' ')
        print()
    
    def guess_a_letter(self):
        """description Coming soon"""
        letter = input("Please guess a letter: ").lower()
        if letter not in self._chosen_secret_word:
            self._wrong_guesses += 1
            self._parachute_list.pop(0)
        self._gussed_letters.append(letter)
    
    def check_status(self):
        """description Coming soon"""
        count = 0
        for i in self._place_holders:
            for j in range(len(self._chosen_secret_word)):
                if i == j:
                    count += 1
        if count == len(self._chosen_secret_word):
            return True
        else:
            return False


puzzle = Puzzle()

is_playing = True

while is_playing:
    puzzle.draw_parachute()
    puzzle.place_holders()
    puzzle.guess_a_letter()
    puzzle.draw_parachute()
    
    game_status = puzzle.check_status()

    if game_status:
        print("YOU WIN!!!, Thank you for playing!")
        break


                

            



    
        
    

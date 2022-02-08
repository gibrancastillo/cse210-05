
class Parachute:
    def __init__(self):
        #self._parachute_list = [ "  ___",  " /___\\", " \   /", "  \ /", "   O", "  /|\\", "  / \\", "     ", "^^^^^^^" ]
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
        print()
        
        for index in range(len(self._parachute_list)):
            print(self._parachute_list[index])
            
        print()


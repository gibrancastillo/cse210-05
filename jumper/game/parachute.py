class Parachute:
    def __init__(self):
        #self._parachute_list = [ "  ___",  " /___\\", " \   /", "  \ /", "   O", "  /|\\", "  / \\", "     ", "^^^^^^^" ]
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
    

    def draw_parachute(self):
        print()

        for parachute in self._parachute_list:
            print(parachute)
        
        if self._parachute_list[0] == "   O    ":
            # replace first value
            self._parachute_list[0] = "   x    "

    def cut_line(self):
        if self._parachute_list[0] == "   x    ":
            self._is_out_of_line = True
        self._parachute_list.pop(0)
    

    def is_out_of_line(self):
        return self._is_out_of_line
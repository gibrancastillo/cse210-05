class TerminalService:
    
    def read_letter(self, prompt):
        return input(prompt).lower()
    
    def write_text(self, text):
        print(text)
    
    def write_text_without_newline(self, text):
        print(text, end = " ")

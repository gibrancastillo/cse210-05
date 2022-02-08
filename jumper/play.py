import random

#parachute_list = [ "  ___",  " /___\\", " \   /", "  \ /", "   O", "  /|\\", "  / \\", "     ", "^^^^^^^" ]
parachute_list = [ "  ___", 
                   " /___\\", 
                   " \   /", 
                   "  \ /", 
                   "   O", 
                   "  /|\\", 
                   "  / \\", 
                   "     ",
                   "^^^^^^^"]

secret_word = random.choice(["charity", "honesty", "integrity", "patience", "forgiveness", "friendship", "service"])
print(f"secret_word: {secret_word}")

revealed_letters = []
print()
for index in range(len(secret_word)):
    print("-", end =" ")
    revealed_letters.append("-")

print()

for index in range(len(parachute_list)):
    print(parachute_list[index])

print()





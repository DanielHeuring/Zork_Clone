import time

#Use function [gprint("string")] to give text scrolling/typing effect
def gprint(string):
    string = string + "\n"
    for char in string:
        print(char, end='')
        time.sleep(.04)

#Use function [uinput("string")] to take user input for correct terminal organization and ">" at cursor
def uinput(string):
    output = input(string + "\n>")
    return output

loop = 1

print("---------------------------------------------------------")
print("Welcome to GAME_NAME_HERE")

while True:
    while loop == 1:
        if loop == 1:
            print("---------------------------------------------------------")
            gprint("You are standing STARTING_AREA")
            first = uinput("What do you do?")
        if first.lower() == ("POSSIBLE_INPUT_HERE"):
            print("---------------------------------------------------------")
            gprint("OUTPUT_HERE")
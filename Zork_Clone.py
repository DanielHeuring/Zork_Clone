import time
from time import sleep

#Use function [gprint("string")] to give text scrolling/typing effect
def gprint(string):
    string = string + "\n"
    for i in string:
        print(i, end='', flush = True)
        sleep(0.025)

#Use function [uinput("string")] to take user input for correct terminal organization and ">" at cursor
def uinput(string):
    output = input(string + "\n>").lower().strip()
    return output

place_list = []
#COMMON INPUTS
north = ["north", "n", "go north", "head north"]
south = []
east = []
west = []

exitDoor = ["open door", "exit", "exit room"]

location = 1

print("---------------------------------------------------------")
print("Welcome to Bulldog Brawl")

while True:
    if location == 0:
        break
    #DORM = 1
    while location == 1:
        if location == 1:
            print("---------------------------------------------------------")
            if 1 not in place_list:
                gprint("You are standing in your dorm. Your roommate, Brad, is watching TV on his bed. You desperately need help on your \nProgramming Project. In your room there is a door, a window, and your desk.")
                first = uinput("What do you do?")
                place_list.append(1)
            else:
                gprint("DORM\nBrad is still watching TV. There is a window, a door, and a desk.")
                first = uinput("")

        elif first == ("open window"):
            print("---------------------------------------------------------")
            gprint("You see the campus and feel the breeze off Lake Superior.")
            first = uinput("")
        elif first == ("jump out") or ("jump out window") or ("exit window"):
            print("---------------------------------------------------------")
            gprint("You fall to your death. What were you thinking?")
            location = 0
        elif first in exitDoor:
            print("---------------------------------------------------------")
            gprint("YOU GO TO HALLWAY ***")
            location = 2
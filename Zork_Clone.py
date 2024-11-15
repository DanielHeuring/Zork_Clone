import time
from time import sleep

#Use function [gprint("string")] to give text scrolling/typing effect
def gprint(string):
    string = string + "\n"
    for i in string:
        print(i, end='', flush = True)
        sleep(0.001) #0.02 for real game

#Use function [uinput("string")] to take user input for correct terminal organization and ">" at cursor
#NEED TO ADD > IN FRONT OF CURSOR
def uinput(string):
    print("\n")
    output = (input(string)).lower().strip()
    return str(output)

def changeLocation(newLocation):
    global prevLocation, location
    prevLocation = location
    location = int(newLocation)

def displayBackpack():
    gprint("\nBackpack:\n-------------")
    print(*backpack, sep= "\n")
    print("\n")

#Globals
#-----------------------------------------------------------

location = 1
prevLocation = 0

backpack = ["laptop", "notebook", "myUcard"]

place_list = []
#COMMON INPUTS
north = ["north", "n", "go north", "head north"]
south = ["south", "s", "go south", "head south"]
east = ["east", "e", "go east", "head east"]
west = ["west", "w", "go west", "head west"]

exitDoor = ["open door", "exit", "exit room"]
jumpOutWindow = ["jump out", "jump out window", "exit window"]
backpackNames = ["i", "b", "backpack", "inventory", "back pack", "open backpack", "look in backpack"]
lookOutWindow = ["look out window", "open window"]

#-----------------------------------------------------------

print("---------------------------------------------------------")
print("Welcome to Bulldog Brawl")

first = ""
second = ""

while True:
    if location == 0:
        break
    #DORM = 1
    while location == 1:
        if first in backpackNames:
            displayBackpack()
            first = ""
        elif first in jumpOutWindow:
            print("---------------------------------------------------------")
            gprint("You fall to your death. What were you thinking?")
            location = 0
        elif first in lookOutWindow:
            print("---------------------------------------------------------")
            gprint("You see the campus and feel the breeze off Lake Superior.")
            first = uinput("")
        elif first in exitDoor:
            print("---------------------------------------------------------")
            changeLocation(2)
        elif first != "":
            print("---------------------------------------------------------")
            gprint("I don't know " + first)
            first = ""
        elif location == 1:
            print("---------------------------------------------------------")
            if 1 not in place_list:
                gprint("You are standing in your dorm. Your roommate, Brad, is watching TV on his bed. You desperately need help on your \nProgramming Project. In your room there is a door, a window, and your desk.")
                first = uinput("What do you do? ")
                place_list.append(1)
            else:
                gprint("DORM\nBrad is still watching TV. There is a window, a door, and a desk.")
                first = uinput("")

    #DORM HALLWAY = 2
    while location == 2:
        if second in backpackNames:
            displayBackpack()
            second = ""
        elif second in north:
            print("---------------------------------------------------------")
            changeLocation(3)
        elif second ==("***"):
            print("---------------------------------------------------------")
            gprint("***")
            second = uinput("")
        elif second ==("***"):
            print("---------------------------------------------------------")
            gprint("***")
            second = uinput("")
        elif second ==("***"):
            print("---------------------------------------------------------")
            gprint("***")
            second = uinput("")
        elif second != "":
            print("---------------------------------------------------------")
            gprint("I don't know " + second)
            second = ""
        elif location == 2:
            if 1 not in place_list:
                gprint("You've made your way to the main dorm hallway. If you look north, you see a sign for the LSH office. Your dorm is West to your back. To the south is a couple parking lots for students. You didn't bother bringing your car up this semester, but are sure you won't need it. ")
                second = uinput("")
                place_list.append(1)
            else:
                gprint("DORM HALLWAY\nYou can see LSH, your dorm, and the parking lots")
                first = uinput("")
    while location == 3:
        print("LSH")
    #LSH Office - 3
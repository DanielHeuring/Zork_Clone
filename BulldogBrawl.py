import time
from time import sleep

def gprint(string):
    string = string + "\n"
    for i in string:
        print(i, end='', flush=True)
        sleep(0.001) # 0.02 for game

def gprintcustom(string, speed):
    string = string + "\n"
    for i in string:
        print(i, end='', flush=True)
        sleep(speed)

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

# Globals
location = 1
prevLocation = 0
isTerminated = False

backpack = ["laptop", "notebook", "myUcard"]
place_list = []

# Common Inputs
north = ["north", "n", "go north", "head north"]
south = ["south", "s", "go south", "head south"]
east = ["east", "e", "go east", "head east"]
west = ["west", "w", "go west", "head west"]

exitDoor = ["open door", "exit", "exit room"]
jumpOutWindow = ["jump out", "jump out window", "exit window"]
backpackNames = ["i", "b", "backpack", "inventory", "back pack", "open backpack", "look in backpack"]

discoveredLocations = []

# Locations
locations = {
    1: {
        "initialDescription": "You are standing in your dorm. Your roommate, Brad, is watching TV on his bed. In your room there is a door, a window, and your desk.",
        "description": "DORM\nBrad is still watching TV. There is a window, a door, and a desk.",
        "exits": {"door": 2, "exit": 2, "open door": 2, "exit door": 2, "east": 2, "e": 2, "go east": 2},
        "actions": {
            "open window": "You see the campus and feel the breeze off Lake Superior.",
            "jump out window": "You fall to your death. What were you thinking?"
        }
    },
    2: {
        "initialDescription": "You've made your way to the main dorm hallway. If you look north, you see a sign for the LSH office. Your dorm is West to your back. To the south is a couple parking lots for students. You didn't bother bringing your car up this semester, but are sure you won't need it.",
        "description": "DORM HALLWAY\nYou can see LSH, your dorm, and the parking lots.",
        "exits": {"north": 3, "west": 1, "south": 4},
        "actions": {}
    },
    3: {
        "initialDescription": "***",
        "description": "You are in front of the LSH office. The door is slightly open.",
        "exits": {"south": 2},
        "actions": {"open door": "The door is locked."}
    },
    4: {
        "initialDescription": "***",
        "description": "",
        "exits": {"north": 2},
        "actions": {"***"}
    }
}

# Function to handle location transitions and actions
def handle_location(location):
    print("---------------------------------------------------------")
    if location in discoveredLocations:
        gprint(locations[location]["description"])
        user_input = uinput(">")
    else:
        gprint(locations[location]["initialDescription"])
        user_input = uinput(">")
        discoveredLocations.append(location)

    # Handle exits (moving to another location)
    if user_input in locations[location]["exits"]:
        new_location = locations[location]["exits"][user_input]
        changeLocation(new_location)
    # Handle actions within the current location
    elif user_input in locations[location]["actions"]:
        gprint(locations[location]["actions"][user_input])
    # Ends the program at any point
    elif user_input == "terminate":
        global isTerminated
        isTerminated = True
    else:
        gprint("I don't know how to " + user_input)

# Main Game Loop
while True:
    if location == 0:
        break
    elif isTerminated == True:
        gprintcustom("TERMINATING...\n\n\n", 0.1)
        break
    handle_location(location)

    

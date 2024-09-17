import time
from time import sleep


def gprint(string):
    string = string + "\n"
    for i in string:
        print(i, end='', flush=True)
        sleep(0.02) # 0.02 for game

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
    location = newLocation

def displayBackpack():
    gprint("\nBackpack:\n-------------")
    print(*backpack, sep= "\n")
    print("\n")

def get_exit(user_input):
    for action, aliases in exit_aliases.items():
        if user_input in aliases:
            return action
    return None

def get_action(user_input):
    for action, aliases in action_aliases.items():
        if user_input in aliases:
            return action
    return None

# Globals
location = "dorm"
prevLocation = 0
isTerminated = False

backpack = ["laptop", "notebook", "myUcard"]
place_list = []

# Exit Lists
north = ["north", "n", "go north", "head north"]
south = ["south", "s", "go south", "head south"]
east = ["east", "e", "go east", "head east"]
west = ["west", "w", "go west", "head west"]
exitDoor = ["open door", "exit", "exit room"]

exit_aliases = {"north": north,
                "south": south,
                "east": east,
                "west": west,
                "door": exitDoor}

# Action Lists
backpackNames = ["i", "b", "backpack", "inventory", "back pack", "open backpack", "look in backpack"]
jumpOutWindow = ["jump out", "jump out window", "exit window"]

action_aliases = {"jump out window": jumpOutWindow,
                 "backpack": backpackNames}

discoveredLocations = []

# Locations
locations = {
    "dorm": {
        "initialDescription": "You are standing in your dorm. Your roommate, Brad, is watching TV on his bed. In your room there is a door, a window, and your desk.",
        "description": "DORM\nBrad is still watching TV. There is a window, a door, and a desk.",
        "exits": {"door": "dormhall"},
        "actions": {
            "open window": "You see the campus and feel the breeze off Lake Superior.",
            "jump out window": "You fall to your death. What were you thinking?",
            "backpack": "**BACKPACK COMPONENTS**"
        }
    },
    "dormhall": {
        "initialDescription": "***",
        "description": "You've made your way to the main dorm hallway. You see a sign for the LSH office to the north.",
        "exits": {"north": "LSHdesk", "west": "dorm"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "LSHdesk": {
        "initialDescription": "***",
        "description": "You are in front of the LSH office",
        "exits": {"south": "dormhall"},
        "actions": {"open door": "The door is locked.",
                   "backpack": "**BACKPACK COMPONENTS**"}
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
    exit = get_exit(user_input)
    action = get_action(user_input)
    if exit in locations[location]["exits"]:
        new_location = locations[location]["exits"][exit]
        changeLocation(new_location)
    # Handle actions within the current location
    elif action in locations[location]["actions"]:
        gprint(locations[location]["actions"][action])
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

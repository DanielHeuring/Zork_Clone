from time import sleep
from typing import List
from rooms import locations

class Hall:
    def __init__(self, data):
        self.init_des = data.get("initialDescription", "")
        self.desc = data.get("description", "")
        self.exits = data.get("exits", {})
        self.actions = data.get("actions", {})
        self.visited = False

    def visit_hall(self):
        if not self.visited:
            self.visited = True
            print(location)
            gprint(self.desc)
        else:
            print(location)
            gprint(self.desc)

    def inspect_hall(self):
       gprint(f"You inspect {self.name}. You see: {','.join(self.items) if self.items  else 'nothing special'}")

# Initialize Halls with location Dict
halls = {key: Hall(data) for key, data in locations.items()}

# Exits
north = ["north", "n", "go north", "head north"]
south = ["south", "s", "go south", "head south"]
east = ["east", "e", "go east", "head east"]
west = ["west", "w", "go west", "head west"]
exitDoor = ["open door", "exit", "exit room"]
exitWindow = ["window", "jump out"]
up_stairs = ["u", "go up", "up stairs", "go up stairs", "up"]
down_stairs = ["d", "go down", "down stairs", "go down stairs", "down"]

exit_aliases = {"north": north,
                "south": south,
                "east": east,
                "west": west,
                "door": exitDoor,
                "window": exitWindow,
                "up": up_stairs,
                "down": down_stairs}

# Action Lists
backpackNames = ["i", "b", "backpack", "inventory", "back pack", "open backpack", "look in backpack"]
jumpOutWindow = ["jump out", "jump out window", "exit window", "jump"]
openWindow = ["open", "open window", "window"]

action_aliases = {"jump out window": jumpOutWindow,
                 "backpack": backpackNames,
                 "open window": openWindow
                 }

# Globals
location = "dorm"
prevLocation = 0
backpack = []

#Functions
def gprint(string):
    string = string + "\n"
    for i in string:
        print(i, end='', flush=True)
        sleep(0.0001) # 0.02 for game

def uinput(string):
    print("\n")
    output = (input(string)).lower().strip()
    return str(output)

def changeLocation(new_location):
    global prevLocation, location
    prevLocation = location
    location = new_location

def get_exit(user_input):
    for exit, aliases in exit_aliases.items():
        if user_input in aliases:
            return exit
    return None

def get_action(user_input):
    for action, aliases in action_aliases.items():
        if user_input in aliases:
            return action
    return None

def invalid_input(user_input, exit_take, action_take):
    if exit_take in exit_aliases:
        gprint("That is not a valid direction here")
    elif action_take in action_aliases:
        gprint("That is not a valid action here")
    else:
        gprint("I don't know how to " + user_input)

# Main Game Handler
def handle_location(location_name):
    print("--------------------")

    current_hall = halls[location_name]
    current_hall.visit_hall()

    user_input = uinput("> ")
    exit_take = get_exit(user_input)
    action_take = get_action(user_input)

    if exit_take in current_hall.exits:
        new_location = current_hall.exits[exit_take]
        changeLocation(new_location)   

    elif action_take in current_hall.actions:
        pass
            
    else:
        invalid_input(user_input, exit_take, action_take)

# Main Game Loop
while True:
    handle_location(location)
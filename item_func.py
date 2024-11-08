from time import sleep
from typing import List

class Hall:
    def __init__(
        self,
        name: str = None,
        init_des: str = None,
        desc: str = None,
        exits: List[str] = None,
        actions: str = None,
        visited: bool = False,
        items: bool = False
        ):
        self.name = name
        self.init_des = init_des
        self.desc = desc
        self.exits = exits
        self.visited = visited
        self.items = items
        self.inspected = False
        self.actions = actions if actions else []

       
    def visit_hall(self):
        if not self.visited:
            self.visited = True
            gprint(self.init_des)
            # TODO - display the init_des
        else:
            gprint(self.desc)

    def inspect_hall(self):
       gprint(f"You inspect {self.name}. You see: {','.join(self.items) if self.items  else 'nothing special'}")

# Array containing locations
location = 0        
halls = [
    # Dorm Room
    Hall(
        name = "Dorm Room",
        init_des= "You are standing in your room.",
        desc = "Brad is still watching TV",
        exits = {
            "door": "Dorm Hall",
            "window" : ""
        },
        actions= {
            "Open the window": "",
            "items": ""
        },
        items= True
    ),
    Hall(
        name = "Dorm Hall",
        init_des= "Standing outside of your room you see the LSH desk to the north",
        desc = "You are in the dorm hall",
        exits= {
            "east": "Dorm Room",
            "north": "LSH Desk"
        },
        items= True
    ),
    Hall(
        name= "LSH Desk",
        init_des= "You are standing outside the LSH desk but nobody is there",
        desc = "There's a light on at the desk but nobody is there",
        exits= {
            "south": "Dorm Hall",
            "east": "Dining Center"
        },
        items= True
    ),
    Hall(
        name= "Dining Center",
        init_des= "Standing in front of the glass doors you find a smell assulting your nose",
        desc = "The assulting smell is still there.",
        exits= {
            "west": "LSH Desk"
        }
    )
]
# Exits
north = ["north", "n", "go north", "head north"]
south = ["south", "s", "go south", "head south"]
east = ["east", "e", "go east", "head east"]
west = ["west", "w", "go west", "head west"]
exitDoor = ["open door", "exit", "exit room"]
exitWindow = ["window", "jump out"]

exit_aliases = {"north": north,
                "south": south,
                "east": east,
                "west": west,
                "door": exitDoor,
                "window": exitWindow}

# Action Lists
backpackNames = ["i", "b", "backpack", "inventory", "back pack", "open backpack", "look in backpack"]
jumpOutWindow = ["jump out", "jump out window", "exit window", "jump"]
openWindow = ["open", "open window", "window"]

action_aliases = {"jump out window": jumpOutWindow,
                 "backpack": backpackNames,
                 "open window": openWindow
                 }


# Globals
prevLocation = 0
backpack = []

# Funtions
def gprint(string):
    string = string + "\n"
    for i in string:
        print(i, end='', flush=True)
        sleep(0.02) # 0.02 for game

def uinput(string):
    print("\n")
    output = (input(string)).lower().strip()
    return str(output)

def changeLocation(newLocation):
    global prevLocation, location
    prevLocation = location
    location = newLocation

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

# Function finding what hall we want in array
def find_hall(new_hall_name):
    for hall_index in range(len(halls)):
        if halls[hall_index].name == new_hall_name:
            return hall_index
    pass

# Items
def key():
    return "a key on your desk"
def key_card():
    return "a key card laying on the floor"
def ball():
    return "There is ball laying on the ground outside of the desk"
item_dic = {
    "Dorm Room": key,
    "Dorm Hall": key_card,
    "LSH Desk": ball
}

# Main Game Handling
def handle_location(location):
    print("-------------------------")

    halls[location].visit_hall()
    
    user_input = uinput("> ")
    exit_take = get_exit(user_input)
    action_take = get_action(user_input)

    if "inspect" in user_input:
        if halls[location].items:
            hall_index = halls[location].name
            item = item_dic[hall_index]
            if callable(item):
                item_desc = item()
                gprint(f"There is {item_desc}")
        halls[location].inspected = True
    
    elif "grab" in user_input or "pick up" in user_input:
        if halls[location].items and halls[location].inspected:
            hall_index = halls[location].name
            item = item_dic[hall_index]
            if callable(item):
                item_desc = item()
                backpack.append(item)
                gprint(f"You picked up the {item_desc}")
                halls[location].items = False
        elif halls[location].inspected == False:
            gprint("You have not inspected the room")
        else:
            gprint("There is nothing to pick up here")

    elif exit_take in (halls[location].exits):
        new_location_name = halls[location].exits[exit_take]
        new_location = find_hall(new_location_name)
        changeLocation(new_location)   

    elif action_take in (halls[location].actions):
        pass

    elif "backpack" in user_input:
        print(backpack)
            
    else:
        gprint("I don't know how to " + user_input)

# Main Game Loop
while True:
    handle_location(location)
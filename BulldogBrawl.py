import operator
import turtle
from time import sleep
from typing import List

class Hall:
    def __init__(
        self,
        name: str = None,
        init_des: str = None,
        exits: List[str] = None,
        actions: str = None,
        elements: str = None,
        visited: bool = False,
        #shape: turtle
    ):
        self.name = name
        self.init_des = init_des
        self.exits = exits
        self.visited = visited
        if actions is None:
            self.actions = []
        else:
            self.actions = actions
        if elements is None:
            self.elements = []
        else:
            self.elements = []

       # self.shape = shape

    #def draw(self):
        #however you should draw it in turtle

    def visit_hall(self):
        if not self.visited:
            self.visited = True
            gprint(self.init_des)
            # TODO - display the init_des
            

        # TODO - ?? is there anything else to display here

    def inspect_hall(self):
        # TODO - display specific info you want when inspecting the hall
        pass

location = 0        

halls = [
    # Dorm Room
    Hall(
        name = "Dorm Room",
        init_des= "You are standing in your room.",
        exits = {
            "door": "Dorm Hall",
            "Window" : "You fall to your death"
        },
        actions= [
            "Open the window",
            "Grab set of Keys"
        ]
    ),
    Hall(
        name = "Dorm Hall",
        init_des= "Standing outside of your room you see the LSH desk to the north",
        exits= [
            "Dorm Room",
            "LSH Desk"
        ]
    ),
    Hall(
        name= "LSH Desk",
        init_des= "You are standing outside the LSH desk but nobody is there",
        exits= [
            "Dorm Hall"
        ]
    )
]
# Exits
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

# Globals
prevLocation = 0

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
    for action, aliases in exit_aliases.items():
        if user_input in aliases:
            return action
    return None

# Function finding what hall we want in array
def find_hall(new_hall_name):
    for hall_index in range(len(halls)):
        if halls[hall_index].name == new_hall_name:
            return hall_index
    pass


# Location Handling
def handle_location(location):
    print("-------------------------")
    halls[location].visit_hall()
    user_input = uinput(">")
    exit_take = get_exit(user_input)
    if exit_take in (halls[location].exits):
        # this gets us the name of the room to go to
        new_location_name = halls[location].exits[exit_take]
        # convert that room name into an index in the halls array
        new_location = find_hall(new_location_name)
        changeLocation(new_location)   


# Main Game Loop
while True:
    handle_location(location)
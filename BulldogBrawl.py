import sys
from rooms import locations
from GameState import GameState

# Game state Class
state = GameState()

# Hall Class
class Hall:
    def __init__(self, data):
        self.init_des = data.get("initialDescription", "")
        self.desc = data.get("description", "")
        self.exits = data.get("exits", {})
        self.actions = data.get("actions", {})
        self.items = data.get("items", {})
        self.special_desc = data.get("specialDesc", {})
        self.visited = False
        self.inspected = False

    def visit_hall(self):
        if not self.visited:
            self.visited = True
            print(state.location.capitalize())
            if state.location == "heller3":
                for desc in self.desc.values():
                    state.gprint(desc)
            else:
                state.gprint(self.desc)
        else:
            print(state.location.capitalize())
            if state.location == "heller3":
                for desc in self.desc.values():
                    state.gprint(desc)
            else:
                state.gprint(self.desc)

    def inspect_hall(self):
        print("--------------------")
        self.inspected = True
        for item in self.items.values():
            state.gprint(item.get("description"))
        
        if self.special_desc:
            for desc in self.special_desc.values():
                state.gprint(desc)
                
            #state.gprint(self.special_desc)

        elif len(self.items) == 0:
            state.gprint("Nothing catches your eye") 

# Initialize Halls with location Dict
halls = {key: Hall(data) for key, data in locations.items()}

# Exits
north = ["north", "n", "go n", "go north", "head north"]
south = ["south", "s", "go s", "go south", "head south"]
east = ["east", "e", "go e", "go east", "head east"]
west = ["west", "w", "go w", "go west", "head west"]
exitDoor = ["open door", "exit", "exit room"]
enter = ["enter", "enter hall", "enter room", "go inside"]
up_stairs = ["u", "go up", "go u", "up stairs", "go up stairs", "up"]
down_stairs = ["d", "go down", "go d", "down stairs", "go down stairs", "down"]
backup = ["back", "leave", "go back"]
forward = ["foward", "f", "go foward"]

exit_aliases = {"north": north,
                "south": south,
                "east": east,
                "west": west,
                "exit": exitDoor,
                "enter": enter,
                "up": up_stairs,
                "down": down_stairs,
                "back": backup,
                "forward":forward
                }

# Action Lists
jumpOutWindow = ["jump out", "jump out window", "exit window", "jump"]
openWindow = ["open", "open window", "window"]
unlockDoor = ["unlock door", "unlock", "open door"]
chemKey = ["use chemistry key", "unlock lab"]
meltChains = ["use acid", "melt chain", "use beaker of acid"]
chickenDog = ["toss chicken wing", "use chicken wing", "distract dog"]
talkTo = ["talk", "talk to them", "speak", "speak with"]
fight = ["fight", "attack", "take exam"]

action_aliases = {"jump_out_window": jumpOutWindow,
                 "open window": openWindow,
                 "unlock": unlockDoor,
                 "acid": meltChains,
                 "chicken": chickenDog,
                 "talk": talkTo,
                 "fight": fight,
                 "use_ckey": chemKey
                 }

# Instruction Variable
instructions = """
---------Instructions---------
- Navigate the halls using commands like 'go north', 'go south', 'up', or 'down'.
- Inspect rooms to find items and uncover hidden details.
- Use 'grab <item>' to pick up an item after inspecting.
- Actions in rooms can be 'talk', 'unlock', or 'use <item name>', with more that can be discovered
- Manage your items using 'backpack' to check what you've collected.
- Your goal is to explore, find items, and steal the final answer keys.!
        """

help = """
---------Helpful Commands---------
- Make sure to inspect halls with <inspect>!!!
- Directional Commands: north, south, west, east, up, down
- Special Commands: exit, enter, back, backpack
- Actions: unlock door, use <item name>, talk
"""

# Functions
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

# Invalid user response for exits and actions
def invalid_input(user_input, exit_take, action_take):
    print("--------------------")
    if exit_take in exit_aliases:
        state.gprint("That is not a valid direction here")
    elif action_take in action_aliases:
        state.gprint("That is not a valid action here")
    else:
        state.gprint("I don't know how to " + user_input)

# Function for backpack
def display_backpack():
    print("---- Backpack ----")
    for item in state.backpack:
        print(item["name"])

# Main Game Handler
def handle_location(location_name):
    print("--------------------")

    current_hall = halls[location_name]

    if location_name =="game_over":
        sys.exit()

    current_hall.visit_hall()

    user_input = state.uinput("> ")
    exit_take = get_exit(user_input)    
    action_take = get_action(user_input)

    if user_input == "inspect":
        current_hall.inspect_hall()

    elif user_input == "help":
        state.gprint(f"{help}")
        
    elif "grab" in user_input and current_hall.inspected:
        user_item = user_input.split("grab ")[-1]
        for item in current_hall.items.values():
            if user_item == item.get("name"):
                state.backpack.append(item)
                del current_hall.items[user_item]
                print("--------------------")
                state.gprint(f"You got the {user_item}!!")
                break
            else:
                state.gprint(f"{user_item} is not a valid item")

    elif "backpack" in user_input:
        display_backpack()

    elif "instruction" in user_input:
        state.gprint(f"{instructions}")

    elif exit_take in current_hall.exits:
        new_location = current_hall.exits[exit_take]
        state.changeLocation(new_location)   

    elif action_take in current_hall.actions:
        result = current_hall.actions.get(action_take)
        if isinstance(result, str):
            print(result)
        else:
            result(state)
            
    else:
        invalid_input(user_input, exit_take, action_take)

# Main Game Loop
def game_loop(state):
    print("--------------------")
    state.gprint("Remmber your goal is to break into Proffesor Buck's office and steal the final exam.")
    while True:
        handle_location(state.location)

#Start Menu
def menu(state):
    state.gprint("""
---------WELCOME TO BULLDOG BRAWl---------
    1. Play game
    2. Instructions
    3. Exit""")
    choice = state.uinput("> ")
    if choice =='1':
        game_loop(state)
    elif choice =='2':
        state.gprint(f"{instructions}")
        menu(state)
    elif choice =='3':
        sys.exit()
    else:
        state.gprint("Invalid input")

menu(state)
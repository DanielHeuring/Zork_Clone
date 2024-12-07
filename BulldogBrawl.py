import sys
import time
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
        exits = ", ".join(f"{key}: {value}" for key, value in self.exits.items())
        state.gprint(exits)

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
keyPad = ["use keypad", "keypad", "enter code"]
useInvite = ["give invite", "use invite", "throw invite"]
useUcard = ["use ucard", "get food", "buy food"]
giveSalad = ["use ceaser salad", "give ceaser salad", "give salad", "use salad"]

action_aliases = {"jump_out_window": jumpOutWindow,
                 "open window": openWindow,
                 "unlock": unlockDoor,
                 "acid": meltChains,
                 "chicken": chickenDog,
                 "talk": talkTo,
                 "use_ckey": chemKey,
                 "keypad": keyPad,
                 "invite": useInvite,
                 "useUcard": useUcard,
                 "salad": giveSalad
                 }

# Instrtion Variable
instructions = """
---------Instructions---------
- Navigate the halls using commands like 'go north', 'go south', 'up', or 'down'.
- Inspect rooms to find items and uncover hidden details.
- Use 'grab <item>' to pick up an item after inspecting.
- Actions in rooms can be 'talk', 'unlock', or 'use <item name>', with more that can be discovered
- Manage your items using 'backpack' to check what you've collected.
- Type help into the prompt at anytime to get useful commands!
- In order to leave the game just type leave game.
- Your goal is to explore, find items, and steal the final answer keys.!
        """

help = """
                ----------HELP---------
- inspect    >  inspects current room or hall
- n/s/e/w    >  moves around to different rooms and halls
- u/d        >  moves up or down stairs when available
- grab       >  adds item or object to your backpack
- use        >  uses item stored in backpack
- backpack   >  view the contents of your backpack
- talk       >  interacts with people in rooms
- leave game >  exits the game

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
    print("--------------------")
    print("---- Backpack ----")
    for item in state.backpack:
        print(item["name"])

# Main Game Handler
def handle_location(location_name):
    print("--------------------")

    current_hall = halls[location_name]

    if location_name =="game_over":
        time.sleep(5)
        sys.exit()

    current_hall.visit_hall()

    user_input = state.uinput("> ")
    exit_take = get_exit(user_input)    
    action_take = get_action(user_input)

    if user_input == "inspect":
        current_hall.inspect_hall()

    elif user_input == "leave game":
        sys.exit()

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
        else:
            state.gprint(f"I don't know how to grab {user_item}")

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
    state.gprint("Remember your goal is to break into Proffesor Buck's office and steal the final exam.")
    while True:
        handle_location(state.location)

#Start Menu
def menu(state):
    print("""
▀█████████▄  ███    █▄   ▄█        ▄█       ████████▄   ▄██████▄     ▄██████▄  
  ███    ███ ███    ███ ███       ███       ███   ▀███ ███    ███   ███    ███ 
  ███    ███ ███    ███ ███       ███       ███    ███ ███    ███   ███    █▀  
 ▄███▄▄▄██▀  ███    ███ ███       ███       ███    ███ ███    ███  ▄███        
▀▀███▀▀▀██▄  ███    ███ ███       ███       ███    ███ ███    ███ ▀▀███ ████▄  
  ███    ██▄ ███    ███ ███       ███       ███    ███ ███    ███   ███    ███ 
  ███    ███ ███    ███ ███▌    ▄ ███▌    ▄ ███   ▄███ ███    ███   ███    ███ 
▄█████████▀  ████████▀  █████▄▄██ █████▄▄██ ████████▀   ▀██████▀    ████████▀  
                        ▀         ▀                                            
        ▀█████████▄     ▄████████    ▄████████  ▄█     █▄   ▄█                         
          ███    ███   ███    ███   ███    ███ ███     ███ ███                         
          ███    ███   ███    ███   ███    ███ ███     ███ ███                         
         ▄███▄▄▄██▀   ▄███▄▄▄▄██▀   ███    ███ ███     ███ ███                         
        ▀▀███▀▀▀██▄  ▀▀███▀▀▀▀▀   ▀███████████ ███     ███ ███                         
          ███    ██▄ ▀███████████   ███    ███ ███     ███ ███                         
          ███    ███   ███    ███   ███    ███ ███ ▄█▄ ███ ███▌    ▄                   
        ▄█████████▀    ███    ███   ███    █▀   ▀███▀███▀  █████▄▄██                   
                       ███    ███                          ▀                           
""")
    
    state.gprint("""\033[1m
    1. Play Game
    2. Instructions
    3. Exit\033[0;0m""")
    choice = state.uinput("> ")
    if choice =='1':
        game_loop(state)
    elif choice =='2':
        state.gprint(f"{instructions}")
        menu(state)
    elif choice == "help":
        state.gprint(f"{help}")
        menu(state)
    elif choice =='3':
        sys.exit()
    else:
        state.gprint("Invalid input")

menu(state)

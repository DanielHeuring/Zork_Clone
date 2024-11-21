from time import sleep
from typing import List
from rooms import locations

# Globals
location = "dorm"
prevLocation = 0
backpack = []
drbuck_string ="Dr. Buck says, 'You think you can run from me!! What a pitiful action. What's that in your hand? Test answers. You are going to have to see the dean for this.' He drags you by your ear through the student filled halls staright into the dean's office. The dean quickly informs you that your time at UMD is over."
class Hall:
    def __init__(self, data):
        self.init_des = data.get("initialDescription", "")
        self.desc = data.get("description", "")
        self.exits = data.get("exits", {})
        self.actions = data.get("actions", {})
        self.items = data.get("items", {})
        self.visited = False
        self.inspected = False

    def visit_hall(self):
        if not self.visited:
            self.visited = True
            print(location)
            gprint(self.desc)
        else:
            print(location)
            gprint(self.desc)

    def inspect_hall(self):
        self.inspected = True
        for item in self.items.values():
            gprint(item.get("description"))
        if len(self.items) == 0:
            gprint("Nothing catches your eye") 

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
run =['run', 'run away', 'escape']
action_aliases = {"jump out window": jumpOutWindow,
                 "backpack": backpackNames,
                 "open window": openWindow
                 }

#Functions
def blackJack():
    global buck_Health, player_Health, action
    #Description of the "troll" 
    gprint("""
You here rattles coming from the dark corner of his office. All of the sudden
a dark figure imerges. You scream out in terror. "AHhhhhh" You realize it was 
Dr. Buck and are a little embaressed that you screamed. He questions you on
what you are doing in his office until he notices the answer key in your hand.
You attempt to run but the door slams shut and you cannot pry in open. You turn
around and Dr. Buck has a deck of cards on his deck and asks if you want to play.
He wants to play a version of blackjack where the difference in value deals damage
to your health. 
    """)
    #Intial Health Values. Can be adjusted to change difficulty and length of fight. 
    buck_Health = 50 
    player_Health = 65
    while buck_Health>0 and player_Health>0:

        gprint(f"Your health is {player_Health} and Dr. Buck's health is {buck_Health}")
        #Resets variables for new round
        aces = 0
        aces_comp = 0
        action = ""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
                    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

        deck = [(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(deck)
        #Pre-action cards
        card1 = deck.pop()
        card2 = deck.pop()
        card3 = deck.pop()
        hidden_card4 = deck.pop()
        hand_val_player = card_values[card1[0]] + card_values[card3[0]]
        hand_val_computer = card_values[card2[0]]
        if card1[0]=='Ace':
            aces+=1
        if card2[0]=='Ace':
            aces_comp +=1
        if card3[0]=='Ace':
            aces+=1
        if hidden_card4[0]=='Ace':
            aces_comp+=1
        #Fixes edge case
        if aces == 2:
            hand_val_player -=10
            aces -=1
        #Informs player of cards
        gprint(f"Your first two cards are {card1[0]} of {card1[1]} and {card3[0]} of {card3[1]} for a total of {hand_val_player}.")
        gprint(f"Dr. Buck's first card is the {card2[0]} of {card2[1]}.")

        while True:
            if hand_val_player<=21: #Loops rounds while both players are alive
                    action = input("Do you want to hit or stand? ").strip().lower()
                    if action =="hit":
                        drawcard = deck.pop()
                        hand_val_player += card_values[drawcard[0]]
                        if drawcard[0] == 'Ace':
                            aces+=1
                        if hand_val_player>21 and aces>0:
                            aces-=1
                            hand_val_player-=10
                        gprint(f"You drew the {drawcard[0]} of {drawcard[1]} and your new hand value is {hand_val_player}.")
                    elif action == "stand":
                        gprint(f"You stand with {hand_val_player}.")
                        break
                    else:
                        gprint(f"Dr. Buck does not understand {action} and requests that you say hit or stand.")
                        
            else:
                gprint("You have busted. Your hand is now worth 0")
                hand_val_player = 0
                break
        hand_val_computer += card_values[hidden_card4[0]]
        gprint(f"Dr. Buck flips over his hidden card and it is the {hidden_card4[0]} of {hidden_card4[1]} and their new total is {hand_val_computer}.")
        while hand_val_computer <= 21:
            if hand_val_computer <= 17:
                drawcard = deck.pop()
                hand_val_computer += card_values[drawcard[0]]          
                if drawcard[0] == 'Ace':
                    aces_comp += 1
                if hand_val_computer > 21 and aces_comp > 0:
                    aces_comp -= 1
                    hand_val_computer -= 10
                gprint(f"Dr. Buck draws the {drawcard[0]} of {drawcard[1]}. Their new total is {hand_val_computer}.")
            else:
                gprint(f"Dr. Buck stands with {hand_val_computer}.")
                break
        if hand_val_computer > 21:
            buck_Health= buck_Health - hand_val_player
            gprint(f"Dr. Buck busted. You deal {hand_val_player} to him.\n")
        elif hand_val_player > hand_val_computer:
            damage_Buck = hand_val_player-hand_val_computer
            buck_Health = buck_Health - damage_Buck
            gprint(f"You deal {damage_Buck} to Dr. Buck.\n")
        elif hand_val_computer > hand_val_player:
            damage_player = hand_val_computer - hand_val_player
            player_Health = player_Health - damage_player
            gprint(f"Dr. Buck deals {damage_player} to you.\n")
        else: 
            gprint("Your hand values were the same neither person deals any damage.\n")
        sleep(1) #Delays between rounds and allows user to catch up
    if buck_Health<=0:
        gprint("""
You have defeated Dr. Buck in a game of blackjack. He 
looks at you with dread and allows you to leave the room
answer key in hand. You succesfully pass the final exam 
and are able to move on with your college journey.
              """)
    elif player_Health<=0:
        gprint("""
Dr. Buck defeats you in his card game and rips the answer key
out of your hand. He stands up and tightly grabs your arm as he
escorts you down the hall. You pass numerous students who point
and laugh at you before arriving at the office of student conduct.
You are told your time at UMD has come to an end. You have been expelled.
              """)

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

# Invalid user response for exits and actions
def invalid_input(user_input, exit_take, action_take):
    if exit_take in exit_aliases:
        gprint("That is not a valid direction here")
    elif action_take in action_aliases:
        gprint("That is not a valid action here")
    else:
        gprint("I don't know how to " + user_input)

# Function for backpack
def display_backpack():
    print("---- Backpack ----")
    for item in backpack:
        print(item["name"])

# Main Game Handler
def handle_location(location_name):
    print("--------------------")

    current_hall = halls[location_name]
    current_hall.visit_hall()

    user_input = uinput("> ")
    exit_take = get_exit(user_input)    
    action_take = get_action(user_input)

    if user_input =='fight' and location_name =='thomasbuckoffice':
        blackJack()
        sys.exit()
    elif user_input in run and location_name == 'thomasbuckoffice':
        print(drbuck_string)
        sys.exit()

    elif user_input == "inspect":
        current_hall.inspect_hall()
        
    elif "grab" in user_input and current_hall.inspected:
        user_item = user_input.split("grab ")[-1]
        for item in current_hall.items.values():
            if user_item == item.get("name"):
                backpack.append(item)
                del current_hall.items[user_item]
                gprint("You got the item!!")
                break
            else:
                gprint("That is not a valid item")

    elif "backpack" in user_input:
        display_backpack()

    elif exit_take in current_hall.exits:
        new_location = current_hall.exits[exit_take]
        changeLocation(new_location)   

    elif action_take in current_hall.actions:
        pass
            
    else:
        invalid_input(user_input, exit_take, action_take)

# Main Game Loop
while True:
    handle_location(location)

from time import sleep
import random
import sys
global locations
#File 1
#Game State Class
class GameState:
    def __init__(self):
        self.location = "dorm"
        self.prevLocation = 0
        self.backpack = []

    def gprint(self, string):
        string = string + "\n"
        for i in string:
            print(i, end='', flush=True)
            sleep(0.0001) # 0.02 for game

    def uinput(self, string):
        print("\n")
        output = (input(string)).lower().strip()
        return str(output)
    
    def changeLocation(self, new_location):
        global prevLocation, state
        prevLocation = self.location
        self.location = new_location

state = GameState()
#File 4
#Final battle of the game
def blackJack(state):
    state.gprint("""
He questions you on what you are doing in his office until he notices the answer key in your hand.
You attempt to run but the door slams shut and you cannot pry in open. You turn
around and Dr. Buck has a deck of cards on his deck and asks if you want to play.
He challanges you to a game of blackjack.
---hint---
This game of blackjack is a version where each hand determines who and how much damage is dealt. Your goal is to reduce Dr. Buck's health from 50 to zero before he does the same to your 65 health. Winning a hand deals damage to Dr. Buck based on the difference in card values, while losing means you take the damage. Strategically decide when to hit or stand, and avoid busting to ensure your survival!
----------
    """)
    #Intial Health Values
    buck_Health = 50
    player_Health = 65
    while buck_Health>0 and player_Health>0:
        state.gprint(f"Your health is {player_Health} and Dr. Buck's health is {buck_Health}")
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
        state.gprint(f"Your first two cards are {card1[0]} of {card1[1]} and {card3[0]} of {card3[1]} for a total of {hand_val_player}.")
        state.gprint(f"Dr. Buck's first card is the {card2[0]} of {card2[1]}.")

        while True:
            if hand_val_player<=21:
                    action = input("Do you want to hit or stand? ").strip().lower()
                    if action =="hit":
                        drawcard = deck.pop()
                        hand_val_player += card_values[drawcard[0]]
                        if drawcard[0] == 'Ace':
                            aces+=1
                        if hand_val_player>21 and aces>0:
                            aces-=1
                            hand_val_player-=10
                        state.gprint(f"You drew the {drawcard[0]} of {drawcard[1]} and your new hand value is {hand_val_player}.")
                    elif action == "stand":
                        state.gprint(f"You stand with {hand_val_player}.")
                        break
                    else:
                        print(f"Dr. Buck does not understand {action} and requests that you say hit or stand.")
                        
            else:
                state.gprint("You have busted. Your hand is now worth 0")
                hand_val_player = 0
                break
        hand_val_computer += card_values[hidden_card4[0]]
        state.gprint(f"Dr. Buck flips over his hidden card and it is the {hidden_card4[0]} of {hidden_card4[1]} and their new total is {hand_val_computer}.")
        while hand_val_computer <= 21:
            if hand_val_computer <= 17:
                drawcard = deck.pop()
                hand_val_computer += card_values[drawcard[0]]          
                if drawcard[0] == 'Ace':
                    aces_comp += 1
                if hand_val_computer > 21 and aces_comp > 0:
                    aces_comp -= 1
                    hand_val_computer -= 10
                state.gprint(f"Dr. Buck draws the {drawcard[0]} of {drawcard[1]}. Their new total is {hand_val_computer}.")
            else:
                state.gprint(f"Dr. Buck stands with {hand_val_computer}.")
                break
        if hand_val_computer > 21:
            buck_Health= buck_Health - hand_val_player
            state.gprint(f"Dr. Buck busted. You deal {hand_val_player} to him.")
        elif hand_val_player > hand_val_computer:
            damage_Buck = hand_val_player-hand_val_computer
            buck_Health = buck_Health - damage_Buck
            state.gprint(f"You deal {damage_Buck} to Dr. Buck.")
        elif hand_val_computer > hand_val_player:
            damage_player = hand_val_computer - hand_val_player
            player_Health = player_Health - damage_player
            state.gprint(f"Dr. Buck deals {damage_player} to you.")
        else: 
            state.gprint("Your hand values were the same neither person deals any damage.")
    if buck_Health<=0:
        state.gprint("""
You have defeated Dr. Buck in a game of blackjack. He 
looks at you with dread and allows you to leave the room
answer key in hand. You succesfully pass the final exam 
and are able to move on with your college journey.
              """)
        menu(state)
    elif player_Health<=0:
        state.gprint("""
Dr. Buck defeats you in his card game and rips the answer key
out of your hand. He stands up and tightly grabs your arm as he
escorts you down the hall. You pass numerous students who point
and laugh at you before arriving at the office of student conduct.
You are told your time at UMD has come to an end. You have been expelled.
              """)
        menu(state)
#File 2
# This file contains the large dictionary of halls and their information
# Also contains the functions relating to the actions taken in each hall/room

def unlock_bucks_acid(state: GameState):
    print("--------------------")
    acid_used = False
    item_used = "acid"
    prev_exit = locations[state.location]["exits"]["enter"]
    for x in range(len(state.backpack) -1,-1,-1):
        item = state.backpack[x]
        if item.get("name") == "beaker of acid":
            state.gprint("Pouring the acid upon the chains they quickly dissolve and fall away.")
            locations['heller3']['exits'].update(enter= "drbucks_locked_dog")
            acid_used = True
            del state.backpack[x]

    if not acid_used:
        state.gprint("You do not have acid to melt the chains")

    bucks_door_check(state, item_used, prev_exit)
    
def unlock_bucks_chicken(state: GameState):
    print("--------------------")
    chicken_used = False
    item_used = "chicken"
    prev_exit = locations[state.location]["exits"]["enter"]
    for x in range(len(state.backpack) -1,-1,-1):
        item = state.backpack[x]
        if item.get("name") == "chicken wing":
            state.gprint("Waving the chicken wing in front of the dog you gain its attention. Tossing it aside the dog sprints after it.")
            locations['heller3']['exits'].update(enter= "drbucks_locked_chain")
            chicken_used = True
            del state.backpack[x]

    if not chicken_used:
        state.gprint("You need to find chicken to distract the dog.")

    bucks_door_check(state, item_used, prev_exit)

def bucks_door_check(state: GameState, item_used, prev_exit):
    if prev_exit == "drbucks_locked_dog" and item_used == "chicken":
        locations['heller3']['exits'].update(enter= "drbucks_office")

    if prev_exit == "drbucks_locked_chain" and item_used == "acid":
        locations['heller3']['exits'].update(enter= "drbucks_office")

def unlock_chem_lab(state: GameState):
    print("--------------------")
    item_found = False
    for x in state.backpack:
        if x.get("name") == "bronze key":
            state.gprint("You unlocked the door")
            locations['chemistry4']['exits'].update(enter= "chemistrylab")
            item_found = True

    if not item_found:
        state.gprint("You can't unlock this door")

locations = {
    "dorm": {
        "initialDescription": "You are standing in your dorm. Your roommate, Brad, is watching TV on his bed. In your room there is a door, a window, and your desk.",
        "description": "DORM\nBrad is still watching TV. There is a window, a door, and a desk.",
        "exits": {"exit": "dormhall"},
        "actions": {
            "open window": "You see the campus and feel a gust off Lake Superior. Rain falls in your room.",
            "jump out window": "You fall to your death. What were you thinking?",
            "backpack": "**BACKPACK COMPONENTS**"
        }
    },
    "dormhall": {
        "initialDescription": "***",
        "description": "You've made your way to the main dorm hallway. You see a sign for the LSH office to the north.",
        "exits": {"north": "LSHdesk", "enter": "dorm", "south": "dorm_entryway"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"},
        "items": {"ucard": {"name": "ucard", "description": "You see a Ucard laying face down on the floor"}}
    },
    "LSHdesk": {
        "initialDescription": "***",
        "description": "You are in front of the LSH office",
        "exits": {"south": "dormhall", "east": "diningcenter"},
        "actions": {"open door": "Nope",
                   "backpack": "**BACKPACK COMPONENTS**"}
    },
    "diningcenter": {
        "initialDescription": "***",
        "description": "You stop a moment to look inside the dining center. The food looks like it is suitable for a dog.",
        "exits": {"west": "LSHdesk", "east": "kirby3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"},
        "items": {"chicken wing": {"name": "chicken wing", "description": "Laying near the entrance you see a discarded chicken wing"}}
    },
    "kirby3": {
        "initialDescription": "***",
        "description": "You are at the top of a large and busy stairwell. To your north and south are two sets of doors.",
        "exits": {"north": "rafters", "south": "kirbyBall", "west": "diningcenter", "down": "kirby2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "rafters": {
        "initialDescription": "***",
        "description": "You enter a bare white room with some tables",
        "exits": {"south": "kirby3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "kirbyBall": {
        "intialDescription": "***",
        "description": "Large room with pillars and wooden floor",
        "exits": {"north": "kirby3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "kirby2": {
        "initialDescription": "***",
        "description": "You are halfway down the stairs. To the south is the Office of Diversity and Inclusion. To the north, you spot the school store and a food court.",
        "exits": {"north": "kirbyplaza2", "south": "officediversity", "up": "kirby3", "down": "kirby1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "officediversity":{
        "initialDescription": "***",
        "description": "You enter a room with a sitting area and smaller office space, you can not go further.",
        "exits": {"north": "kirby2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "kirby1": {
        "initialDescription": "***",
        "description": "You are at the bottom of a large stairwell. You see hallways leading in all directions.",
        "exits": {"north": "kirbyplaza1", "south": "heller1", "up": "kirby2",  "down": "soloncc"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "kirbyplaza1": {
        "initialDescription": "***",
        "description": "-----",
        "exits": {"south": "kirby1", "north": "techcenter","east": "cinahall1","up": "kirbyplaza2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
     "kirbyplaza2": {
        "initialDescription": "***",
        "description": "There are no classrooms in this area and few students walking about. you can smell some nice scents to the north.",
        "exits": {"down": "kirbyplaza1", "south": "kirby2", "north": "foodcourt", "up": "kirbyplaza3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "foodcourt": {
        "initialDescription": "***",
        "description": "Wow! There is real food being made here and it looks somewhat decent.",
        "exits": {"down": "techcenter", "south": "kirbyplaza2", "up": "kirbyplaza3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
     "kirbyplaza3": {
        "initialDescription": "***",
        "description": "You climb up a pristine staircase to the top floor of kirby plaza and find a bunch of IT offices.",
        "exits": {"down": "kirbyplaza2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "techcenter": {
        "initialDescription": "***",
        "description": "Around you theres several benches with tables",
        "exits": {"south": "kirbyplaza1", "north": "thegrind", "east": "bohannon1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "thegrind": {
        "initialDescription": "***",
        "description": "You walk into a little shop cornor with snacks and drinks",
        "exits": {"south": "techcenter", "north": "outsidekathrynalib", "west": "labovitzfl1", "east": "montague1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"},
        "items": {"dnergy drink": {"name": "energy drink", "description":"A powerful energy drink that promises to keep you awake for hours."}}
        
    },
    "heller1": {
        "initialDescription": "***",
        "description": "The hallway continues to run north-south. There is a stairwell that takes you to the second floor of Heller Hall.",
        "exits": {"north": "kirby1", "south": "lifescience1", "up": "heller2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "heller2": {
        "initialDescription": "***",
        "description": "This hallway is of no interest to you.",
        "exits": {"down": "heller1", "up": "heller3", "south": "lifescience2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "heller3": {
        "initialDescription": "***",
        "description": "You are on the top floor of Heller Hall. A door with chains and a vicious dog blocks your way.",
        "exits": {"down": "heller2", "enter": "drbucks_office_locked", "south": "lifescience3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**",
                    "acid": unlock_bucks_acid,
                    "chicken": unlock_bucks_chicken}
    },
    "drbucks_office_locked": {
        "description": "As you approach the door the vicous dog stands and starts to growl",
        "exits": {"back": "heller3"}
    },
    "drbucks_locked_chain": {
        "description": "The door is still securely shut with chains. Find something to break or melt the chains.",
        "exits": {"back": "heller3"}
    },
    "drbucks_locked_dog": {
        "description": "The dog still stands in your way. Find something to distract it",
        "exits": {"back": "heller3"}
    },
    "lifescience1": {
        "initialDescription": "***",
        "description": "Life Science Floor 1 has large lecture halls. A hallway leads south and east.",
        "exits": {"north": "heller1", "south": "MWAH1", "east": "chemistry2", "up": "lifescience2", "down": "lifesciencegr"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "lifesciencegr": {
        "initialDescription": "***",
        "description": "Some classrooms and offices. You faintly remember traveling to the observatory as a kid.",
        "exits": {"up": "lifescience1", "south": "MWAHgr"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "lifescience2": {
        "initialDescription": "***",
        "description": "This hallway looks like every other one on campus.",
        "exits": {"north": "heller2", "down": "lifescience1", "up": "lifescience3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "lifescience3": {
        "initialDescription": "***",
        "description": "The top floor of the Life Science building. A hallway breaks north and a skyway is to the west.",
        "exits": {"north": "heller3", "west": "swensonsci1", "down": "lifescience2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "MWAH1": {
        "initialDescription": "***",
        "description": "You are at the farthest south point on campus. A hall heads north and east.",
        "exits": {"north": "lifescience1", "east": "medicinehall1", "up": "MWAH2", "down": "MWAHgr"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "MWAHgr": {
        "initialDescription": "***",
        "description": "You are on the ground floor of Marshall W. Alworth Hall. There is a set of stairs and a circular building you're unsure about.",
        "exits": {"up": "MWAH1", "enter": "planetarium", "north": "lifesciencegr"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "MWAH2": {
        "initialDescription": "***",
        "description": "Nothing seems to interest you on this floor.",
        "exits": {"down": "MWAH1", "up": "MWAH3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "MWAH3": {
        "initialDescription": "***",
        "description": "Nothing seems to interest you on this floor.",
        "exits": {"down": "MWAH2", "up": "MWAH4"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "MWAH4": {
        "initialDescription": "***",
        "description": "Nothing seems to interest you on this floor",
        "exits": {"down": "MWAH3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "swensonsci1": {
        "initialDescription": "***",
        "description": "The Swenson building feels new and open, with large amounts of natural light. To the east is a skyway connecting to the Life Science building.",
        "exits": {"east": "lifescience3", "down": "swensonscigr", "up": "swensonsci2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "swensonscigr": {
        "initialDescription": "***",
        "description": "You are on the ground floor of Swenson Science.",
        "exits": {"up": "swensonsci1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "swensonsci2": {
        "initialDescription": "***",
        "description": "There are some labs and classrooms up here, but all the doors seem locked.",
        "exits": {"down": "swensonsci1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "chemistry1": {
        "initialDescription": "***",
        "description": "A hallway runs north to south with locked doors to the south.",
        "exits": {"north": "soloncc", "up": "chemistry2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "chemistry2": {
        "initialDescription": "***",
        "description": "The chemistry building appears very old and run down. A hallway takes you west to the Life Science building.",
        "exits": {"west": "lifescience1", "south": "medicinehall1", "down": "chemistry1", "up": "chemistry3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "chemistry3": {
        "initialDescription": "***",
        "description": "There is some caution tape blocking the stairs on the way up.",
        "exits": {"down": "chemistry2", "up": "chemistry4"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "chemistry4": {
        "initialDescription": "***",
        "description": "This floor feels abandoned, but you notice a light on in a lab.",
        "exits": {"down": "chemistry3", "enter": "lockedchem"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**",
                    "unlock": unlock_chem_lab},
    },
    "lockedchem": {
        "description": "This door is locked find the key.",
        "exits": {"back": "chemistry4"}
    },
    "chemistrylab": {
        "initialDescription": "***",
        "description": "The lights flicker as you enter the room. Around you there are several tables littered with onjects you don't recognize.",
        "exits": {"exit": "chemistry4"},
        "items": {"beaker of acid": {"name": "beaker of acid", "description": "Across the room you see what youve come for. The bright green liquid swirling around. A beaker of acid."}}
    },
    "soloncc": {    #will need to make a "special_room", needs wedge and missing 4-5 exits.
        "initialDescription": "***",
        "description": "A hallway leads north, and another leads east. Students study intently.",
        "exits": {"north": "cinahallgr", "east": "darlandadmin", "up": "kirby1", "south": "chemistry1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "darlandadmin": {
        "initialDescription": "***",
        "description": "The doors ahead are locked.",
        "exits": {"west": "soloncc"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "cinahallgr": {
        "initialDescription": "***",
        "description": "This hallway feels darker than the rest. Doors advertise photography classes.",
        "exits": {"south": "soloncc", "up": "cinahall1", "north": "humanities2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "cinahall1": {
        "initialDescription": "***",
        "description": "You have arrived at Cina Hall. The area is bright and lively.",
        "exits": {"north": "humanities3", "west": "kirbyplaza1", "down": "cinahallgr", "up": "cinahall2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "cinahall2": {
        "initialDescription": "***",
        "description": "This floor is very boring. A hall leads to Humanities, and stairs go up and down.",
        "exits": {"north": "humanities4", "down": "cinahall1", "up": "cinahall3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "cinahall3": {
        "initialDescription": "***",
        "description": "You have wandered to Cina Hall floor three, but there is nothing of interest here.",
        "exits": {"down": "cinahall2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "humanities1": {
        "initialDescription": "***",
        "description": "Stretching eastward is a long hallway lined with locked music practice rooms. Vacant classrooms line the other side. There are no windows, and the hallway appears abandoned.",
        "exits": {"east": "webermusic1", "south": "abanderson1", "up": "humanities2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "humanities2": {
        "initialDescription": "***",
        "description": "The humanities hall is mostly comprised of music classrooms and offices. Hallways lead in all directions but west.",
        "exits": {"north": "bohannongr", "west": "cinahallgr", "south": "abanderson2", "east": "webermusic2", "down": "humanities1", "up": "humanities3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "humanities3": {
        "initialDescription": "***",
        "description": "A long, bland hallway stretches out in front of you. Stairs lead up and down, with a hallway leading south.",
        "exits": {"west": "cinahall1", "south": "abanderson3", "down": "humanities2", "up": "humanities4"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "humanities4": {
        "initialDescription": "***",
        "description": "This building has more floors than expected. Stairs take you down to other humanities floors.",
        "exits": {"west": "cinahall2", "south": "abanderson4", "down": "humanities3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "webermusic1": {
        "initialDescription": "***",
        "description": "You are on the bottom floor of Weber Music Hall. There is a closed ticket stand, and a dimly lit hallway heads west.",
        "exits": {"west": "humanities1", "north": "rsopgr", "up": "webermusic2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "webermusic2": {
        "initialDescription": "***",
        "description": "Weber Music Hall's performance stage is locked. A hallway extends north past Romano Gym, with stairs descending to the first floor.",
        "exits": {"north": "rsop1", "west": "humanities2", "down": "webermusic1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "rsop1": {
        "initialDescription": "***",
        "description": "Standing in a lobby of a sports arena you see closed doors except to the south. You hear the jingle of a key falling on the ground.",
        "exits": {"south": "webermusic2"},
        "actions": {},
        "items": {"bronze key": {"name": "bronze key", "description": "You see a bronze key tossed aside on the ground. The key is engraved with CHEM LAB"}}
    },
    "bohannongr": {
        "initialDescription": "***",
        "description": "You notice Bohannon 90, a massive lecture hall. A hallway runs west to Ven Den and also runs north and south.",
        "exits": {"south": "humanities2", "north": "montaguegr", "west": "venden", "up": "bohannon2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "bohannon1": {
        "initialDescription": "***",
        "description": "This hall bores you. Go west to Kirby Plaza. Stairs take you to other Bohannon floors.",
        "exits": {"west": "techcenter", "down": "bohannongr", "up": "bohannon2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "bohannon2": {
        "initialDescription": "***",
        "description": "The school seems to be full of classrooms, and western exits take you to Kirby Plaza.",
        "exits": {"west": "foodcourt", "down": "bohannon1", "up": "bohannon3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "bohannon3": {
        "initialDescription": "***",
        "description": "Another boring hallway. Go west to Kirby Plaza.",
        "exits": {"west": "kirbyplaza3", "down": "bohannon2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "montaguegr": {
        "initialDescription": "***",
        "description": "Montague Hall's ground floor has large lecture halls. A hallway runs north and south.",
        "exits": {"south": "bohannongr", "north": "edugr", "east": "marshallpacfl1", "up": "montague1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "montague1": {
        "initialDescription": "***",
        "description": "Lecture halls surround you, with stairs leading up and down.",
        "exits": {"west": "thegrind", "down": "montaguegr", "up": "montague2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "montague2": {
        "initialDescription": "***",
        "description": "---",
        "exits": {"down": "montague1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "edugr": {
        "initialDescription": "***",
        "description": "This open room has chairs that remind you of kindergarten. Classrooms line the walls.",
        "exits": {"south": "montaguegr", "north": "engineering1", "up": "edu1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "edu1": {
        "initialDescription": "***",
        "description": "From the upper floor, you can see down to the ground floor. Rooms line the walls.",
        "exits": {"west": "outsidekathrynalib", "down": "edugr"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "engineering1": {
        "initialDescription": "***",
        "description": "Engineering labs line the halls, showcasing senior projects. A tunnel leads somewhere unknown.",
        "exits": {"south": "edugr", "north": "civilengfl1sec2", "east": "vosskovach1", "up": "engineering2", "enter": "outsidekathrynalib"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "engineering2": {
        "initialDescription": "***",
        "description": "The upper floor of the engineering building is less interesting.",
        "exits": {"east": "vosskovach2", "down": "engineering1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "vosskovach1": {
        "initialDescription": "***",
        "description": "You step into the hall and are greeted by a potent chemical scent.",
        "exits": {"north": "civilengfl1sec1", "west": "engineering1", "up": "vosskovach2", "down": "vosskovachbs"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "vosskovach2": {
        "initialDescription": "***",
        "description": "Voss Kovach Floor 2, with labs, classrooms, and offices.",
        "exits": {"west": "engineering2", "down": "vosskovach1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "vosskovachbs": {
        "initialDescription": "***",
        "description": "The bottom floor of Voss is tightly sealed. Stairs lead back up.",
        "exits": {"up": "vosskovach1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "civilengfl1sec1": {
        "initialDescription": "***",
        "description": "You walk into a hallway containing numerous mechanical workshops on both sides. The hallway continues west, and stairs go up. A different building lies South of you.",
        "exits": {"south": "vosskovach1", "up": "civilengfl2", "west": "civilengfl1sec2"},
        "actions": {}
    },
    "civilengfl1sec2": {
        "initialDescription": "***",
        "description": "You are in the western section of the civil engineering building. This area houses lots of locked classrooms. The building continues east, to the south is the engineering building and stairs take you to the upper floor.",
        "exits": {"east": "civilengfl1sec1", "south": "engineering1", "up": "civilengfl2"},
        "actions": {}
    },
    "civilengfl2": {
        "initialDescription": "***",
        "description": "There is an overlook of a couple of shops up here but they all seem empty. The rooms up here also appear unused. Stairs take you back to the first floor of the civil engineering building.",
        "exits": {"down": "civilengfl1sec1"},
        "actions": {}
    },
    "labovitzfl1": {
        "initialDescription": "***",
        "description": "You are wowed by the architecture of this building. Natural light floods in. Stairs lead to upper floors, and a hallway leads east.",
        "exits": {"east": "thegrind", "up": "labovitzfl2"},
        "actions": {}
    },
    "labovitzfl2": {
        "initialDescription": "***",
        "description": "The middle floor is nice but only has classrooms. Stairs go up and down.",
        "exits": {"down": "labovitzfl1", "up": "labovitzfl3"},
        "actions": {}
    },
    "labovitzfl3": {
        "initialDescription": "***",
        "description": "The upper floor is even better than the bottom two. But nothing but the views and the architecture are interesting. Stairs go down.",
        "exits": {"down": "labovitzfl2"},
        "actions": {}
    },
    "outsidekathrynalib": {
        "initialDescription": "***",
        "description": "You are outside the entrance to the library. A unique staircase leads to the engineering building. To the south is Kirby Plaza.",
        "exits": {"south": "thegrind", "down": "engineering1", "enter": "kathrynafl1", "east": "edu1"},
        "actions": {}
    },
    "kathrynafl1": {
        "initialDescription": "***",
        "description": "You have reached the main floor of the library. There are not a lot of books on this floor, but there are plenty of places to study. You hear people talking on this floor, so it must be a conversation floor. Stairs lead up 3 more floors.",
        "exits": {"exit": "outsidekathrynalib", "up": "kathrynafl2"},
        "actions": {}
    },
    "kathrynafl2": {
        "initialDescription": "***",
        "description": "The second floor of the library still does not have many books and is more geared towards studying. A staircase leads up and down. This floor is much quieter than the other floors. To the south is the annex of the library.",
        "exits": {"down": "kathrynafl1", "up": "kathrynafl3", "south": "libraryannexfl2"},
        "actions": {}
    },
    "kathrynafl3": {
        "initialDescription": "***",
        "description": "You find your way to the third floor of the library and see large amounts of books and quiet study areas. Stairs continue up and down. Your legs feel weak because of all the stairs you have done.",
        "exits": {"down": "kathrynafl2", "up": "kathrynafl4"},
        "actions": {}
    },
    "kathrynafl4": {
        "initialDescription": "***",
        "description": "The upper floor of the library has the most books and countless spots to study on your own. Your only option to leave is go back down all the steps you climbed up to get here.",
        "exits": {"down": "kathrynafl3"},
        "actions": {}
    },
    "libraryannexfl2": {
        "initialDescription": "***",
        "description": "You are in the library annex. You're confused by the purpose of this room besides housing books. Why isn't this called the library? You are super confused. Stairs lead down, and the library is to the north.",
        "exits": {"north": "kathrynafl2", "down": "libraryannexfl1"},
        "actions": {}
    },
    "libraryannexfl1": {
        "initialDescription": "***",
        "description": "You are in the first floor of the library annex. Stairs lead back up.",
        "exits": {"up": "libraryannexfl2"},
        "actions": {}
    },
    "medicinehall1": {
        "initialDescription": "***",
        "description": "How did you get in here? The doors were supposed to be locked. The School of Medicine is very posh and well-kept. To the north is the disgusting chemistry building, and to the south is MWAH. Stairs take you up and down but remember you are not supposed to be here.",
        "exits": {"north": "chemistry2", "west": "MWAH1", "down": "medicinehallgr", "up": "medicinehall2"},
        "actions": {}
    },
    "medicinehallgr": {
        "initialDescription": "***",
        "description": "Down here is nice and tidy compared to every other basement in the school. You should really be going now. Take the stairs up, it is your only option.",
        "exits": {"up": "medicinehall1"},
        "actions": {}
    },
    "medicinehall2": {
        "initialDescription": "***",
        "description": "This floor is just like the main floor. You should really be going—you are going to get caught. Take the stairs down. They may also go up.",
        "exits": {"down": "medicinehall1", "up": "medicinehall3"},
        "actions": {}
    },
    "medicinehall3": {
        "initialDescription": "***",
        "description": "Why waste your time coming to the top floor that is the same as the floors below it? GO BACK DOWN!",
        "exits": {"down": "medicinehall2"},
        "actions": {}
    },
    "venden": {
        "initialDescription": "***",
        "description": "The lights turn on when you enter the room. It’s just a simple lounge area. You notice a microwave that might be useful later.",
        "exits": {"east": "bohannongr", "up": "bohannon1"},
        "actions": {}
    },
    "marshallpacfl1": {
        "initialDescription": "***",
        "description": "You can tell the space you are in is intended for public viewing. It is clean and contains unique art. To the west is a hallway that leads to Montague Hall. Stairs lead up to access the upper level of the performance hall, but the doors are shut. Stairs also lead to the basement. A hallway takes you east to the engineering building.",
        "exits": {"west": "montagueflgr", "down": "marshallpacbs", "up": "marshallpacfl2", "east": "engineering1"},
        "actions": {}
    },
    "marshallpacfl2": {
        "initialDescription": "***",
        "description": "You are on the balcony of the performing arts center. Nothing up here seems open. Stairs lead back down.",
        "exits": {"down": "marshallpacfl1"},
        "actions": {}
    },
    "marshallpacbs": {
        "initialDescription": "***",
        "description": "This room is very creepy. You hear something creaking in the room, but you cannot see it because the lights are off. You get creeped out and think it is best to go back up the stairs.",
        "exits": {"up": "marshallpacfl1"},
        "actions": {}
    },
    "abanderson1": {
        "initialDescription": "***",
        "description": "This building is shaped like a rectangle with pottery classes around the outside. In fact, you see some students making pots right now. You look for stairs but see none. To leave, you must go north.",
        "exits": {"north": "humanities1", "up": "abanderson2"},
        "actions": {}
    },
    "abanderson2": {
        "initialDescription": "***",
        "description": "You notice this building is just one big square hallway with empty classrooms. Stairs lead up but not down, oddly. Humanities is to the north.",
        "exits": {"north": "humanities2", "down": "abanderson1", "up": "abanderson3"},
        "actions": {}
    },
    "abanderson3": {
        "initialDescription": "***",
        "description": "This floor serves no purpose to you. Go north or take the stairs up or down to leave.",
        "exits": {"north": "humanities3", "down": "abanderson2", "up": "abanderson4"},
        "actions": {}
    },
    "abanderson4": {
        "initialDescription": "***",
        "description": "This floor serves no purpose to you. Go north or take the stairs down to leave.",
        "exits": {"north": "humanities4", "down": "abanderson3"},
        "actions": {}
    },
    "drbucks_office": {
        "initialDescription": "***",
        "description": "You have managed to break into Dr. Buck's office. His desk is riddled with papers. You notice a bottle on the desk labeled 'Tears of Previous Students'. Your body shakes as your nerves increase. You finally find what you are looking for, a briefcase labeled 'Final Exam'. You open it up and find the answer key. Just as you are about to leave, Dr. Buck enters the room.",
        "exits": {"exit": "heller3"},
        "actions": {"fight":blackJack}
    },
    #Intergrated into the room above
    "drbuck_confrontation": {
        "initialDescription": "***",
        "description": "See boss fight confrontation.",
        "exits": {},
        "actions": {"bribe": "If over 100 dollars you win else game over", "other": "game over"}
    },
    "dorm_entryway": {
        "initialDescription": "***",
        "description": "There is a storm raging outside. Only a fool would adventure outside the comfort of the buildings",
        "exits": { "north":"dormhall", "exit":"cold_dark"},
        "actions": {}
    },
    "cold_dark":{
        "description":"The cold water beats against your head. The wind rattles your soul as you fight your way down the path off campus. You should turn back.",
        "exits": {"back":"dorm_entryway", "forward": "game_over"},
        "actions" : {}
    },
    "game_over":{
        "description" : "The wind picks you up and blows you away. You get lost in the dark rain on the streets of Duluth. You approach a homeless man for help and he stabs you.",
    },
    "planetarium": {
        "initialDescription": "***",
        "description": "You enter the planetarium to see a strange machine in the center of a circular room. The only other thing you see is old squeaky chairs.",
        "exits": {"exit": "MWAHgr"},
        "actions": {}
    }
} 



# Game state Class
state = GameState()
#File 3
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
            print(state.location)
            state.gprint(self.desc)
        else:
            print(state.location)
            state.gprint(self.desc)

    def inspect_hall(self):
        self.inspected = True
        for item in self.items.values():
            print("--------------------")
            state.gprint(item.get("description"))
        if len(self.items) == 0:
            print("--------------------")
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
exitWindow = ["window", "jump out"]
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
                "window": exitWindow,
                "up": up_stairs,
                "down": down_stairs,
                "back": backup,
                "forward":forward,
                }

# Action Lists
backpackNames = ["i", "b", "backpack", "inventory", "back pack", "open backpack", "look in backpack"]
jumpOutWindow = ["jump out", "jump out window", "exit window", "jump"]
openWindow = ["open", "open window", "window"]
unlockDoor = ["unlock door", "unlock"]
meltChains = ["use acid", "melt chain", "use beaker of acid"]
chickenDog = ["toss chicken wing", "use chicken wing", "distract dog"]
fight = ["fight","attack","take exam"]

action_aliases = {"jump out window": jumpOutWindow,
                 "backpack": backpackNames,
                 "open window": openWindow,
                 "unlock": unlockDoor,
                 "acid": meltChains,
                 "chicken": chickenDog,
                 "fight" : fight
                 }

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
    if exit_take in exit_aliases:
        state.gprint("That is not a valid direction here")
    elif action_take in action_aliases:
        state.gprint("That is not a valid action here")
    else:
        state.gprint("I don't know how to " + user_input)

# Function for backpack
def display_backpack(state):
    print("---- Backpack ----")
    for item in state.backpack:
        print(item["name"])




# Main Game Handler
def handle_location(location_name):
    print("--------------------")

    current_hall = halls[location_name]
    current_hall.visit_hall()
    if location_name=="game_over":
       menu(state)

    user_input = state.uinput("> ")
    exit_take = get_exit(user_input)    
    action_take = get_action(user_input)

    if user_input == "inspect":
        current_hall.inspect_hall()
        
    elif "grab" in user_input and current_hall.inspected:
        user_item = user_input.split("grab ")[-1]
        for item in current_hall.items.values():
            if user_item == item.get("name"):
                state.backpack.append(item)
                del current_hall.items[user_item]
                print("--------------------")
                state.gprint("You got the item!!")
                break
            else:
                state.gprint("That is not a valid item")

    elif "backpack" in user_input:
        display_backpack()

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
    while True:
        handle_location(state.location)
#start menu and where player returns to after winning or losing.
def menu(state):
    state.gprint("""
---------WELCOME TO BULLDOG BRAWl---------
    1. Play game
    2. Instructions
    3. Exit""")
    choice = state.uinput(">")
    if choice =='1':
        game_loop(state)
    elif choice =='2':
        state.gprint("""
---------Instructions---------
- Navigate the halls using commands like 'go north', 'go south', 'up', or 'down'.
- Inspect rooms to find items and uncover hidden details.
- Use 'grab <item>' to pick up an item after inspecting.
- Manage your items using 'backpack' to check what you've collected.
- Your goal is to explore, find items, and steal the final answer keys.!
        """)
        menu(state)
    elif choice =='3':
        sys.exit()
    else:
        state.gprint("Invalid input")

menu(state)

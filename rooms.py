import GameState
import sys
from Blackjack_Battle import blackJack
global locations

# This file contains the large dictionary of halls and their information
# Also contains the functions relating to the actions taken in each hall/room

heller3 = "You are on the top floor of Heller Hall. A door with chains and a vicious dog blocks your way."
heller3_dog = "Melted chains frame the door but the dog still sits there."
heller3_chains = "The dog no longer stands in your way but chains block the door still."
heller3_no_barriers = "Nothing stands in your way to enter now."

def unlock_bucks_acid(state: GameState):
    print("--------------------")
    acid_used = False
    item_used = "acid"
    prev_exit = locations['heller3']["exits"]["enter"]
    for x in range(len(state.backpack) -1,-1,-1):
        item = state.backpack[x]
        if item.get("name") == "beaker of acid":
            state.gprint("Pouring the acid upon the chains they quickly dissolve and fall away.")
            locations['heller3']['exits'].update(enter= "drbucks_locked_dog")
            locations['heller3']["description"].update(desc= heller3_dog)
            acid_used = True
            del state.backpack[x]
            del locations['heller3']['actions']['acid']
            if state.location == "drbucks_office_locked":
                state.location = "drbucks_locked_dog"

    if not acid_used:
        state.gprint("You do not have acid to melt the chains")

    bucks_door_check(state, item_used, prev_exit)
    
def unlock_bucks_chicken(state: GameState):
    print("--------------------")
    chicken_used = False
    item_used = "chicken"
    prev_exit = locations['heller3']["exits"]["enter"]
    for x in range(len(state.backpack) -1,-1,-1):
        item = state.backpack[x]
        if item.get("name") == "chicken wing":
            state.gprint("Waving the chicken wing in front of the dog you gain its attention. Tossing it aside the dog sprints after it.")
            locations['heller3']['exits'].update(enter= "drbucks_locked_chain")
            locations['heller3']["description"].update(desc= heller3_chains)
            chicken_used = True
            del state.backpack[x]
            del locations['heller3']['actions']['chicken']
            if state.location == "drbucks_office_locked":
                state.location = "drbucks_locked_chain"

    if not chicken_used:
        state.gprint("You need to find chicken to distract the dog.")

    bucks_door_check(state, item_used, prev_exit)

def bucks_door_check(state: GameState, item_used, prev_exit):
    if prev_exit == "drbucks_locked_dog" and item_used == "chicken":
        locations['heller3']['exits'].update(enter= "drbucks_office")
        locations['heller3']["description"].update(desc= heller3_no_barriers)
        state.location = "heller3"

    if prev_exit == "drbucks_locked_chain" and item_used == "acid":
        locations['heller3']['exits'].update(enter= "drbucks_office")
        locations['heller3']["description"].update(desc= heller3_no_barriers)
        state.location = "heller3"

def unlock_chem_lab(state: GameState):
    print("--------------------")
    item_found = False
    for x in state.backpack:
        if x.get("name") == "chemistry key":
            state.gprint("You unlocked the door")
            locations['chemistry4']['exits'].update(enter= "chemistrylab")
            del locations["chemistry4"]["specialDesc"]["desc"]
            item_found = True
            if state.location == "lockedchem":
                state.location = "chemistry4"

    if not item_found:
        state.gprint("You can't unlock this door")

def grad_student(state: GameState):
    while True:
        print("--------------------")
        state.gprint("Grad Student: H-hello are you a student of Doctor Buck's? (yes or no)")
        user_input = state.uinput("> ")
        if user_input == "yes":
            print("--------------------")
            state.gprint("Grad Student: He always creates extreme exams. Please go to his office and get the Final Exam for the sake of other. Here's a key to a lab on the fourth floor of the chemistry building. There's acid in there that can melt straight through the chains on his door.")
            state.gprint("\nYou got the chemistry key needed for the lab.")
            state.backpack.append({"name": "chemistry key"})
            break
        elif "no":
            print("--------------------") 
            state.gprint("Grad Student: That's too bad. I wanted other students to succeed.")
            break
        else:
            print("--------------------")
            state.gprint("Grad Student: Huh what was that?")

def frat_guys(state: GameState):
    while True:
        print("--------------------")
        state.gprint("""
Frat Guy #1: Are you sure it's there?\n
Frat Guy #2: Trust me bro it's in that office.\n
Frat Guy #3: I heard it was password protected by a complex equation though..\n
Frat Guy #2: Hey you there you seem smart.\n
Frat Guy #3: Yeah do use a favor. Break into our math teacher's office for us.\n
Frat Guy #1: If you steal the exam key we'll put you on the list for our next party.\n
                    """)
        state.gprint("Do you accept the quest to steal the key for them (yes or no)")
        user_input = state.uinput("> ")
        if user_input == "yes":
            print("--------------------")
            state.gprint("Frat Guy #2: Great! The office is in soloncc. Meet us in Labovitz when you get it.")
            locations['soloncc']['actions'].update(keypad= unlock_office)
            locations['soloncc']['specialDesc'].update(desc= "You see the office that the frat guys said to find.")
            locations['labovitzfl1']['specialDesc'].update(desc= "Three frat guys sit huddled around a table off to the side.")
            locations['labovitzfl1']['actions'].update(talk= give_key)
            del locations['underground']['specialDesc']['desc']
            del locations['underground']['actions']['talk']
            break
        elif user_input == "no":
            print("--------------------")
            state.gprint("Frat Guy #1: You'll never be accepted into a party during your time at UMD then!!")
            del locations['underground']['specialDesc']['desc']
            del locations['underground']['actions']['talk']
            break
        else:
            print("--------------------")
            state.gprint("That is not a valid response.")

def unlock_office(state: GameState):
    print("--------------------")
    state.gprint("As you approach the lock you see a sticky note stuck right above the key pad.")
    state.gprint("The note says - The code to my office is: sin(90)")
    state.gprint("Attempt to unlock door (yes or no)")
    attempts = 5
    user_input = state.uinput("> ")
    while user_input == "yes" and attempts != 0:
        print("--------------------")
        answer = 1
        state.gprint("Enter the answer")
        user_answer = state.uinput("> ")
        try:
            if int(user_answer) == answer:
                print("--------------------")
                state.gprint("BEEP BEEP - CLICK")
                state.gprint("The door is now unlocked")
                locations['soloncc']['exits'].update(enter= "math_office")
                break
            else:
                print("--------------------")
                state.gprint("BEEP BEEP - WRONG")
                attempts -= 1
                state.gprint(f"You now have {attempts} attempts remaining")
        except ValueError:
            if user_answer == "exit":
                break
            else:
                state.gprint("That is not a number!")
    
    if attempts == 0:
        state.gprint("You got caught trying to trying to break into the office and was expelled.")
        sys.exit()

def give_key(state: GameState):
    while True:
        print("--------------------")
        state.gprint("Frat Guy #1: Hey you're here! Do you have the key?\n")
        state.gprint("Answer (yes or no)")
        user_input = state.uinput("> ")
        if user_input == "yes":
            while True:
                print("--------------------")
                state.gprint("Frat Guy #3: Great! Hand it over to us.\n")
                state.gprint("Give exam key or refuse")
                user_action = state.uinput("> ")
                if user_action == "give exam key":
                    print("--------------------")
                    state.gprint("Frat Guy #1: You saved us now we'll be able to pass algebra.")
                    state.backpack.append({"name": "invite"})
                    locations['dormhall']['exits'].update(south= "offcampus")
                    return
                elif user_action == "refuse":
                    print("--------------------")
                    state.gprint("Frat Guy #1: What!?!? How dare you!\n")
                    state.gprint("Frat Guy #3: We're gonna beat you up now!!\n")
                    state.gprint("After what felt like forever they finally left you with all broken limbs for refusing them. Because of that you went to the hospital and was unable to steal the final exam.\n")
                    sys.exit()
                else:
                    print("--------------------")
                    state.gprint("Frat Guy #3: Huh what was that?\n")
        elif user_input == "no":
            print("--------------------")
            state.gprint("Frat Guy #2: Why the hell are you wasting our time then?\n")
            state.gprint("Frat Guy #1: Get out of here loser.\n")
            break
        else:
            print("--------------------")
            state.gprint("Frat guy #2: Huh what was that? Sounded like gibberish.\n")

def room_mate(state: GameState):
    print("--------------------")
    state.gprint("Brad: Leave me alone I'm watching Real House Wives of Beverly Hills")

def open_window(state: GameState):
    print("--------------------")
    state.gprint("You see the campus and feel the breeze off Lake Superior.")
    locations['dorm']['actions'].update(jump_out_window= jump_out)

def jump_out(state: GameState):
    print("--------------------")
    state.gprint("You fall to your death. What were you thinking?")
    state.location = "game_over"

def class_mate(state: GameState):
    print("--------------------")
    state.gprint("Classmate: Hey! You're finally here. We have a lot of work to do to steal the exam.\n")
    state.gprint("Classmate: Buck's office is somewhere in heller or life science. Also his door is guarded by a dog and chains. There's talk about an old student of bucks hanging out somewhere in Voss Kovach or the engineering building he might have something we need.\n")
    state.gprint("Classmate: Go find and talk to them and try to get the exam before it's too late.")
    del locations['venden']['specialDesc']["desc"]
    del locations['venden']['actions']['talk']

locations = {
    "dorm": {
        "initialDescription": "You are standing in your dorm. Your roommate, Brad, is watching TV on his bed. In your room there is a door, a window, and your desk.",
        "description": "Your roomate Brad is watching TV. There is a window, a door, and a desk.",
        "specialDesc": {"desc": "A note on your desk reminds you to meet a classmate in the venden"},
        "exits": {"exit": "dormhall"},
        "actions": {
            "open window": open_window,
            "talk": room_mate
        }
    },
    "dormhall": {
        "initialDescription": "***",
        "description": "You've made your way to the main dorm hallway. You see a sign for the LSH office to the north.",
        "exits": {"north": "LSHdesk", "enter": "dorm"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"},
        "items": {"ucard": {"name": "ucard", "description": "You see a <Ucard> laying face down on the floor"}}
    },
    "LSHdesk": {
        "initialDescription": "***",
        "description": "You are in front of the LSH office. A long hallway leads south towards Ianni. A sign points east for the main campus and dining center.",
        "exits": {"south": "dormhall", "east": "diningcenter"},
        "actions": {"open door": "Nope",
                   "backpack": "**BACKPACK COMPONENTS**"}
    },
    "diningcenter": {
        "initialDescription": "***",
        "description": "You stop a moment to look inside the dining center. The food looks like it is suitable for a dog.",
        "exits": {"west": "LSHdesk", "east": "kirby3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"},
        "items": {"chicken wing": {"name": "chicken wing", "description": "Laying near the entrance you see a discarded <chicken wing>"}}
    },
    "kirby3": {
        "initialDescription": "***",
        "description": "You are at the top of a large and busy stairwell. To your north and south are two sets of doors.",
        "exits": {"north": "rafters", "south": "kirbyBall", "west": "diningcenter", "down": "kirby2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "rafters": {
        "initialDescription": "***",
        "description": "You enter a bare white room with some tables. There are some doors on the north side.",
        "exits": {"south": "kirby3", "north": "kirbybalcony"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "kirbybalcony": {
        "initialDescription": "***",
        "description": "You stand on a balcony overlooking a main entrance to the school with many old chairs around. There is a white hall to the north and stairs that lead down.",
        "exits": {"south": "rafters", "down": "kirbyplaza2", "north": "kirbyplaza3"},
    },
    "kirbyBall": {
        "intialDescription": "***",
        "description": "Large room with pillars and wooden floor",
        "exits": {"north": "kirby3", "south": "kirbystaircase3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "kirbystaircase3": {
        "initialDescription": "***",
        "description": "You are at the top of a stairwell that only goes down. To the north lays the ballroom.",
        "exits": {"north": "kirbyBall", "down": "kirbystaircase2"},
    },
    "kirbystaircase2": {
        "initialDescription": "***",
        "description": "Stairs lead up and down. North of you is the Multiculural Center",
        "exits": {"down": "kirbysc", "up": "kirbystaircase3", "north": "multicultural"},
    },
    "kirby2": {
        "initialDescription": "***",
        "description": "You are halfway down the stairs. To the south is the Multicultural Center and Offices of Diversity. To the north, you spot the school store and a food court.",
        "exits": {"north": "kirbyplaza2", "south": "multicultural", "up": "kirby3", "down": "kirbydesk"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "multicultural":{
        "initialDescription": "***",
        "description": "You enter almost a lounge area with several sections to it. To the north and south lay sets of doors.",
        "exits": {"north": "kirby2", "south": "kirbystaircase2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "kirbydesk": {
        "initialDescription": "***",
        "description": "You are at the bottom of a large stairwell in front of the kirby help desk. You see hallways leading in three directions.",
        "exits": {"north": "kirbyplaza1", "south": "kirbysc", "up": "kirby2",  "down": "soloncc"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "kirbysc": {
        "initialDescription": "***",
        "description": "You stand admidst what must be the busiest hall on campus. To your north there is the student desk. Theres another stairwell going up here with more stairs leading down near one end of the hall. South of you lay another hall.",
        "specialDesc": {"desc": "You see your classmate sitting at a booth table with several pieces of paper layed before him."},
        "exits": {"north": "kirbydesk", "south": "heller1", "down": "underground", "up": "kirbystaircase2"}
    },
    "underground": {
        "initialDescription": "***",
        "description": "Entering into the underground you notice the low ceilings and what seems like an 80's themed bowling alley.",
        "exits": {"up": "kirbysc", "east": "soloncc"},
        "specialDesc": {"desc": "Standing around a pool table there are three so called frat guy's."},
        "actions": {"talk": frat_guys}
    },
    "kirbyplaza1": {
        "initialDescription": "***",
        "description": "You stand in between the lower store and Northern Shores coffee shop. Hallways lead north, south, and east with a staircase going up.",
        "exits": {"south": "kirbydesk", "north": "techcenter","east": "cinahall1","up": "kirbyplaza2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
     "kirbyplaza2": {
        "initialDescription": "***",
        "description": "You are standing outside of the upper UMD store. To your north is the food court and to the south is kirby floor 2.",
        "exits": {"down": "kirbyplaza1", "south": "kirby2", "north": "foodcourt", "up": "kirbybalcony"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "foodcourt": {
        "initialDescription": "***",
        "description": "Around you seems to be food that is more fitting than that from the DC. There are two exits one to the north and south.",
        "exits": {"down": "techcenter", "south": "kirbyplaza2", "up": "kirbyplaza3", "north": "northoffc"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "northoffc": {
        "initialDescription": "***",
        "description": "The food court lies south. There's a staircase and a hall leading east.",
        "exits": {"south": "foodcourt", "east": "bohannon2", "up": "kirbyplaza3"}
    },
    "kirbyplaza3": {
        "initialDescription": "***",
        "description": "You're in a all white hallway that seems almost hospital like. Hallways lead south and east with stairs leading down.",
        "exits": {"down": "northoffc", "east": "bohannon3", "south": "kirbybalcony"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "techcenter": {
        "initialDescription": "***",
        "description": "Around you theres several benches with tables. The hallway goes south and north. Another hall is to your east.",
        "exits": {"south": "kirbyplaza1", "north": "thegrind", "east": "bohannon1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "thegrind": {
        "initialDescription": "***",
        "description": "Standing in front of a small shop you see halls leading in all directions.",
        "exits": {"south": "techcenter", "north": "outsidekathrynalib", "west": "labovitzfl1", "east": "montague1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "heller1": {
        "initialDescription": "***",
        "description": "The hallway continues to run north-south. There is a stairwell that takes you to the second floor of Heller Hall.",
        "exits": {"north": "kirbysc", "south": "lifescience1", "up": "heller2"},
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
        "description": {"desc": heller3},
        "exits": {"down": "heller2", "enter": "drbucks_office_locked", "south": "lifescience3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**",
                    "acid": unlock_bucks_acid,
                    "chicken": unlock_bucks_chicken}
    },
    "drbucks_office_locked": {
        "description": "As you approach the door the vicous dog stands and starts to growl",
        "exits": {"exit": "heller3"},
        "actions": {
            "acid": unlock_bucks_acid,
            "chicken": unlock_bucks_chicken
        }
    },
    "drbucks_locked_chain": {
        "description": "Trying the door it still is securely shut with chains. Find something to break or melt the chains.",
        "exits": {"exit": "heller3"},
        "actions": {"acid": unlock_bucks_acid}
    },
    "drbucks_locked_dog": {
        "description": "You approach the door but the dog still stands in your way. Find something to distract it",
        "exits": {"exit": "heller3"},
        "actions": {"chicken": unlock_bucks_chicken}
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
        "specialDesc": {"desc": "The lab seems important. There might be something in there."},
        "exits": {"down": "chemistry3", "enter": "lockedchem"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**",
                    "use_ckey": unlock_chem_lab}
    },
    "lockedchem": {
        "description": "Standing in the entrance of the lab you try the door but it's locked. A Chemistry Key is needed to unlock the door.",
        "exits": {"exit": "chemistry4"},
        "actions": {"use_ckey": unlock_chem_lab}
    },
    "chemistrylab": {
        "initialDescription": "***",
        "description": "The lights flicker as you enter the room. Around you there are several tables littered with objects you don't recognize.",
        "exits": {"exit": "chemistry4"},
        "items": {"beaker of acid": {"name": "beaker of acid", "description": "Across the room you see what youve come for. The bright green liquid swirling around. A beaker of acid."}}
    },
    "soloncc": {    #will need to make a "special_room", needs wedge and missing 4-5 exits.
        "initialDescription": "***",
        "description": "A hallway leads north, and another leads east. Students study intently.",
        "specialDesc": {"desc": "In one of the hallways you see an interesting door with a keypad..."},
        "exits": {"north": "cinahallgr", "east": "darlandadmin", "up": "kirbydesk", "south": "chemistry1", "west": "underground"},
        "actions": {}
    },
    "darlandadmin": {
        "initialDescription": "***",
        "description": "Trying the doors of the administration you notice them tightly locked. You can go no further.",
        "exits": {"back": "soloncc"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "cinahallgr": {
        "initialDescription": "***",
        "description": "This hallway feels darker than the rest. Doors advertise photography classes.",
        "exits": {"south": "soloncc", "up": "cinahall1", "north": "tweedmus"},
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
    "tweedmus": {
        "initialDescription": "***",
        "description": "Standing outside a museum of art inside the campus you see halls running north and south along with one to your east.",
        "exits": {"south": "cinahallgr", "north": "bohannongr", "east": "humanities2"}
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
        "exits": {"west": "tweedmus", "south": "abanderson2", "east": "webermusic2", "down": "humanities1", "up": "humanities3"},
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
        "description": "Standing in a lobby of a sports arena you see doors are closed and locked except to the south",
        "exits": {"south": "webermusic2"},
        "actions": {}
    },
    "rsop": {
      "initialDescription": "***",
      "description": "There are many tunnels down here but nothing seems important. Head south or up.",
      "exits": {"up": "rsop1", "south": "webermusic1"}  
    },
    "bohannongr": {
        "initialDescription": "***",
        "description": "You notice Bohannon 90, a massive lecture hall. A hallway runs west to Ven Den and also runs north and south.",
        "exits": {"south": "tweedmus", "north": "montaguegr", "west": "venden", "up": "bohannon1"},
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
        "description": "The school seems to be full of classrooms, and to the west brings you north of the food court.",
        "exits": {"west": "northoffc", "down": "bohannon1", "up": "bohannon3"},
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
        "description": "Engineering labs line the halls, showcasing senior projects. A tunnel leads underneath to the library.",
        "specialDesc": "You overhear a group of students say <Wow the test average was really high this time. It was a wopping 57!!>",
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
        "description": "The bottom floor of Voss is tightly sealed. Stairs lead back up but you think you see something in the shadows.",
        "exits": {"up": "vosskovach1"},
        "specialDesc": {"desc": "In the corner you see an older student crouched and seems to be crying"},
        "actions": {"talk": grad_student}
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
        "specialDesc": {},
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
        "description": "You enter the venden students are sitting at the several tables around the room.",
        "specialDesc": {"desc": "You see your classmate sitting in one corner of the room."},
        "exits": {"east": "bohannongr", "up": "bohannon1"},
        "actions": {"talk": class_mate}
    },
    "marshallpacfl1": {
        "initialDescription": "***",
        "description": "You can tell the space you are in is intended for public viewing. It is clean and contains unique art. To the west is a hallway that leads to Montague Hall. Stairs lead up to access the upper level of the performance hall, but the doors are shut. Stairs also lead to the basement. A hallway takes you east to the engineering building.",
        "exits": {"west": "montagueflgr", "down": "marshallpacbs", "up": "marshallpacfl2"},
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
        "actions": {"fight": blackJack}
    },
    "drbuck_confrontation": {
        "initialDescription": "***",
        "description": "See boss fight confrontation.",
        "exits": {},
        "actions": {"bribe": "If over 100 dollars you win else game over", "other": "game over"}
    },
    "offcampus": {
        "initialDescription": "***",
        "description": "You arrive off campus at an old rundown house. You can hear music playing. Your friend invites you in.",
        "exits": {"enter": "in_the_house", "back": "dormhall"},
        "actions": {}
    },
    "in_the_house": {
        "initialDescription": "***",
        "description": "You step inside the front door and are handed a beverage you have never even heard of. People are talking all around you. You walk over a rug and are unsure what the original color is.",
        "exits": {"exit": "offcampus"},
        "actions": {}
    },
    "pit": {
        "initialDescription": "***",
        "description": "Your friends take you to a location called the pit. You are a bit woozy already and are unsure if you should keep going.",
        "exits": {"forward": "game_over", "backward": "in_the_house"},
        "actions": {}
    },
    "secret_basement": {
        "initialDescription": "***",
        "description": "You move the rug and go through a trap door and find a group of seniors running an underground roulette table.",
        "exits": {"gamble": "Play roulette", "leave": "in_the_house"},
        "actions": {}
    },
    "planetarium": {
        "initialDescription": "***",
        "description": "You enter the planetarium to see a strange machine in the center of a circular room. The only other thing you see is old squeaky chairs.",
        "exits": {"exit": "MWAHgr"},
        "actions": {}
    },
    "math_office": {
        "initialDescription": "***",
        "description": "You enter a small room with desk littered with papers.",
        "exits": {"exit": "soloncc"},
        "items": {"exam key": {"name": "exam key", "description": "Peeking out from underneath a pile of other papers you see the big red letters <EXAM KEY>"}}
    },
    "game_over": {
        "description": ""
    }
} 


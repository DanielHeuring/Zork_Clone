# Challenge 5

import turtle
import sys
from random import choice
from venv import create

screen = turtle.Screen()
screen.title("Name of Turtle Design Here")
screen.setup(width=800, height=800)

t = turtle.Turtle()

t.speed(0)

locations = {
    "dorm": {
        "initialDescription": "You are standing in your dorm. Your roommate, Brad, is watching TV on his bed. In your room there is a door, a window, and your desk.",
        "description": "DORM\nBrad is still watching TV. There is a window, a door, and a desk.",
        "type": "reg_room",
        "exits": {"east": "dormhall"},
        "actions": {
            "open window": "You see the campus and feel the breeze off Lake Superior.",
            "jump out window": "You fall to your death. What were you thinking?",
            "backpack": "**BACKPACK COMPONENTS**"
        }
    },
    "dormhall": {
        "initialDescription": "***",
        "description": "You've made your way to the main dorm hallway. You see a sign for the LSH office to the north.",
        "type": "hall",
        "exits": {"north": "LSHdesk", "west": "dorm", "south": "offcampus"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "LSHdesk": {
        "initialDescription": "***",
        "description": "You are in front of the LSH office",
        "type": "reg_room",
        "exits": {"south": "dormhall", "east": "diningcenter"},
        "actions": {"open door": "The door is locked.",
                   "backpack": "**BACKPACK COMPONENTS**"}
    },
    "superiorhall": {
        "initialDescription": "***",
        "description": "***",
        "type": "hall",
        "exits": {"west": "LSHdesk", "south": "kirbyballroom"},
        "actions": {}
    },
    "kirbyballroom": {
        "initialDescription": "***",
        "description": "***",
        "type": "reg_room",
        "exits": {"north": "superiorhall", "east": "diningcenter"},
        "actions": {}
    }
}


def create_room(roomID):

    location_entry = locations[f"{roomID}"]["exits"]
    type = locations[f"{roomID}"]["type"]

    roomID = roomID.upper()

    def turtle_exit():
        t.left(90)
        t.forward(25)
        t.right(90)
        t.penup()
        t.forward(100)
        t.right(90)
        t.pendown()
        t.forward(25)
        t.left(90)

    def turtle_halls():
        t.forward(300)
        t.right(90)
        t.penup()
        t.forward(100)
        t.right(90)
        t.pendown()
        t.forward(300)
        t.left(90)

    exit_east = False
    exit_west = False
    exit_north = False
    exit_south = False

    if "north" in location_entry:
        exit_north = True
    else:
        pass
    if "south" in location_entry:
        exit_south = True
    else:
        pass
    if "east" in location_entry:
        exit_east = True
    else:
        pass
    if "west" in location_entry:
        exit_west = True
    else:
        pass

    # Displays Room Name
    t.teleport(-240, 275)
    t.write(f"{roomID}", False, "left", font=("Monospace", 14, 'normal'))

    # GENERATES "REGULAR" ROOMS
    if type == "reg_room":
        t.teleport(250, 250)
        t.right(90)
        t.forward(200)
        if exit_east == True:
            turtle_exit()
        else:
            t.forward(100)
        t.forward(200)
        t.right(90)
        t.forward(200)
        if exit_south == True:
            turtle_exit()
        else:
            t.forward(100)
        t.forward(200)
        t.right(90)
        t.forward(200)
        if exit_west == True:
            turtle_exit()
        else:
            t.forward(100)
        t.forward(200)
        t.right(90)
        t.forward(200)
        if exit_north == True:
            turtle_exit()
        else:
            t.forward(100)
        t.forward(200)
        t.right(90)

    # GENERATES HALLS
    elif type == "hall":
        t.teleport(50, 50)
        if exit_east == True:
            turtle_halls()
        else:
            t.right(90)
            t.forward(100)
        if exit_south == True:
            turtle_halls()
        else:
            t.right(90)
            t.forward(100)
        if exit_west == True:
            turtle_halls()
        else:
            t.right(90)
            t.forward(100)
        if exit_north == True:
            turtle_halls()
        else:
            t.right(90)
            t.forward(100)

    turtle.done()

def five_dorm():
    def five_dorm_menu():
        while True:
            choice = input("Select what you would like to do\n1. Go EAST\n2. INPUT ACTION\n3. Exit Menu")
            if choice == "1":
                five_dormhall()
            elif choice == "2":
                pass
            elif choice == "3":
                break

    def five_dorm_description():
        print("You are standing in your dorm. Your roommate, Brad, is watching TV on his bed. In your room there is a door, a window, and your desk.")

    def five_dorm_floorplan():
        create_room("dorm")
    while True:
        choice = input("DORM - (menu, description, floorplan)\n>>")
        if choice == "menu" or "1":
            five_dorm_menu()
        elif choice == "description" or "2":
            five_dorm_description()
        elif choice == "floorplan" or "3":
            five_dorm_floorplan()

def five_dormhall():
    def five_dormhall_menu():
        while True:
            choice = input("Select what you would like to do\n1. Go NORTH\n2. Go SOUTH\n3. Go WEST\n4. INPUT ACTION\n5. Exit Menu")
            if choice == "1":
                five_LSHDesk()
            elif choice == "2":
                five_superiorhall()
            elif choice == "3":
                five_dorm()
            elif choice == "4":
                pass  # You can add action handling here
            elif choice == "5":
                break

    def five_dormhall_description():
        print("You've made your way to the main dorm hallway. You see a sign for the LSH office to the north.")

    def five_dormhall_floorplan():
        create_room("dormhall")

    while True:
        choice = input("DORM HALL - (menu, description, floorplan)\n>>")
        if choice == "menu" or "1":
            five_dormhall_menu()
        elif choice == "description" or "2":
            five_dormhall_description()
        elif choice == "floorplan" or "3":
            five_dormhall_floorplan()


def five_LSHDesk():
    def five_LSHDesk_menu():
        while True:
            choice = input("Select what you would like to do\n1. Go SOUTH\n2. Go EAST\n3. INPUT ACTION\n4. Exit Menu")
            if choice == "1":
                five_dormhall()
            elif choice == "2":
                five_superiorhall()
            elif choice == "3":
                pass  # Add action handling here
            elif choice == "4":
                break

    def five_LSHDesk_description():
        print("You are in front of the LSH office.")

    def five_LSHDesk_floorplan():
        create_room("LSHdesk")

    while True:
        choice = input("LSH DESK - (menu, description, floorplan)\n>>")
        if choice == "menu" or "1":
            five_LSHDesk_menu()
        elif choice == "description" or "2":
            five_LSHDesk_description()
        elif choice == "floorplan" or "3":
            five_LSHDesk_floorplan()


def five_superiorhall():
    def five_superiorhall_menu():
        while True:
            choice = input("Select what you would like to do\n1. Go WEST\n2. Go SOUTH\n3. INPUT ACTION\n4. Exit Menu")
            if choice == "1":
                five_LSHDesk()
            elif choice == "2":
                five_kirbyballroom()
            elif choice == "3":
                pass  # Add action handling here
            elif choice == "4":
                break

    def five_superiorhall_description():
        print("You are in Superior Hall.")

    def five_superiorhall_floorplan():
        create_room("superiorhall")

    while True:
        choice = input("SUPERIOR HALL - (menu, description, floorplan)\n>>")
        if choice == "menu" or "1":
            five_superiorhall_menu()
        elif choice == "description" or "2":
            five_superiorhall_description()
        elif choice == "floorplan" or "3":
            five_superiorhall_floorplan()


def five_kirbyballroom():
    def five_kirbyballroom_menu():
        while True:
            choice = input("Select what you would like to do\n1. Go NORTH\n2. INPUT ACTION\n3. Exit Menu")
            if choice == "1":
                five_superiorhall()
            elif choice == "2":
                pass
            elif choice == "3":
                break

    def five_kirbyballroom_description():
        print("You are in the Kirby Ballroom.")

    def five_kirbyballroom_floorplan():
        create_room("kirbyballroom")

    while True:
        choice = input("KIRBY BALLROOM - (menu, description, floorplan)\n>>")
        if choice == "menu" or "1":
            five_kirbyballroom_menu()
        elif choice == "description" or "2":
            five_kirbyballroom_description()
        elif choice == "floorplan" or "3":
            five_kirbyballroom_floorplan()


def challenge_5_function():
    five_dorm()

def play_game():
    challenge_5_function()

def show_instructions():
    print("###ENTER INSTRUCTIONS HERE###")

def start_menu():
    # i is used to end the while loop and close the program
    i = True
    while i:
        # Displays the users options upon opening the menu
        print("-----Bulldog Brawl Menu-----")
        print("1. Play Game")
        print("2. Instructions")
        print("3. Quit Game")
        # Prompts for user input
        menu_choice = input("\nMake A Selection (1, 2, 3): ")
        # Checks for valid inputs and runs correct function where necessary
        if menu_choice == "1":
            play_game()
        elif menu_choice == "2":
            show_instructions()
        elif menu_choice == "3":
            # Sets i to False, thus ending the while loop and completing the start_menu() function
            i = False

# initializes the start menu function upon program start
challenge_5_function()

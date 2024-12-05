from time import sleep
# This class is for functions and variables that handle the basic enviroment of the game
class GameState:
    def __init__(self):
        self.location = "dorm"
        self.prevLocation = 0
        self.backpack = []

    def gprint(self, string):
        string = string + "\n"
        for i in string:
            print(i, end='', flush=True)
            sleep(0.00001) # 0.02 for game

    def uinput(self, string):
        print("\n")
        output = (input(string)).lower().strip()
        return str(output)
    
    def changeLocation(self, new_location):
        global prevLocation, state
        prevLocation = self.location
        self.location = new_location
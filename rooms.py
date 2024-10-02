#this is not finished, I will update later - Caleb
locations = {
    "dorm": {
        "initialDescription": "You are standing in your dorm. Your roommate, Brad, is watching TV on his bed. In your room there is a door, a window, and your desk.",
        "description": "DORM\nBrad is still watching TV. There is a window, a door, and a desk.",
        "exits": {"door": "dormhall"},
        "actions": {
            "open window": "You see the campus and feel the breeze off Lake Superior.",
            "jump out window": "You fall to your death. What were you thinking?",
            "backpack": "**BACKPACK COMPONENTS**"
        }
    },
    "dormhall": {
        "initialDescription": "***",
        "description": "You've made your way to the main dorm hallway. You see a sign for the LSH office to the north.",
        "exits": {"north": "LSHdesk", "west": "dorm", "south": "offcampus"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "LSHdesk": {
        "initialDescription": "***",
        "description": "You are in front of the LSH office",
        "exits": {"south": "dormhall", "east": "diningcenter"},
        "actions": {"open door": "The door is locked.",
                   "backpack": "**BACKPACK COMPONENTS**"}
    },
    "diningcenter": {
        "initialDescription": "***",
        "description": "You stop a moment to look inside the dining center. The food looks like it is suitable for a dog.",
        "exits": {"west": "LSHdesk", "east": "kirby3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "kirby3": {
        "initialDescription": "***",
        "description": "You are at the top of a large and busy stairwell. To your north and south are two sets of doors.",
        "exits": {"north": "rafters", "south": "kirbyballroom", "west": "diningcenter"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "kirby2": {
        "initialDescription": "***",
        "description": "You are halfway down the stairs. To the south is the Office of Diversity and Inclusion. To the north, you spot the school store and a food court.",
        "exits": {"north": "foodcourt", "south": "kirbyplaza2", "west": "kirby3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "kirby1": {
        "initialDescription": "***",
        "description": "You are at the bottom of a large stairwell. You see hallways leading in all directions.",
        "exits": {"north": "kirbyplaza1", "south": "heller1", "west": "kirby2", "east": "cinahall"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "heller1": {
        "initialDescription": "***",
        "description": "The hallway continues to run north-south. There is a stairwell that takes you to the second floor of Heller Hall.",
        "exits": {"north": "kirby1", "south": "lifescience1", "west": "heller2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "heller2": {
        "initialDescription": "***",
        "description": "This hallway is of no interest to you.",
        "exits": {"north": "heller1", "south": "heller3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "heller3": {
        "initialDescription": "***",
        "description": "You are on the top floor of Heller Hall. A door with chains and a vicious dog blocks your way.",
        "exits": {"north": "heller2", "west": "thomasbuckoffice"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "lifescience1": {
        "initialDescription": "***",
        "description": "Life Science Floor 1 has large lecture halls. A hallway leads south and east.",
        "exits": {"north": "heller1", "south": "MWAH1", "east": "chemistry2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "lifesciencegr": {
        "initialDescription": "***",
        "description": "Some classrooms and offices. You faintly remember traveling to the observatory as a kid.",
        "exits": {"north": "lifescience1", "south": "MWAHgr"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "lifescience2": {
        "initialDescription": "***",
        "description": "This hallway looks like every other one on campus.",
        "exits": {"north": "heller2", "south": "lifescience1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "lifescience3": {
        "initialDescription": "***",
        "description": "The top floor of the Life Science building. A hallway breaks north and a skyway is to the west.",
        "exits": {"north": "heller3", "west": "swensonscience1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "MWAH1": {
        "initialDescription": "***",
        "description": "You are at the farthest south point on campus. A hall heads north and east.",
        "exits": {"north": "lifescience1", "east": "schoolofmedicine1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "MWAHgr": {
        "initialDescription": "***",
        "description": "You are on the ground floor of Marshall W. Alworth Hall. There is a set of stairs and a circular building you're unsure about.",
        "exits": {"north": "MWAH1", "south": "planetarium"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "MWAH2": {
        "initialDescription": "***",
        "description": "Nothing seems to interest you on this floor.",
        "exits": {"north": "MWAH1", "south": "MWAH3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "MWAH3": {
        "initialDescription": "***",
        "description": "Nothing seems to interest you on this floor.",
        "exits": {"north": "MWAH2", "south": "MWAH4"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "swensonsci1": {
        "initialDescription": "***",
        "description": "The Swenson building feels new and open, with large amounts of natural light. To the east is a skyway connecting to the Life Science building.",
        "exits": {"east": "lifescience2", "south": "swensonscigr"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "swensonscigr": {
        "initialDescription": "***",
        "description": "You are on the ground floor of Swenson Science.",
        "exits": {"north": "swensonsci1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "swensonsci2": {
        "initialDescription": "***",
        "description": "There are some labs and classrooms up here, but all the doors seem locked.",
        "exits": {"north": "swensonsci1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "chemistry1": {
        "initialDescription": "***",
        "description": "A hallway runs north to south with locked doors to the south.",
        "exits": {"north": "soloncc", "south": "chemistry2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "chemistry2": {
        "initialDescription": "***",
        "description": "The chemistry building appears very old and run down. A hallway takes you west to the Life Science building.",
        "exits": {"west": "lifescience1", "north": "chemistry1", "south": "chemistry3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "chemistry3": {
        "initialDescription": "***",
        "description": "There is some caution tape blocking the stairs on the way up.",
        "exits": {"north": "chemistry2", "south": "chemistry4"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "chemistry4": {
        "initialDescription": "***",
        "description": "This floor feels abandoned, but you notice a light on in a lab.",
        "exits": {"north": "chemistry3", "east": "chemistrylab4"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "soloncc": {
        "initialDescription": "***",
        "description": "A hallway leads north, and another leads east. Students study intently.",
        "exits": {"north": "cinahallgr", "east": "darlandadmin"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "darlandadmin": {
        "initialDescription": "***",
        "description": "The doors ahead are locked.",
        "exits": {},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "cinahallgr": {
        "initialDescription": "***",
        "description": "This hallway feels darker than the rest. Doors advertise photography classes.",
        "exits": {"north": "humanities2", "south": "soloncc"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "cinahall1": {
        "initialDescription": "***",
        "description": "You have arrived at Cina Hall. The area is bright and lively.",
        "exits": {"north": "humanities3", "west": "kirbyplaza1", "south": "cinahallgr"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "cinahall2": {
        "initialDescription": "***",
        "description": "This floor is very boring. A hall leads to Humanities, and stairs go up and down.",
        "exits": {"north": "humanities4", "south": "cinahall1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "cinahall3": {
        "initialDescription": "***",
        "description": "You have wandered to Cina Hall floor three, but there is nothing of interest here.",
        "exits": {"north": "cinahall2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "humanities1": {
        "initialDescription": "***",
        "description": "Stretching eastward is a long hallway lined with locked music practice rooms. Vacant classrooms line the other side. There are no windows, and the hallway appears abandoned.",
        "exits": {"east": "webermusic1", "south": "abanderson1", "stairs": "humanities2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "humanities2": {
        "initialDescription": "***",
        "description": "The humanities hall is mostly comprised of music classrooms and offices. Hallways lead in all directions but west.",
        "exits": {"north": "bohannongr", "west": "cinahallgr", "south": "abanderson2", "east": "webermusic2", "stairs": "humanities1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "humanities3": {
        "initialDescription": "***",
        "description": "A long, bland hallway stretches out in front of you. Stairs lead up and down, with a hallway leading south.",
        "exits": {"west": "cinahall1", "south": "abanderson3", "stairs": "humanities4"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "humanities4": {
        "initialDescription": "***",
        "description": "This building has more floors than expected. Stairs take you down to other humanities floors.",
        "exits": {"west": "cinahall2", "south": "abanderson4", "stairs": "humanities3"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "webermusic1": {
        "initialDescription": "***",
        "description": "You are on the bottom floor of Weber Music Hall. There is a closed ticket stand, and a dimly lit hallway heads west.",
        "exits": {"west": "humanities1", "north": "rsopgr", "stairs": "webermusic2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "webermusic2": {
        "initialDescription": "***",
        "description": "Weber Music Hall's performance stage is locked. A hallway extends north past Romano Gym, with stairs descending to the first floor.",
        "exits": {"north": "rsop1", "west": "humanities2", "stairs": "webermusic1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "bohannongr": {
        "initialDescription": "***",
        "description": "You notice Bohannon 90, a massive lecture hall. A hallway runs west to Ven Den and also runs north and south.",
        "exits": {"south": "humanities2", "north": "montaguegr", "west": "venden"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "bohannon1": {
        "initialDescription": "***",
        "description": "This hall bores you. Go west to Kirby Plaza. Stairs take you to other Bohannon floors.",
        "exits": {"west": "kirbyplaza1", "stairs": "bohannongr"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "bohannon2": {
        "initialDescription": "***",
        "description": "The school seems to be full of classrooms, and western exits take you to Kirby Plaza.",
        "exits": {"west": "kirbyplaza2", "stairs": "bohannon1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "bohannon3": {
        "initialDescription": "***",
        "description": "Another boring hallway. Go west to Kirby Plaza.",
        "exits": {"west": "kirbyplaza3", "stairs": "bohannon2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "montaguegr": {
        "initialDescription": "***",
        "description": "Montague Hall's ground floor has large lecture halls. A hallway runs north and south.",
        "exits": {"south": "bohannongr", "north": "edugr", "east": "marshallpac1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "montague1": {
        "initialDescription": "***",
        "description": "Lecture halls surround you, with stairs leading up and down.",
        "exits": {"west": "kirbyplaza1", "stairs": "montaguegr"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "edugr": {
        "initialDescription": "***",
        "description": "This open room has chairs that remind you of kindergarten. Classrooms line the walls.",
        "exits": {"south": "montaguegr", "north": "engineering1", "stairs": "edu1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "edu1": {
        "initialDescription": "***",
        "description": "From the upper floor, you can see down to the ground floor. Rooms line the walls.",
        "exits": {"west": "library1", "stairs": "edugr"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "engineering1": {
        "initialDescription": "***",
        "description": "Engineering labs line the halls, showcasing senior projects. A tunnel leads somewhere unknown.",
        "exits": {"south": "edugr", "north": "civileng1sec2", "east": "vosskovach1", "stairs": "engineering2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "engineering2": {
        "initialDescription": "***",
        "description": "The upper floor of the engineering building is less interesting.",
        "exits": {"east": "vosskovach2", "stairs": "engineering1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "vosskovach1": {
        "initialDescription": "***",
        "description": "You step into the hall and are greeted by a potent chemical scent.",
        "exits": {"north": "civileng1", "west": "engineering1", "stairs": "vosskovach2"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "vosskovach2": {
        "initialDescription": "***",
        "description": "Voss Kovach Floor 2, with labs, classrooms, and offices.",
        "exits": {"west": "engineering2", "stairs": "vosskovach1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "vosskovachbs": {
        "initialDescription": "***",
        "description": "The bottom floor of Voss is tightly sealed. Stairs lead back up.",
        "exits": {"stairs": "vosskovach1"},
        "actions": {"backpack": "**BACKPACK COMPONENTS**"}
    },
    "civilengfl1sec1": {
        "initialDescription": "***",
        "description": "You walk into a hallway containing numerous mechanical workshops. The hallway continues west, and stairs go up. A different building lies South of you.",
        "exits": {"south": "vosskovach1", "stairs": "civilengfl2", "west": "civilengfl1sec2"},
        "actions": {}
    },
    "civilengfl1sec2": {
        "initialDescription": "***",
        "description": "You are in the western section of the civil engineering building. This area houses lots of locked classrooms. The building continues east, to the south is the engineering building and stairs take you to the upper floor.",
        "exits": {"east": "civilengfl1sec1", "south": "engineeringfl1", "stairs": "civilengfl2"},
        "actions": {}
    },
    "civilengfl2": {
        "initialDescription": "***",
        "description": "There is an overlook of a couple of shops up here but they all seem empty. The rooms up here also appear unused. Stairs take you back to the first floor of the civil engineering building.",
        "exits": {"stairs": "civilengfl1sec1"},
        "actions": {}
    },
    "labovitzfl1": {
        "initialDescription": "***",
        "description": "You are wowed by the architecture of this building. Natural light floods in. Stairs lead to upper floors, and a hallway leads east.",
        "exits": {"east": "kirbyplazafl1", "stairs": "labovitzfl2"},
        "actions": {}
    },
    "labovitzfl2": {
        "initialDescription": "***",
        "description": "The middle floor is nice but only has classrooms. Stairs go up and down.",
        "exits": {"stairs": ["labovitzfl1", "labovitzfl3"]},
        "actions": {}
    },
    "labovitzfl3": {
        "initialDescription": "***",
        "description": "The upper floor is even better than the bottom two. But nothing but the views and the architecture are interesting. Stairs go down.",
        "exits": {"stairs": "labovitzfl2"},
        "actions": {}
    },
    "outsidekathrynalib": {
        "initialDescription": "***",
        "description": "You are outside the entrance to the library. A unique staircase leads to the engineering building. To the south is Kirby Plaza.",
        "exits": {"south": "kirbyplazafl1", "stairs": "engineeringfl1", "enter": "kathrynafl1"},
        "actions": {}
    },
    "kathrynafl1": {
        "initialDescription": "***",
        "description": "You have reached the main floor of the library. There are not a lot of books on this floor, but there are plenty of places to study. You hear people talking on this floor, so it must be a conversation floor. Stairs lead up 3 more floors.",
        "exits": {"leave": "outsidekathrynalib", "stairs": "kathrynafl2"},
        "actions": {}
    },
    "kathrynafl2": {
        "initialDescription": "***",
        "description": "The second floor of the library still does not have many books and is more geared towards studying. A staircase leads up and down. This floor is much quieter than the other floors. To the south is the annex of the library.",
        "exits": {"stairs": ["kathrynafl1", "kathrynafl3"], "south": "libraryannexfl2"},
        "actions": {}
    },
    "kathrynafl3": {
        "initialDescription": "***",
        "description": "You find your way to the third floor of the library and see large amounts of books and quiet study areas. Stairs continue up and down. Your legs feel weak because of all the stairs you have done.",
        "exits": {"stairs": ["kathrynafl2", "kathrynafl4"]},
        "actions": {}
    },
    "kathrynafl4": {
        "initialDescription": "***",
        "description": "The upper floor of the library has the most books and countless spots to study on your own. Your only option to leave is go back down all the steps you climbed up to get here.",
        "exits": {"stairs": "kathrynafl3"},
        "actions": {}
    },
    "libraryannexfl2": {
        "initialDescription": "***",
        "description": "You are in the library annex. You're confused by the purpose of this room besides housing books. Why isn't this called the library? You are super confused. Stairs lead down, and the library is to the north.",
        "exits": {"north": "kathrynafl2", "stairs": "libraryannexfl1"},
        "actions": {}
    },
    "libraryannexfl1": {
        "initialDescription": "***",
        "description": "You are in the first floor of the library annex. Stairs lead back up.",
        "exits": {"stairs": "libraryannexfl2"},
        "actions": {}
    },
    "medicinehallfl1": {
        "initialDescription": "***",
        "description": "How did you get in here? The doors were supposed to be locked. The School of Medicine is very posh and well-kept. To the north is the disgusting chemistry building, and to the south is MWAH. Stairs take you up and down but remember you are not supposed to be here.",
        "exits": {"north": "chemistryfl2", "south": "mwahfl1", "stairs": ["medicinehallflgr", "medicinehallfl2"]},
        "actions": {}
    },
    "medicinehallflgr": {
        "initialDescription": "***",
        "description": "Down here is nice and tidy compared to every other basement in the school. You should really be going now. Take the stairs up, it is your only option.",
        "exits": {"stairs": "medicinehallfl1"},
        "actions": {}
    },
    "medicinehallfl2": {
        "initialDescription": "***",
        "description": "This floor is just like the main floor. You should really be going—you are going to get caught. Take the stairs down. They may also go up.",
        "exits": {"stairs": ["medicinehallfl1", "medicinehallfl3"]},
        "actions": {}
    },
    "medicinehallfl3": {
        "initialDescription": "***",
        "description": "Why waste your time coming to the top floor that is the same as the floors below it? GO BACK DOWN!",
        "exits": {"stairs": "medicinehallfl2"},
        "actions": {}
    },
    "venden": {
        "initialDescription": "***",
        "description": "The lights turn on when you enter the room. It’s just a simple lounge area. You notice a microwave that might be useful later.",
        "exits": {"east": "bohannonflgr"},
        "actions": {}
    },
    "marshallpacfl1": {
        "initialDescription": "***",
        "description": "You can tell the space you are in is intended for public viewing. It is clean and contains unique art. To the west is a hallway that leads to Montague Hall. Stairs lead up to access the upper level of the performance hall, but the doors are shut. Stairs also lead to the basement. A hallway takes you east to the engineering building.",
        "exits": {"west": "montagueflgr", "stairs": ["marshallpacbs", "marshallpacfl2"], "east": "engineeringfl1"},
        "actions": {}
    },
    "marshallpacfl2": {
        "initialDescription": "***",
        "description": "You are on the balcony of the performing arts center. Nothing up here seems open. Stairs lead back down.",
        "exits": {"stairs": "marshallpacfl1"},
        "actions": {}
    },
    "marshallpacbs": {
        "initialDescription": "***",
        "description": "This room is very creepy. You hear something creaking in the room, but you cannot see it because the lights are off. You get creeped out and think it is best to go back up the stairs.",
        "exits": {"stairs": "marshallpacfl1"},
        "actions": {}
    },
    "abandersonfl1": {
        "initialDescription": "***",
        "description": "This building is shaped like a rectangle with pottery classes around the outside. In fact, you see some students making pots right now. You look for stairs but see none. To leave, you must go north.",
        "exits": {"north": "humanitiesfl1", "stairs": "abandersonfl2"},
        "actions": {}
    },
    "abandersonfl2": {
        "initialDescription": "***",
        "description": "You notice this building is just one big square hallway with empty classrooms. Stairs lead up but not down, oddly. Humanities is to the north.",
        "exits": {"north": "humanitiesfl2", "stairs": ["abandersonfl1", "abandersonfl3"]},
        "actions": {}
    },
    "abandersonfl3": {
        "initialDescription": "***",
        "description": "This floor serves no purpose to you. Go north or take the stairs up or down to leave.",
        "exits": {"north": "humanitiesfl3", "stairs": ["abandersonfl2", "abandersonfl4"]},
        "actions": {}
    },
    "abandersonfl4": {
        "initialDescription": "***",
        "description": "This floor serves no purpose to you. Go north or take the stairs down to leave.",
        "exits": {"north": "humanitiesfl4", "stairs": "abandersonfl3"},
        "actions": {}
    },
    "drbucks_office": {
        "initialDescription": "***",
        "description": "You have managed to break into Dr. Buck's office. His desk is riddled with papers. You notice a bottle on the desk labeled 'Tears of Previous Students'. Your body shakes as your nerves increase. You finally find what you are looking for, a briefcase labeled 'Final Exam'. You open it up and find the answer key. Just as you are about to leave, Dr. Buck enters the room.",
        "exits": {},
        "actions": {}
    },
    "drbuck_confrontation": {
        "initialDescription": "***",
        "description": "See boss fight confrontation.",
        "exits": {},
        "actions": {"bribe": "If over 100 dollars you win else game over", "other": "game over"}
    },
    "invite_required": {
        "initialDescription": "***",
        "description": "You arrive off campus at an old rundown house. You can hear music playing. Your friend invites you in.",
        "exits": {"forward": "in_the_house", "backward": "dorm_hallway"},
        "actions": {}
    },
    "in_the_house": {
        "initialDescription": "***",
        "description": "You step inside the front door and are handed a beverage you have never even heard of. People are talking all around you. You walk over a rug and are unsure what the original color is.",
        "exits": {"forward": "pit", "backward": "outside", "rug": "secret_basement"},
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
    }
}
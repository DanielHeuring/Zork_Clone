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
    }
})

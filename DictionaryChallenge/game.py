# modify exits to be a dict instead of a list with keys as numbers of the locations, values being
# dictionaries holding the exits.  no change should be needed to the actual code


locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of the hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in a forest"}
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

namedExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
              2: {"5": 5},
              3: {"1": 1},
              4: {"1": 1, "2": 2,},
              5: {"2": 2, "1": 1}}

compass = {"WEST": "W",
           "EAST": "E",
           "SOUTH": "S",
           "NORTH": "N",
           "QUIT": "Q",
           "ROAD": "1",
           "HILL": "2",
           "BUILDING": "3",
           "VALLEY": "4",
           "FOREST": "5" }

# print(locations[0].split())
# print(locations[3].split(","))
# print(' '.join(locations[0].split()))

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])

    direction = input("available exits are " + availableExits).upper()
    print()
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in compass:
                direction = compass[word]
                break
    if direction in allExits:
        loc = allExits[direction]
    else:
        print("can't go in that direction")

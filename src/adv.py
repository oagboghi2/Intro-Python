
import time
import textwrap

# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.

rooms = {
    "outside": {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mouth beckons.",
        "n_to": "foyer",
    },

    "foyer": {
        "name": "Foyer",
        "description": "Dim light filters in from the south. Dusty passages run north and east.",
        "n_to": "overlook",
        "s_to": "outside",
        "e_to": "narrow",
    },

    "overlook": {
        "name": "Grand Overlook",
        "description": """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        "s_to": "foyer",
    },

    "narrow": {
        "name": "Narrow Passage",
        "description": "The narrow passage bends here from west to north. The smell of gold permeates the air.", 
        "w_to": "foyer",
        "n_to": "treasure",
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure
chamber. Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        "s_to": "narrow",
    },

}

""" template room to copy into code
    "room": {
        "name": "",
        "description": "",
        "n_to": "",
        "s_to": "",
        "e_to": "",
        "w_to": "",
    },
"""

# print("testing")
# time.sleep(2) #sleep for 2 second
# print("test finished")

# Write a class to hold player information, e.g. what room they are in currently

class Player:
    def __init__(self, startRoom):
        self.curRoom = startRoom

def choosePath(d, curRoom):
    path = d + "_to"
    if path not in rooms[curRoom]:
        print("You can't go that way")
        return curRoom

    dest = rooms[curRoom][path]

    return dest

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p = Player('outside')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

done = False

while not done:
    # Print the room name
    print("\n{}\n".format(rooms[p.curRoom]['name']))

    # Print the room description
    for line in textwrap.wrap(rooms[p.curRoom]['description']):
        print(line)

    # User prompt
    s = input("\nCommand> ").strip().lower()

    # Handle input
    if s == "q":
        done = True
    elif s in ["n", "s", "w", "e"]:
        p.curRoom = choosePath(s, p.curRoom)
    else:
        print("Unknown command {}".format(s))
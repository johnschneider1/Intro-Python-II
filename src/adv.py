from room import Room
from player import Player
import textwrap
from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'Thunderfury': Item('Thunderfury', 'The blessed blade hums and shines in the dull light'),
    'QuelSerrar': Item('QuelSerrar', 'The beautiful weapon appears to be crafted by artisans long since departed'),
    'Ashkandi': Item('Ashkandi', 'One of the most powerful swrods sits idly on the ground'),
    'DarkEdgeofInsanity': Item('DarkEdgeofInsanity', 'Cthun weeps!!!'),
    'CorruptedAshbringer': Item('CorruptedAshbringer', 'A weapon designed for a holy Paladin sits before you')
}
# print(item['Thunderfury'].description)

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# add items to rooms
room["outside"].item = [item['Thunderfury']]
room["foyer"].item = [item['QuelSerrar']]
room["overlook"].item = [item['Ashkandi']]
room["narrow"].item = [item['DarkEdgeofInsanity']]
room["treasure"].item = [item['CorruptedAshbringer']]

# #
# Main
#

# Make a new player object that is currently in the 'outside' room.
user_name = input("Join the fight against the Horde, enter your name: ")
player = Player(user_name, room['outside'])
# room = Room()

print("player test:", player)

# REPL should accept 'r', 'p', 's' commands
# 'q' to quit

choices = ['n', 'e', 's', 'w']
# Write a loop that:
while True:

    cmd = input(f"choose your Path -> ").split(' ')
    # new_cmd = cmd.capitalize()

    print(f"You Have Chosen to {cmd} ")

    if cmd[0] == 'n':
        if player.current_location.n_to != None:
            player.current_location = player.current_location.n_to
        else:
            print(f"The Horde is blocking your route North turn back.")
        # print(f"You Gentley Step North")
    elif cmd[0] == 'e':
        if player.current_location.e_to != None:
            player.current_location = player.current_location.e_to
        else:
            print(f"The Horde is blocking your route East turn back.")
        # print(f"You Silently Slide East")
    elif cmd[0] == 's':
        if player.current_location.s_to != None:
            player.current_location = player.current_location.s_to
        else:
            print(f"The Horde is blocking your route South turn back.")
        # print(f"You Cautiously Move South")
    elif cmd[0] == 'w':
        if player.current_location.w_to != None:
            player.current_location = player.current_location.w_to
        else:
            print(f"The Horde is blocking your route West turn back.")
        # print(f"You Sneak to the West")
    elif cmd[0] == 'look':
        for item in player.current_location.item:
            print(f" your eyes do not fail you, and you notice the {item}")
        # if player.current_location.item != None
        # print(f"you are looking around and see")
        # else:
        #     print(f"you look around and see nothing")

    elif cmd[0] == 'take':
        try:
            player.collect_item(cmd[1])
        except:
            print(f"please enter an item to take ")
    elif cmd[0] == 'drop':
        try:
            player.drop_item(cmd[1])
        except:
            print(f"please select an item to drop ")

    elif cmd[0] == "inv":
        if len(player.items) > 0:
            for item in player.items:
                print(f" You are currently holding {item}")
        else:
            print("You're backpack is empty")

    elif cmd[0] == 'q':
        print('Goodbye!, Thanks For Playing')
        break
    else:
        print(f"invalid entry, n, e, s, w, q, look, take, drop are only valid inputs")

    # * Prints the current room name

    print(
        f"you are currently situated in the {player.current_location.name}")

    # * Prints the current description (the textwrap module might be useful here).
    print(textwrap.wrap(player.current_location.description))

    # * Waits for user input and decides what to do.
    # for item in player.current_location.item:
    #     print(f" your eyes do not fail you, and you notice the {item}")

    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
    # adding a line of text

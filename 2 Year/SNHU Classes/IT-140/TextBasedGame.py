#Ryan Blackburn


# A dictionary for the simplified dragon text game
# My dictionary includes all potential directions, as well as descriptions for the rooms and the items that belong in them
rooms = {
    'Entrance': {'South': 'Love',
                 'description': 'There is only a candle here. The room is lonely as death.'},
    'Love': {'North': 'Start', 'West': 'Childhood', 'East': 'Adventure', 'South': 'Achievement',
             'item': 'Faded Letter',
             'description': 'You feel yourself regaining emotion'},
    'Childhood': {'East': 'Love', 'South': 'Nature',
                  'item': 'Teddy Bear',
                  'description': 'You feel courage in the face of despair'},
    'Adventure': {'West': 'Love', 'South': 'Perseverance',
                  'item': 'Compass',
                  'description': 'To find your way to the end'},
    'Nature': {'North': 'Childhood', 'East': 'Achievement',
               'item': 'Flower',
               'description': 'For healing'},
    'Achievement': {'North': 'Love', 'West': 'Nature', 'East': 'Perseverance', 'South': 'Boss',
                    'item': 'Broken Pen',
                    'description': 'You feel the weight of unfinished business'},
    'Perseverance': {'North': 'Adventure', 'West': 'Achievement',
                     'item': 'Magic Sword',
                     'description': 'To defeat the Necromancer'},
    'Boss': {'North': 'Achievement',
             'description': 'You now face the Necromancer'}
}
#This creates a variable which can be used to check whether a valid move is entered
valid_move = ['North', 'South', 'East', 'West',]

#Establish the players empty inventory
inventory = []

#Define a variable for the introduction of the game, which can be reused when the game restarts
def intro():
    introduction = (
        'The Necromancer Game.\n'
        'Recover the remnants of your life to regain your body.\n'
        'Face the Necromancer once you have collected 6 items.\n'
        'Move Commands: North, East, West, South, or Exit.\n'
        "Action Commands: get 'Item Name', Status"
    )
    print(introduction)

#Create a function for moving the current state of the player from where they moved to where they are
def get_new_state(direction_from_user, current_room):
    if direction_from_user in rooms[current_room]:
        return rooms[current_room][direction_from_user]
    else:
        return current_room

#Create a new function which allows the player to see where they are and what they can do
def show_status():
    #Give the room
    print('Current Room: {}.'.format(curr_room))
    #Show the description of the room
    if 'description' in rooms[curr_room]:
        print(rooms[curr_room]['description'])
    #Let the player know which items are in the room
    if 'item' in rooms[curr_room]:
        print('Item in the room: {}'.format(rooms[curr_room]['item']))
    #Show the players current inventory
    print('Inventory: {}'.format(inventory))

    valid_room_move = [move for move in valid_move if move in rooms[curr_room]]
    print('Valid moves: {}'.format(', '.join(valid_room_move)))

#Print Introduction
intro()

#Establish the starting room room
curr_room = 'Entrance'

#Create a variable to check against for a win condition; in this game, it is having all 6 items.
total_items = 6

#First establish the gameplay loop

while True:
    #Introduce the player current room and inventory at the beginning of each round
    show_status()

    #Next accept the players move and store into a new variable
    user_move = input()

    #First check to ensure that the command entered is valid
    if user_move in valid_move:
        #This only executes if move is Valid
        #Verify that the movement selected is inside the current dictionary
        curr_room = get_new_state(user_move,curr_room)
            #Inform the player of their movement
        print(curr_room)

        # This begins the end-game loop, which must be checked immediately as soon as the player enters the Boss room
            #First set the condition which must be fully completed in order for victory
        if len(inventory) == total_items and curr_room != 'Boss':
            print("Congratulations! You have regained your soul and defeated the Necromancer!")
            break

        # If the win condition (6 items) is not met, the player will automatically lose.
        elif curr_room == 'Boss':
            print('You were not strong enough to regain your soul.')
            print('Please try again')
            break

    #If the player selects Exit, the player will move to a new room called 'exit' and prompt the Game Over dialogue
    elif user_move == 'Exit':
        rooms = 'Exit'
        print('Game Over')
    #This sequence breaks the 'room' dictionary and renders the game unable to continue play
    #However since it is contained in a loop, it will not over-write the initial dictionary.
        break

    #Check to see if the player inputs a proper command to pick up an item
    elif user_move.lower().startswith("get '") and user_move.endswith("'"):
        requested_item = user_move[5:-1]

    #Next see if the item that was requested
        #and the item that is supposed to be in the room
        #are still inside the current room. This will execute only if the Requested and Listed item are present, AND
        #If the item has not been removed.
    #If successful, the code appends the requested item to the players inventory
        if 'item' in rooms[curr_room] and requested_item.lower() == rooms[curr_room]['item'].lower():
            inventory.append(requested_item)
            print('You picked up the {}.'.format(requested_item))
        #It then removes the item from the room so that it cannot be picked up again.
            rooms[curr_room].pop('item')
        else:
            print('That item is not in this room. Try again.')

    # Finally if no form of valid input is entered, the game gives an error message and returns to start for a valid input.
    else:
        print("You can't do that")
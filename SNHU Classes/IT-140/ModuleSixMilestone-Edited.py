# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Entrance': {'South': 'Love',
                 'description': 'There is only a candle here. The room is lonely as death.'},
    'Love': {'North': 'Start', 'West': 'Childhood', 'East': 'Adventure', 'South': 'Achievement',
             'item': 'Faded Letter', 'description': 'You feel yourself regaining emotion'},
    'Childhood': {'East': 'Love', 'South': 'Nature',
                  'item': 'Teddy Bear', 'description': 'You feel courage in the face of despair'},
    'Adventure': {'West': 'Love', 'South': 'Perseverance',
                  'item': 'Compass','description': 'To find your way to the end'},
    'Nature': {'North': 'Childhood', 'East': 'Achievement',
               'item': 'Flower', 'description': 'For healing'},
    'Achievement': {'North': 'Love', 'West': 'Nature', 'East': 'Perseverance', 'South': 'Boss',
                    'item': 'Broken Pen', 'description': 'You feel the weight of unfinished business'},
    'Perseverance': {'North': 'Adventure', 'West': 'Achievement',
                     'item': 'Magic Sword', 'description': 'To defeat the Necromancer'},
    'Boss': {'North': 'Achievement', 'description': 'You now face the Necromancer'}
}
#This creates a variable which can be used to check whether a valid move is entered
valid_move = ['North', 'South', 'East', 'West',]

#Establish the players empty inventory
inventory = []

#Define a variable for the introduction of the game, which can be reused when the game restarts
def intro():
    print('The Necromancer Game.')
    print('Recover the remnants of your life to regain your body.')
    print('Face the Necromancer once you have collected 6 items')
    print('Move Commands: North, East, West, South, or Exit')
    print("Action Commands: get 'Item Name', Look Around")
#Create a list of valid moves

#Print Introduction
print(intro)
curr_room = 'Entrance'

#First establish the gameplay loop
#Loop will break and return to the top if an invalid move is made

while True:
    #Introduce the player current room and inventory at the beginning of each round
    print('Current Room: {}.'.format(curr_room))
    print('Inventory: {}'.format(inventory))

    #Show the player the flavor text for the room
    if 'description' in rooms[curr_room]:
        print(rooms[curr_room]['description'])

    #Next accept the players move and store into a new variable
    user_move = input()

    #First check to ensure that the command entered is valid
    if user_move in valid_move:
        #This only executes if move is Valid
        #Verify that the movement selected is inside the current dictionary
        if user_move in rooms[curr_room].keys():
            #Update the current room to reflect the valid move that was selected
            curr_room = rooms[curr_room][user_move]
            #Inform the player of their movement
            print(curr_room)
        #If the movement selected is not available, give an error message
        else:
            print('You cannot do that')
    # If the player can see the item, display it here.

    elif 'item' in rooms[curr_room] and user_move.lower() == "look around":
        item = rooms[curr_room]['item']
        print('There is a {} in the room.'.format(item))

    #Since 'Exit' is not listed under Valid Moves, the code will skip to here.
    #This will move the player to a new room called 'exit' and prompt the Game Over dialogue
    elif user_move == 'Exit':
        rooms = 'Exit'
        print('Game Over')
    #This sequence breaks the 'room' dictionary and renders the game unable to continue play
    #However since it is contained in a loop, it will not over-write the initialized dictionary.
        break

    #Check to see if the player properly inputs the name of an item
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
    print('Invalid input')
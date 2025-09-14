# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

#Define a variable for the introduction of the game, which can be reused when the game restarts.
intro = 'Welcome Message. Moves: North, East, West, South, or Exit'
#Create a list of valid moves

#Print Introduction
print(intro)
curr_room = 'Great Hall'

#First establish the gameplay loop
#Loop will break and return to the top if an invalid move is made

while True:
    print('Current Room: {}.'.format(curr_room))
    #Next accept the players move and store into a new variable
    user_move = input()
    if user_move in rooms[curr_room].keys():
        curr_room = rooms[curr_room][user_move]
        print(curr_room)
    else:
        #if the player enters an invalid move
        #then display an error message on the screen
        print('Invalid move!')
        # condition to check if the player exits the game
    elif user_move == 'Exit':
        print('Thanks for playing!')
    break
    # case for invalid input
    else:
        print('Invalid input')
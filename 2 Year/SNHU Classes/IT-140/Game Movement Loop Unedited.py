# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

#Define a variable for the introduction of the game, which can be reused when the game restarts.
intro = 'Welcome Message. To move, type goNorth, goEast, goWest, goSouth'

#list type variable directions
#stores the valid moves
direction_of_moves = ['goNorth', 'goSouth', 'goEast', 'goWest']
#displaying the instruction on the screen
print(intro)
current_position_room = 'Great Hall'

#loop for displaying the current position of the player
while True:
    #and condition of winning the game
    if current_position_room == 'Bedroom':
        print('Congratulations! You have reached the Bedroom and won the game!')
        break
    # displays the player's current position
    print('You are in the {}.'.format(current_position_room))

    #users input for move
    user_command_of_move = input('\nEnter the moves command to move between the rooms or exit the game: ')
    # condition for controlling the player's movement
    if user_command_of_move in direction_of_moves:
        user_command_of_move = user_command_of_move.replace("go", "")
        if user_command_of_move in rooms[current_position_room].keys():
            current_position_room = rooms[current_position_room][user_command_of_move]
            print(current_position_room)
        else:
            #if the player enters an invalid move
            #then display an error message on the screen
            print('Invalid move!')
    # condition to check if the player exits the game
    elif user_command_of_move == 'exit':
        print('Thanks for playing!')
        break
    # case for invalid input
    else:
        print('Invalid input')
#Ryan Blackburn

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}
#This creates a variable which can be used to check whether a valid move is entered
valid_move = ['North', 'South', 'East', 'West',]

#Define a variable for the introduction of the game, which can be reused when the game restarts
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
            print('Error Message')
    #Since 'Exit' is not listed under Valid Moves, the code will skip to here.
    #As long as the player enters Exit, it will move the player to a new room called 'exit' and prompt the Game Over dialogue
    elif user_move == 'Exit':
        rooms = 'Exit'
        print('Game Over')
    #This sequence breaks the 'room' dictionary and renders the game unable to continue play, even if a new direction is entered
    #However since it is contained in a loop, it will not over-write the initialized dictionary.
        break
    #Finally if no form of valid input is entered, the game gives an error message and returns to start for a valid input.
    else:
        print('Invalid input')
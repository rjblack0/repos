# Basic Printing
print("Hello World!")

#Storing Variables
msg = "Welcome to the Basics of Python!"

print(msg)

#Combining Variables
msg1 = 'We have'
msg2 = 'a lot to'
msg3 = 'learn together!'

fullMessage = f"{msg1} {msg2} {msg3}"

print(fullMessage)

#Using Lists
#Create List
myList = ['lists', 'easy!', 'Combining', 'is']
#Reorder List
list_message1 = myList[2]
list_message2 = myList[0]
list_message3 = myList[3]
list_message4 = myList[1]
#Combine in Order
list_Output = f"{list_message1} {list_message2} {list_message3} {list_message4}"

print(list_Output)

#Add to the list
myList.append('And')
myList.append('fun!')

#Construct variable directly from the list
new_Message = f"{myList[4]} {myList[5]}"

print(new_Message)

#Variable Rules

msg = "Variable will overwrite if written into again."

print(msg)

#Numerical Lists

squares = []                #Bare shell list
for x in range(1, 11):      #Will iterate from 1 to 10 inclusive.
    squares.append(x**2)    #Adds a new item and brings it up to the second power

print(squares)

#"Clean" version
##Does the same thing, but less clear for learning

squares = [x**2 for x in range(1, 16)]
print(squares)

#Getting custom user input to add to the lists:
squares = [x for x in range(1, 15)]
print(squares)

square0 = int(input("Enter a value for the first item: "))
squares[0] = square0

square4 = int(input("Enter a value for the fifth item: "))
squares[4] = square4

print(squares)


#                                   **Recalling**
(Groups a series of commands together)
[Accesses an element inside a valiable] #Accesses element inside variable
{Accesses a dictionary}
action({dictionary[element]}) #Accesses an item in a dictionary
'STRING_LITERAL' # String value specified in source code of program.

#                                   **Inputs**

name = (input)
name = input('What is your name?')
age = int(input('What is your age?'))


#                                   ****Strings****
variable = input()
variable = int(input) # This will force input to be an integer
variable = float(input) # This will force input to be a float
variable = int/or/float/or/none(input('String')) #Int, float or none are optional. String will be attached as text with the input following
\n #Newline, use with strings
variable = ' ' #Assigns variable with empty string
variable[0] #Accesses the first character of the indicated variable
var1 = var2[-1] #Assigns first variable to second LAST character of second variable.
concatenated_string = string1 + string2 # Will combine two strings, Add ' ' to put a space inbetween

#     **STRING Replace**
string = string.replace ('old', 'new') #Replaces items in a string
string.find('!') #Will return the first instance of !
string.find('!', 2) #Will find ! starting at position 2
string.find('!', 2, 4) #Will find ! between 2 and 4
string.count('!') #Returns how many times ! appears

#     **STRING CONVERSION**

#Conversion functions for some common types.
#Function	Notes	            Can convert:
#int()	    Creates integers	int, float, strings w/ integers only
#float()	Creates floats	    int, float, strings w/ integers or fractions
#str()	    Creates strings	    Any

capitalize() -- #Returns a copy of the string with the first character capitalized and the rest lowercased.
lower() -- #Returns a copy of the string with all characters lowercased.
upper() -- #Returns a copy of the string with all characters uppercased.
strip() -- #Returns a copy of the string with leading and trailing whitespace removed.
title() -- #Returns a copy of the string as a title, with first letters of words capitalized.

#     **String Space Formatting**

#Field Width
#When defining an variable
{variable = name:10} #Field will be 10 characters (Justified right)
{variable = name:<10} #Field will left justify
{variable = name:>10} #Field will right justify
{variable = name:^10} #Field will center justify
{variable = name:0^10} #Will fill all spaces that are not specified

#    **String Slicing**

string[5] #Reads character at index 5 of the string
string[start:end] #Slice notation; creates value of only those indexes
string[1:] #Yields everything after
string[:3] #Yields everything before; Can be used to generate first 3 letters of last name
string[-1]  # Accesses the last character of the string
#    **Slice Stride***
print('All numbers: {}'.format(numbers[::])) #All numbers
print('Every other number: {}'.format(numbers[::2])) #Every other number
print('Every third number between 1 and 8: {}'.format(numbers[1:9:3])) #Every 3rd number between 1 and 8

#**Example**
first_variable = Cat dog
slice_variable = first_variable[4:6]
print(slice_variable)
#yields Dog

#     **Splitting**
split() #Separates string into tokens

string = 'Music/artist/song.mp3'
my_tokens = string.split('/') #Returns my_tokens = ['Music', 'artist', 'song.mp3']

#     **Joining**
join() #Joins list of strings together into 1

web_path = [ 'www.website.com', 'profile', 'settings' ] #Take a list of strings
separator = '/' #Designate how to separate them (Separator is a variable, not a function)
url = separator.join(web_path) # separator.join means "join these with";
# (web_path) is the library of data

'variable'.join(['http://', 'www.', 'ebay', '.com']) #Empty space string
#produces the string 'http://www.ebay.com'.

#     **Examples**
path = input('Enter file name: ')
new_separator = input('Enter new separator: ')
tokens = path.split('/')
print(new_separator.join(tokens))
# The program below reads in a URL and checks whether the fourth token (index 3) is 'wiki'
#Wikipedia sample link format: http://language.wikipedia.org/wiki/topic

url = input('Enter Wikipedia URL: ')
tokens = url.split('/')
if 'wiki' != tokens[3]:
    tokens.insert(3, 'wiki')
    new_url = '/'.join(tokens)
    print('{} is not a valid address.'.format(url))
    print('Redirecting to {}'.format(new_url))
else:
    print('Loading {}'.format(url))

#                                   **Format Specification**

{:Place inside the empty brackets in string}.format
#When used inside replacement field, allows values formatting in the string to be customized.

'{:s}'.format('Aiden') #:s = String (default presentation type - can be omitted)
#Aiden
'{:d}'.format(4) #d = Decimal (integer values only)
#4
'{:b}'.format(4) #b = Binary (integer values only)
#100
'{:x}'.format(15) #x, X = Hexadecimal in lowercase (x) and uppercase (X) (integer values only)
#f
'{:e}'.format(44) #e = Exponent notation
#4.400000e+01
'{:f}'.format(4) #f = Fixed-point notation (6 places of precision)
# 4.000000
'{:.2f}'.format(4) #.[precision]f = Fixed-point notation (programmer-defined precision)
#4.00
'{:.1f}'.format(1.725) #indicates a precision of 1, thus the resulting string would be '1.7'.

#                                   ****Printing****
print(variable, 'string', )
print(end=' ') #Creates a space

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alphabet[0], alphabet[1], alphabet[25]) #Access characters as they appear in the sequence.
#Sequences start at 0.

print(f'string') #an F string allows you to embed expressions inside string literals
print(f'String contains a {dictionary[value_inside_dictionary]}')

print(len(variable) 'String') #This will print the number of characters in a variable, followed by a string

declaration = ("When in the Course of human events, it becomes necessary for "
               "one people to dissolve the political bands which have connected "
               "them with another, and to assume among the powers of the earth...")
#Will generate a single line


#     **Examples**
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
user_number = int(input('Enter number to use as index: '))
print()
print('\nLetter', user_number, 'of the alphabet is', alphabet[user_number])
#This program will return the letter of the alphabet associated with the number input.

#     **String Formatting**
print(string.format()) #The format function

print('string {what:how}) more string.'.format(what))#Creates a string with placeholders; AKA Templates
print('April {}, {}'.format(22, 2020)) #April 22, 2020
print('{0}:{1}'.format(9, 43)) #9:43

month = 'April'
day = 22
print('Today is {month} {0}'.format(day, month=month)) #Today is April 22

print('Hi {{{0}}}!'.format('Bilbo'))#A single brace is printed by using the double brace {{ }} around the replacement field {0}.

#                                   ****Lists****
#Created with [brackets], includes variables and literals
list () #Basic list function
#   list('abc') creates new list with elements ['a', 'b', 'c']

list[1] #Calls the first element in the list
list[start:end] #Calls elements in a range
mylist1 + mylist2 #Get a new list with elements from both lists

my_list[len(mylist):] = [x] #Add elements in x to the end of my_list
#Alternative Append x

empty_list = [ ]

my_nums = [5, 12, 20]
my_nums[1] = -28 #This changes the 2nd value in the list

result_of_power = math.pow(long_variable_name_left_operand,
                           long_variable_name_right_operand)
#Preferable formatting

#     **Editing lists**
object.typeofmethod #Standard method. Object should be a list.

object.append(value) #Adds value to end of list
object.extend([x]) #Add all items in x to list
object.insert(i, x) #Insert x into list BEFORE i
object.remove(x) #Remove first item from list with value x
object.pop(value) #Removes element at value position
object.remove(value) #Removes element containing the value
del my_list[i] #Delete element from list

#     **Sequence Type Methods**
list.sort() #Sort items in-place
list.reverse() #Reverse the elements of list in place
len(list) #Find the length of the list.
list1 + list2 #Produce a new list by concatenating list2 to the end of list1.
min(list) #Find the element in list with the smallest value.
max(list) #Find the element in list with the largest value.
sum(list) #Find the sum of all elements of a list (numbers only).
list.index(val) #Find the index of the first element in list whose value matches val.
list.count(val) #Count the number of occurrences of the value val in list.

#     **Quick Lists**
my_list.sort()
my_list.pop() #Sort and then remove largest element

#Sort short_names in reverse alphabetic order.
short_names = user_input.split()
short_names.sort(reverse=True)


#                                   **Tuples**
#Created by using (parentheses).
#Tuple's elements cannot be changed

#NamedTuple = Define new simple data type with named attributes

Car = namedtuple('Car', ['make','model','price','horsepower','seats'])  # Create the named tuple
chevy_blazer = Car('Chevrolet', 'Blazer', 32000, 275, 8)  # Use the named tuple to describe a car
chevy_impala = Car('Chevrolet', 'Impala', 37495, 305, 5)  # Use the named tuple to describe a different car
print(chevy_blazer)
print(chevy_impala)

#First, you inform Python that you want to create a named tuple named Car.
#Then, you define the names of the elements within the Car class (named tuple), specifying the attributes it will have.
#Once you've done this, you can use Car to create instances, and each instance will have the specified attributes, making it a convenient way to represent structured data.

#                                   ****Dictionaries****
#Created with {Brackets}
#Dictionaries are specific, versus lists which are anonymous

{key:value_pair}

dictionaryname = {'key1': Value, 'key2': Value} #This creates a dictionary with 2 keys, and their value.
empty_dictionary = { }
print()

#     **Editing Dictionaries**
dictionary_keyword['new_entry'] = 'Element' #This will add a new entry to the dictionary
dictionary_keyword['existing_entry'] = 'Element' #This will update the existing entry inside the dictionary
del dictionary_keyword['key'] #This will delete a key from a dictionary
dictionary_keyword.update({'new_entry': 'Element'})

caffeine_content_mg = {
    'Mr. Goodbar chocolate': 122,
    'Red Bull': 33,
}
print(caffeine_content_mg)

#RESULT
# {'Mr. Goodbar chocolate': 122, 'Red Bull': 33,}



#     **Examples**

#LISTS

lamborghini_veneno = 3900000  # $3.9 million!
bugatti_veyron = 2400000      # $2.4 million!
aston_martin_one77 = 1850000  # $1.85 million!

prices = [lamborghini_veneno, bugatti_veyron, aston_martin_one77]

print('Lamborghini Veneno:', prices[0], 'dollars')
print('Bugatti Veyron Super Sport:', prices[1], 'dollars')
print('Aston Martin One-77:', prices[2], 'dollars')

#TUPLES

white_house_coordinates = (38.8977, 77.0366)
print('Coordinates:', white_house_coordinates)
print('Tuple length:', len(white_house_coordinates))

# Access tuples via index
print('\nLatitude:', white_house_coordinates[0], 'north')
print('Longitude:', white_house_coordinates[1], 'west\n')

#Create a new named tuple Dog that has the attributes name, breed, and color.
Dog = namedtuple('Dog', ['name','breed','color'])

#Let Address = namedtuple('Address', ['street', 'city', 'country']).
#Create a new address object 'house' where
#house.street is "221B Baker Street",
#house.city is "London", and
#house.country is "England".

house = Address('221B Baker Street', 'London', 'England')

#Given the following named tuple Car = namedtuple('Car', ['make', 'model', 'price', 'horsepower', 'seats']),
#and data objects car1 and car2,
#write an expression that computes the sum of the price of both cars.

car1.price + car2.price

#Many documents use a specific format for a person's name. Write a program that reads a person's name in the following format:
firstName middleName lastName (in one line)

#and outputs the person's name in the following format:
lastName, firstInitial.middleInitial.

#                                   ****If / Else Statements****
if variable
else variable
elif variable
and, or, not #Boolean Operators
in, not in #Membership operators
is, is not #Identity operators
(<, <=, >, >=) #Relational operators
(==, !=) #Equality operators
a < b < c = Operator Chaining
isalnum() -- #Returns True if all characters in the string are lowercase or uppercase letters, or the numbers 0-9.
isdigit() -- #Returns True if all characters are the numbers 0-9.
islower() -- #Returns True if all cased characters are lowercase letters.
isupper() -- #Return True if all cased characters are uppercase letters.
isspace() -- #Return True if all characters are whitespace.
startswith(x) -- #Return True if the string starts with x.
endswith(x) -- #Return True if the string ends with x.
#     **ORDER OF OPERATIONS**
(Operations)        #Items in Parenthesis
(*/%+-)             #Arithmetic operators
(<,<=,>,>=,==,!=)   #Relational
not                 #Not
and                 #and
or                  #or

#     **EXAMPLES**

full_name = input()
name_parts = full_name.split()
first_name = name_parts[0]
last_name = name_parts[-1]
formatted_name = f'{last_name}, {first_name[0]}.'
if len(name_parts) == 3:
    middle_name = name_parts[1]
    formatted_name += f'{middle_name[0]}.'
print(formatted_name)

#===========

menu_prompt = ('Available commands:\n'
               '  (add) Add passenger\n'
               '  (del) Delete passenger\n'
               '  (print) Print passenger list\n'
               '  (exit) Exit the program\n'
               'Enter command:\n')

destinations = ['PHX', 'AUS', 'LAS']

destination_prompt = ('Available destinations:\n'
                      '(PHX) Phoenix\n'
                      '(AUS) Austin\n'
                      '(LAS) Las Vegas\n'
                      'Enter destination:\n')

passengers = {}

print('Welcome to Mohawk Airlines!\n')
user_input = input(menu_prompt).strip().lower()

while user_input != 'exit':
    if user_input == 'add':
        name = input('Enter passenger name:\n').strip().upper()
        destination = input(destination_prompt).strip().upper()
        if destination not in destinations:
            print('Unknown destination.\n')
        else:
            passengers[name] = destination

    elif user_input == 'del':
        name = input('Enter passenger name:\n').strip().upper()
        if name in passengers:
            del passengers[name]

    elif user_input == 'print':
        for passenger in passengers:
            print('{} --> {}'.format(passenger.title(), passengers[passenger]))
    else:
        print('Unrecognized command.')

    user_input = input('Enter command:\n').strip().lower()

#          ===== DECISION BRANCHING =====

#Standard If;Else
price = 20
age = (input('What is your age?'))
    if age > 60
        price = price - 20
print ('Cost:', price)

#Standard If;Elseif;Else Branch

year = (input)
    if year = 1984
        print ('Orwell!')
    else if year = 2001
        print ('Space Odyssey!')
    else
        print ('Nothing Special')

#Create the Absolute value
val = (input)
    if val < 0
        val = -val
    print (val)

#Find Max
x = (input)
y = (input)
    if x > y
        max = x
    else
        max = y
print (max)

#Checking for an item in a list

barcelona_fc_roster = ['Alves', 'Messi', 'Fabregas']

name = input('Enter name to check: ')

if name in barcelona_fc_roster:
    print('Found', name, 'on the roster.')
else:
    print('Could not find', name, 'on the roster.')

#Checking for Substrings

request_str = 'GET index.html HTTP/1.1'

if '/1.1' in request_str:
    print('HTTP protocol 1.1')
if 'HTTPS' not in request_str:
    print('Unsecured connection')

#Checking for membership in a string

my_dict = {'A': 1, 'B': 2, 'C': 3}

if 'B' in my_dict:
   print("Found 'B'")
else:
   print("'B' not found")

# Membership operator does not check values
if 3 in my_dict:
    print('Found 3')
else:
    print('3 not found')

#                                   ****LOOPS****
x += 1 #Returns to top and adds a value
x -= 1 #Returns to top and subtracts a value
x != '1' #Translates to 'Until'
reversed() #Will pull items from a list back to front
range(5) #Starts from 0 - 4 (Ranges are Non-inclusive)
range(2,5) #Every integer from 2-4
range(5, 0, -1) #Range counting down by 1
range(5, 0, -2) #Every second integer from 5-0

if end_condition == met
    break #Simple check to see if the loop should end

if total_cost + new_cost != 0
    continue #Tells loop to skip to the 'while' or 'for' loop header





#While vs. For Loops Rules
#  Use a for loop when the number of iterations is computable before
#   entering the loop, as when counting down from X to 0, printing a string
#   N times, etc.
#  Use a for loop when accessing the elements of a container, as when
#   adding 1 to every element in a list, or printing the key of every
#   entry in a dict, etc.
#  Use a while loop when the number of iterations is not computable
#   before entering the loop, as when iterating until a user enters a
#   particular character.

#     'For' loop generates everything in a range
for i in range(1,1001)
    print i
#Results all between 1 and 1001

#     'For' Loop accessing all elements in a container
for name in ['Bill', 'Nicole', 'John']:
    print('Hi {}!'.format(name)) #Prints 3 times with all names

#     'For' Loop assigning keys of dictionary to loop variable
channels = {
    'MTV': 35,
    'CNN': 28,
    'FOX': 11,
    'NBC': 4,
    'CBS': 12
}
for c in channels:
    print('{} is on channel {}'.format(c, channels[c]))

#     'For' Loop iterating over string
my_str = ''
for character in "Take me to the moon.":
    my_str += character + '_'
print(my_str) #T_a_k_e_ _m_e_ _t_o_ _t_h_e_ _m_o_o_n_._

#     Printing a Dictionary
contact_emails = {
    'Sue Reyn' : 's.reyn@email.com',
    'Mike Filt': 'mike.filt@bmail.com',
    'Nate Arty': 'narty042@nmail.com'
}
new_contact = input()
new_email = input()
contact_emails[new_contact] = new_email

for contact, email in contact_emails.items():
    print(f'{email} is {contact}')

#     **Nested Loops**

for i in range(5):
    for j in range(10, 12):
        print('{}{}'.format(i, j))

#     **'For' Loop, print all elements in a string**

user_input = input('Enter phone number: ')

index = 0
for character in user_input:
    print('Element {} is: {}'.format(index, character))
    index += 1



#     'While' loop executes until stop condition is met
x = 20
while x > 15:
     print(x)
     x -= 1
#This will print 20, 19, 18, 17, 15

#     Sentinel Value
increment = 0
user_value = '-'
while value != 'q' #This creates an end status decided by user input
    user_input = input ('Entering q will end sequence')
    user_value = user_input
print('This only prints once q is entered')

#     While Loop with user input

user_num = int(input())
while user_num >= 0:
  print('Body')
  user_num = int(input())

print('Done.')

#     **Counting with a While Loop**
# Iterating N times using a loop variable
i = 1
while i <= N:
    # Loop body statements go here
    i = i + 1

#     **Looping an indicated number of times**
names = ['Janice', 'Clarice', 'Martin', 'Veronica', 'Jason']
num = int(input('Enter number of names to print: '))
for i in range(len(names)):
    if i == num:
        break
    print(names[i], end= ' ')
else:
    print('All names printed.')

# Using range() and len() to iterate over a sequence.
origins = [4, 8, 10]
for index in range(len(origins)):
    value = origins[index]  # Retrieve value of element in list.
    print('Element {}: {}'.format(index, value))

#Using list.index() to find the index of each element.
origins = [4, 8, 10]
for value in origins:
    index = origins.index(value)  # Retrieve index of value in list
    print('Element {}: {}'.format(index, value))

#The enumerate() function.
origins = [4, 8, 10]
for (index, value) in enumerate(origins):
    print('Element {}: {}'.format(index, value))

#     **Data Validation**
age = -1
str_age = input(“What is your age? “)
while !str_age.isdigit(): # This loop will run if the input is NOT a digit.
     print(“You didn’t enter an integer.”)
     str_age = input(“What is your age? “)
age = int(str_age)

#     **Counting values in a list of values**

count = 0
val = (input)

While val is not 0
     If val < 0
     count = count + 1

val = (input)

#     **Find Max Value**

max = -1
val = (input)

while val is not 0
   If val > max
      max = val

   val = (input)

#                                   **Functions**
#Built in Functions:
#input, print, int, len, etc.
#Parameter: Used when defining
#Argument: Used when calling
#Variables: If assigned inside a function, its scope is restricted. If defined before, its scope extends from assignment
print(globals) #This will print all of the global variables
print(locals) #Prints the local ones. This is variables executing within a currently executing function

def function_name(): #Creating a function
    #Code goes here
function_name() #Calling a function

#     ***Optional Arguments***
#These are both standard practice keywords; however anything with * and ** will perform the same
*args #Collects optional positional parameters into an arbirary argument list
**kwargs #Creates a dictionary of "extra" arguments not defined in the function definition



#     **SIMPLE***
add() #The add function, will combine two intergers or strings
def add(x, y):
    return x + y
print('add(5, 7) is', add(5, 7))
print("add('Tora', 'Bora') is", add('Tora', 'Bora'))

print(add(5 * y)) #This will return BoraBoraBoraBoraBora

#Pizza Argument Agreement
def print_pizza_area(pizza_diameter):
    pi_val = 3.14159265
    pizza_radius = pizza_diameter / 2.0
    pizza_area = pi_val * pizza_radius * pizza_radius
    print('{:.1f} inch pizza is {:.3f} inches squared'
        .format(pizza_diameter, pizza_area))

print_pizza_area(12.0)
print_pizza_area(16.0)

---
def print_name(name):
    print(“My name is “ + name)

my_name = "Scrappy"
print_name(my_name)
---
def get_name():
    name = input(“What is your name? “)
    return name
#This calls the user to input their name. This is stored
def my_name = get_name()
    print_name(my_name)
#This runs the Get-Name function, which returns the users stored name, and stores 'that' into the new my_name function

---

user_input = int(input()) #the input() function is called and evaluates to a value that is then passed as an argument to the int() function.

#     ***Functions with Branches / Loops***

#     ***Functions are Objects***

def print_face():
   # print face statements...
print_face()
func = print_face
func() #Calling Func is the same as calling print_face()

#     ***KEYWORD ARGUMENTS***

#Keyword arguments must come LAST if used in conjunction with position arguments
def print_book_description(title, author, publisher, year, version, num_chapters, num_pages):
    # Format and print description of a book...

print_book_description(title='The Lord of the Rings', publisher='George Allen & Unwin',
                       year=1954, author='J. R. R. Tolkien', version=1.0,
                       num_pages=456, num_chapters=22)

#     ***Parameters with default values***
def print_date(day, month, year, style=0):

#Mixing keywords with default parameters allows omitting arbitrary arguments
# IE. Changing the argument only when necessary

#     ***Mutiple Fucntion Outputs***
# Package the multiple outputs into a single container, commonly a tuple, and to then return that container.

student_scores = [75, 84, 66, 99, 51, 65]


def get_grade_stats(scores):
    # Calculate the arithmetic mean
    mean = sum(scores) / len(scores)
    # Calculate the standard deviation
    tmp = 0
    for score in scores:
        tmp += (score - mean) ** 2
    std_dev = (tmp / len(scores)) ** 0.5
    # Package and return average, standard deviation in a tuple
    return mean, std_dev
# Unpack tuple
average, standard_deviation = get_grade_stats(student_scores)
print('Average score:', average)
print('Standard deviation:', standard_deviation)
#                                   ****Strings****

variable = input()
variable = int(input) # This will force input to be an integer
variable = float(input) # This will force input to be a float
variable = int/or/float/or/none(input('String')) #Int, float or none are optional. String will be attached as text with the input following
\n #Newline, use with strings
variable = ' ' #Assigns variable with empty string
'STRING_LITERAL' # String value specified in source code of program.
[] #Will recall a character or variable
variable[0] #Accesses the first character of the indicated variable
var1 = var2[-1] #Assigns first variable to second LAST character of second variable.

#String Concatenation
string1 = 1
string2 = 2
concatenated_string = string1 + string2
#Add ' ' to put a space inbetween

#                                   **String Formatting**
string.format() #The format function
print('string {what:how}) more string.'.format(what))
#Creates a string with placeholders; AKA Templates

#All of these will produce the same result; "The cat in the hat is fat"

'The {1} in the {0} is {2}.'.format('hat', 'cat', 'fat')#Positional replacement
'The {} in the {} is {}.'.format('cat', 'hat', 'fat') #Inferred positional replacement
'The {animal} in the {headwear} is {shape}.'.format(animal='cat', headwear='hat', shape='fat') #Named replacement

print('April {}, {}'.format(22, 2020)) #April 22, 2020

date = 'April {}, {}'
print(date.format(22, 2020))
print(date.format(23, 2024)) #Prints both

print('{0}:{1}'.format(9, 43)) #9:43

month = 'April'
day = 22
print('Today is {month} {0}'.format(day, month=month)) #Today is April 22

print('Hi {{{0}}}!'.format('Bilbo')) #Hi {Bilbo}!
#A single brace is printed by using the double brace {{ }} around the replacement field {0}.

#     **Format Specification**
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
#    **Slice stride***
print('All numbers: {}'.format(numbers[::])) #All numbers
print('Every other number: {}'.format(numbers[::2])) #Every other number
print('Every third number between 1 and 8: {}'.format(numbers[1:9:3])) #Every 3rd number between 1 and 8

#**Example**
first_variable = Cat dog
slice_variable = first_variable[4:6]
print(slice_variable)
#yields Dog

#    ****String Replacing****

string = 'String'

string = string.replace ('old', 'new')

#     ****Finding****
#These are used to find the Specific location
string.find('!') #Will return the first instance of !
string.find('!', 2) #Will find ! starting at position 2
string.find('!', 2, 4) #Will find ! between 2 and 4
string.count('!') #Returns how many times ! appears

#     **Comparing String**
Relational Operators (<, <=, >, >=)
Equality operators (==, !=)
Membership operators (in, not in)
Identity operators (is, is not)

isalnum() -- #Returns True if all characters in the string are lowercase or uppercase letters, or the numbers 0-9.
isdigit() -- #Returns True if all characters are the numbers 0-9.
islower() -- #Returns True if all cased characters are lowercase letters.
isupper() -- #Return True if all cased characters are uppercase letters.
isspace() -- #Return True if all characters are whitespace.
startswith(x) -- #Return True if the string starts with x.
endswith(x) -- #Return True if the string ends with x.

#     **Splitting**
split() #Separates string into tokens

string = 'Music/artist/song.mp3'
my_tokens = string.split('/')
#Returns my_tokens = ['Music', 'artist', 'song.mp3']

song = "I scream; you scream; we all scream, for ice cream.\n"
song.split('\n')
#Returns [ Iscream; you scream; we all scream, for ice cream.', ' ']
#The string ends with a separator character, so an empty string is created in the tokens list.

#     **Joining**
join() #Joins list of strings together into 1

web_path = [ 'www.website.com', 'profile', 'settings' ] #Take a list of strings
separator = '/' #Designate how to separate them (Separator is a variable, not a function)
url = separator.join(web_path)
#URL is a new variable;
# separator.join means "join these with";
# (web_path) is the library of data

''.join(['http://', 'www.', 'ebay', '.com']) #Empty space string
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



#                                   ****Printing****

print(variable, 'string', )
print(end=' ') #Creates a space

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alphabet[0], alphabet[1], alphabet[25]) #Access characters as they appear in the sequence.
#Sequences start at 0.
#Using a negative [-1] will access from the right instead of the left. Negatives start at -1

print(f'string') #an F string allows you to embed expressions inside string literals
print(f'String contains a {dictionary[value_inside_dictionary]}')

print(String: {.2f} string'.format(variable))
# This will print with only 2 digits after decimal point
print(len(variable) 'String')
#This will print the number of characters in a variable, followed by a string

#     **Examples**
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
user_number = int(input('Enter number to use as index: '))
print()
print('\nLetter', user_number, 'of the alphabet is', alphabet[user_number])
#This program will return the letter of the alphabet associated with the number input.

#     **Recalling**
(Groups a series of commands together)
[Accesses an element inside a valiable] #Accesses element inside variable
{Accesses a dictionary}
action({dictionary[element]}) #Accesses an item in a dictionary

#                                   ****Lists****
#Created with [brackets], includes variables and literals

my_list = [10, 'abc']
#A list item is called an element.
#A list itself is an object, and its value is a sequence of references to the list's elements.

empty_list = [ ]

my_nums = [5, 12, 20]
my_nums[1] = -28 #This changes the 2nd value in the list
print (my_nums)

#     **Methods** Editing lists
object.typeofmethod #Standard method. Object should be a list.

object.append(value) #Adds value to end of list
object.pop(value) #Removes element at value position
object.remove(value) #Removes element containing the value

#     **Sequence Type Methods** Describing Lists

len(list) #Find the length of the list.
list1 + list2 #Produce a new list by concatenating list2 to the end of list1.
min(list) #Find the element in list with the smallest value.
max(list) #Find the element in list with the largest value.
sum(list) #Find the sum of all elements of a list (numbers only).
list.index(val) #Find the index of the first element in list whose value matches val.
list.count(val) #Count the number of occurrences of the value val in list.

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

#===========

#                                           ****NOTES****

#Lists should be used for Ordered Data, especially if the data can be changed.
#Example is student scores which can be adjusted and ordered from best to worst

#Dict provides a map from names to grades

#Tuple can be used to tally the number of each grade in the class




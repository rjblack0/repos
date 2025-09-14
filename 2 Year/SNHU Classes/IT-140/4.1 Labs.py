#Given a line of text as input, output the number of characters excluding spaces, periods, or commas.
#Note: Account for all characters that aren't spaces, periods, or commas (Ex: "r", "2", "!").

user_text = input()
count = sum(1 for char in user_text if char not in [' ', '.', ','])
print(count)

#Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it stronger by replacing characters using the key below, and by appending "q*s" to the end of the input string.

word = input()
password = ''
replacements = {'i': '!', 'a': '@', 'm': 'M', 'B': '8', 'o': '.'}
for char in word:
    password += replacements.get(char, char)
password += 'q*s'
print(password)

#This program will output a right triangle based on user specified height triangle_height and symbol triangle_char.
#(1) The given program outputs a fixed-height triangle using a * character. Modify the given program to output a right triangle that instead uses the user-specified triangle_char character. (1 pt)
#(2) Modify the program to use a loop to output a right triangle of height triangle_height. The first line will have one user-specified character, such as % or *. Each subsequent line will have one additional user-specified character until the number in the triangle's base reaches triangle_height. Output a space after each user-specified character, including a line's last user-specified character. (2 pts)

triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
print('')

for i in range(1, triangle_height + 1):
    print((triangle_char + ' ') * i)

#Mad Libs are activities that have a person provide various words, which are then used to complete a short story in unexpected (and hopefully funny) ways.
#Write a program that takes a string and an integer as input, and outputs a sentence using the input values as shown in the example below. The program repeats until the input string is quit and disregards the integer input that follows.


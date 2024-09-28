C++ Project Cheat Sheet
### C++ Basics
- **#include <iostream>**
 Includes the library for standard input/output (cout, cin).
- **using namespace std;**
 Allows you to use objects and variables from the standard namespace without needing to prefix
them (e.g., std::cout).
---
### Output & Input
- **cout <<**
 Sends a message or data to the standard output (usually the console).
 Example:
 cout << "Hello, World!" << endl;
- **cin >>**
 Reads input from the user into a variable.
 Example:
 int age;
 cin >> age;
- **endl**
 Moves the cursor to the next line (similar to \n but flushes the buffer).
 Example:
 cout << "Hello" << endl;
---
### Variables and Data Types
- **int**
 Integer data type.
 Example:
 int number = 0;
- **string**
 Represents a sequence of characters (text).
 Example:
 string name = "John";
- **const**
 Declares a constant, meaning its value cannot be changed.
 Example:
 const int MAX_HOURS = 23;
---
### Functions
- **Defining a function:**
 A block of reusable code that performs a specific task.
 Example:
 int add(int a, int b) {
 return a + b;
 }
- **Calling a function:**
 Example:
 int sum = add(3, 5);
---
### Control Structures
- **if-else**
 Executes code based on a condition.
 Example:
 if (age > 18) {
 cout << "Adult";
 } else {
 cout << "Minor";
 }
- **while Loop**
 Repeats a block of code while a condition is true.
 Example:
 while (userChoice != 4) {
 cout << "Menu options...";
 }
- **for Loop**
 Repeats a block of code a set number of times.
 Example:
 for (int i = 0; i < 10; i++) {
 cout << i << endl;
 }
- **switch**
 Selects and executes one of many code blocks based on the value of a variable.
 Example:
 switch(userChoice) {
 case 1:
 cout << "Option 1";
 break;
 case 2:
 cout << "Option 2";
 break;
 default:
 cout << "Invalid";
 }
---
### Operators
- **Arithmetic Operators:**
 +, -, *, /, %
 Example:
 int sum = 5 + 3; // 8
- **Comparison Operators:**
 ==, !=, >, <, >=, <=
 Example:
 if (a == b) { /* do something */ }
- **Logical Operators:**
 && (AND), || (OR), ! (NOT)
 Example:
 if (a > 0 && b > 0) { /* both are positive */ }
---
### String Manipulation
- **string.length()**
 Returns the length of a string.
 Example:
 int len = name.length();
- **string.insert()**
 Inserts a character or string at a specific position.
 Example:
 name.insert(0, "Mr. ");
- **string(n, c)**
 Creates a string of n characters c.
 Example:
 string stars = string(5, '*'); // "*****"
---
### Modulus Operator (%)
- Used to get the remainder of a division.
 Example (useful for clock formatting):
 int hour = (hour + 1) % 24; // Wraps hours after 24
---
### Structures (Structs)
- **struct**
 Used to create custom data types that group multiple variables.
 Example:
 struct TimeClock {
 int hour;
 int minute;
 int second;
 };
---
### Best Practices
- **Declare variables at the beginning of functions.**
 Always initialize variables before using them.
- **Use meaningful variable names.**
 Avoid single-character names except for loop counters.
- **Use constants for fixed values.**
 Example: const int MAX_HOURS = 23;
- **Wrap operations correctly to prevent overflow.**
 Example for clock time:
 hour = (hour + 1) % 24;

                                        /*
                                    Classes
                                        */

 //Public Variable
 /*The main function can access any public variable or function in the class period. 
 The use of public variables is not recommended because the developer cannot control or determine how variable 
 values change since any entity in the program can access the variable and change it.*/

 //Private
//Private variables can be accessed only by functions defined within the class or any class that inherits our class. 
//You cannot access private variables from main().

 //Protected
 //Protected variables are accessed only by the class functions. 
 //If a class inherits our class, that child class cannot access the protected variables.

 /*
 Abstration
 */

/*
Abstraction means to have a user interact with an item at a high-level, with lower-level internal details hidden from the 
user (aka information hiding or encapsulation). Ex: An oven supports an abstraction of a food compartment and a knob to 
control heat. An oven's user need not interact with internal parts of an oven.

Objects strongly support abstraction, hiding entire groups of functions and variables, exposing only certain functions 
to a user.
*/

/*An abstract data type (ADT) is a data type whose creation and update are constrained to specific well-defined operations. 
A class can be used to implement an ADT.*/


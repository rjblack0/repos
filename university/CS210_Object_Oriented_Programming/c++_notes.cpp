#include <iosstream>
using namespace std;

int main () {
    int wage;

    wage = 20;

    cout << "Salary is ";       // cout = common out
    cout << wage * 40 * 52;
    cout << endl;               // endl = end line

    return 0                    // return 0 = no errors
}

cin >> x                        // Characters In
                                //This gathers input from keyboard

int main () {
    int wage;

    cin >> wage;                // This will put keyboard value to 'wage'

    cout << "Salary is ";
    cout << wage * 40 * 52;
    cout << endl;

    return 0
}

//Manipulator
//Output formatting; Overloads the insertion operator (<< / >>)

//fixed
//Fixed-point notation
//12.3400000
cout << fixed << 12.34

//Identifiers

//Constant Variables
//Variables that are declared and cannot ever be changed later

//Type Conversions
int
double

    //Type Casting
    //To explicitly convert an item's type.
        //Ex. program needs a floating-point result from dividing two integers, and at least one of the integers needs to be converted to double so that floating-point division is performed

static_cast<type>(expression) // converts expressions value to the indicated type

// Characters

char myChar 'm'; // This will sort a single character, ex. m
    //Must be surrounded by single quotes

//Escape Sequences

/*
\n newline
\t tab
\' single quote
\" double quote
\\backslash
*/

//Strings

//Initiate using #include <string>

string firstMonth = "January";

//for a string, using cin >> string will only catch the first string up to the first white space

getline(cin, stringVar)
//This will capture the entire line up until the first newline

//Random Numbers

cout << rand() << endl; // Return any number from 0-RAND_MAX
integer % 10 // This has at most 10 remainders; 0-9
rand() % 3 // Random number between 0-2

//Auto
//In Variable Declaration, using Auto as the type specifier causes the compiler to automatically deduce the type from the initializer



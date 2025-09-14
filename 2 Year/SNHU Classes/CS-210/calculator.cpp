/*
 * Calculator.cpp
 *
 *  Date: 09-14-2024
 *  Author: Ryan Blackburn
 */

#include <iostream>

using namespace std;

int main()                  // Changed Void to int for proper initialization
{
    char statement[100];
    int op1, op2;
    char operation;
    char answer = 'Y';                      // Corrected the spacing and changed double quotes to single for use with char.
    while (answer == 'Y' || answer == 'y')  // Added an 'or' statement to allow the user to enter Y or y.
    {
        cout << "Enter expression" << endl; // Fixed whitespace of endl
        cin >> op1 >> operation >> op2;     // Swapped op1 and op2 to the correct order for readability.

        if (operation == '+')       // Removed the semicolon that ended the statement here.
            cout << op1 << " + " << op2 << " = " << op1 + op2 << endl;  // Changed the incorrect >> to <<
        else if (operation == '-')  // Substituted repeated 'if's to 'else if's.
            cout << op1 << " - " << op2 << " = " << op1 - op2 << endl;
        else if (operation == '*')
            cout << op1 << " * " << op2 << " = " << op1 * op2 << endl;  // Corrected the swapped * and / symbols.
        else if (operation == '/')
            cout << op1 << " / " << op2 << " = " << op1 / op2 << endl;  // Corrected the swapped / and * symbols

        cout << "Do you wish to evaluate another expression? "; 
        cin >> answer;

        if (answer == 'N' || answer == 'n')     // Added a Check for whether the user wants to quit
            {
                break;                          // Exit the loop if user is done
        }
    }
        cout << "Program Finished." << endl;    // Tell user the program is ended
        return 0;                               // Added return 0 so the program ends
}

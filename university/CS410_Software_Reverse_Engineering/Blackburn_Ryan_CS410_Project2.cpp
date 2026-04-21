#include <iostream>
#include <string>
#include <limits>
#include <iomanip> //FIX: Added so that size of username can be limited.

using namespace std;

/*
Vulnerability 1: "char username[64];"
Risk of memory corruption with a fixed-size char buffer.
Vulnerable to overflow if input is greater than 63 chars.
*/
//FIX:Mitigated overflow risk by bounding username input size using setw() (see Vulnerability 5 fix).

                                                                                        // ## CODE REVIEW 3.1 ##
char username[64];                          //Set variables
int answer = 0;
int choice = 0;
int changechoice = 0;
int newservice = 0;

const char* name1 = "Client One";
const char* name2 = "Client Two";
const char* name3 = "Client Three";
const char* name4 = "Client Four";
const char* name5 = "Client Five";

int num1 = 1;                               //Initiate values. 
int num2 = 2;
int num3 = 1;
int num4 = 2;
int num5 = 1;

int CheckUserPermissionAccess();            //Initiate functions
void DisplayInfo();
void ChangeCustomerChoice();
                                                                                        // ## CODE REVIEW 3.2 ##
int main() {
    cout << "Created by Ryan Blackburn CS-410 Project 2\n";     //Required output statement
    cout << "Hello! Welcome to our Investment Company\n";

//FIX: Added attempt limiter to reduce brute-force risk (Vulnerability 2).
    const int MAX_LOGIN_ATTEMPTS = 3;
    int attempts = 0;

    answer = CheckUserPermissionAccess();                       //Call CheckUserPermissionAccess, loops until answer = 1
    attempts++; // FIX: Count authentication attempts.

    if (answer != 1) {
        cout << "Invalid Password. Please try again\n";
    }

/*
Vulnerability 2: "while (answer != 1) {"
Allows unlimited authentication attempts. 
Attacks are able to brute-force password without being locked out.
*/

//FIX: Limited attempts to MAX_LOGIN_ATTEMPTS. Exits after too many failures.
    while (answer != 1 && attempts < MAX_LOGIN_ATTEMPTS) {
        answer = CheckUserPermissionAccess();
        attempts++; // FIX: Count authentication attempts.
        if (answer != 1)
        {
            cout << "Invalid Password. Please try again\n";
        }
    }

//FIX: If authentication failed too many times, exit program safely.
    if (answer != 1) {
        cout << "Too many failed login attempts. Exiting program.\n";
        return 0;
    }
                                                                                        // ## CODE REVIEW 3.4 ##
    while (true) {                                              //Main loop, displays menu choices.
        cout << "What would you like to do?\n";
        cout << "DISPLAY the client list (enter 1)\n";
        cout << "CHANGE a client's choice (enter 2)\n";
        cout << "Exit the program.. (enter 3)\n";

/*
Vulnerability 3: "cin >> choice;"
No validation for non-numeric input. 
Cin fail state can trap program in bad loop or skip logic.
*/

//FIX: Validates numeric input and clears cin fail states if needed.
        cin >> choice;
        if (cin.fail()) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Invalid input. Please enter a number (1-3).\n";
            continue; // Return to menu prompt safely
        }

// FIX: Enforce valid menu range (1-3).
        if (choice < 1 || choice > 3) {
            cout << "Invalid choice. Please enter 1, 2, or 3.\n";
            continue;
        }

        cout << "You chose " << choice << endl;

        if (choice == 1) {
            DisplayInfo();
        }
        
        else if (choice == 2) {
            ChangeCustomerChoice();
        }

        if (choice == 3) {      //Exit, otherwise loop to menu.
            break;
        }
    }

    return 0;
}
                                                                                        // ## CODE REVIEW 3.3 ##
int CheckUserPermissionAccess() {                   //Permission check

/*
Vulnerability 4: "cout << "Enter your username: \n";"
Username collected but is not used for authorization.
Authentication only checks hard coded password.
*/
//FIX: Full fix would require redesign to authorize users based on username (beyond current program scope).

    cout << "Enter your username: \n";      //Accepts usernames and passwords
    
/*
Vulnerability 5: "cin >> username;"
Risk of buffer overflow.
Input into char[] is not bound, long username can overflow buffer.
*/
//FIX: Fixed size of username input validation.
    cin >> setw(sizeof(username)) >> username;

    cout << "Enter your password: \n";
    string passwordInput;
    cin >> passwordInput;

/*
Vulnerability 6: "if (passwordInput.compare("123") == 0) {"
Hard coded password embedded in source and binary.
Trivial difficulty to discover through source code, authentication can be bypassed.
*/
//FIX: This would be fixed by removing hard-coded credentials and using secure password storage + hashing

    if (passwordInput.compare("123") == 0) {    //Compare against actual password '123'
        return 1;
    }
    else {
        return 2;
    }
}

void DisplayInfo() {     //DisplayInfo loop
    cout << "  Client's Name    Service Selected (1 = Brokerage, 2 = Retirement)" << endl;

    cout << "1. " << name1 << " selected option " << num1 << endl;
    cout << "2. " << name2 << " selected option " << num2 << endl;
    cout << "3. " << name3 << " selected option " << num3 << endl;
    cout << "4. " << name4 << " selected option " << num4 << endl;
    cout << "5. " << name5 << " selected option " << num5 << endl;
}
                                                                                        // ## CODE REVIEW 3.5 ##
void ChangeCustomerChoice() {       //ChangeCustomerChoice loop
    cout << "Enter the number of the client that you wish to change\n";

/*
Vulnerabilities 7 & 8: both "cin >> changechoice;" and "cin >> newservice"
Integrity issue, No validation for non-numeric or out-of-range input.
Invalid input can set cin into a fail state or cause invalid client selections.

Vulnerability 9: Also allows invalid service values; Services choices are only 1 or 2.
*/
//FIX: Validate changechoice inputs and clear cin fail state (Vulnerabilities 7 & 8).
    cin >> changechoice;
    if (cin.fail()) {
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "Invalid input. Client number must be 1-5.\n";
        return;
    }

//FIX: Enforce valid client range to 1 - 5.
    if (changechoice < 1 || changechoice > 5) {
        cout << "Invalid client selection. Please choose a number from 1 to 5.\n";
        return;
    }

    cout << "Please enter the client's new service choice (1 = Brokerage, 2 = Retirement)\n";

//FIX: Validate newservice input and clear cin fail state (Vulnerabilities 7 & 8).
    cin >> newservice;
    if (cin.fail()) {
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "Invalid input. Service choice must be 1 or 2.\n";
        return;
    }

//FIX: Enforce valid service values to be 1 or 2. (Vulnerability 9).
    if (newservice != 1 && newservice != 2) {
        cout << "Invalid service selection. Please enter 1 (Brokerage) or 2 (Retirement).\n";
        return;
    }

/*
Vulnerability 10: "if (changechoice == 1)" block
No else or default case handling for invalid changechoice. 
Fails silently and provides no user feedback.
*/
    if (changechoice == 1) {            //If changechoice == N, set numN = newservice
        num1 = newservice;
    }
    else if (changechoice == 2) {
        num2 = newservice;
    }
    else if (changechoice == 3) {
        num3 = newservice;
    }
    else if (changechoice == 4) {
        num4 = newservice;
    }
    else if (changechoice == 5) {
        num5 = newservice;
    }
//FIX: Add default case handling to avoid silent failure (Vulnerability 10).
    else {
        cout << "Invalid client selection.\n";
    }
}
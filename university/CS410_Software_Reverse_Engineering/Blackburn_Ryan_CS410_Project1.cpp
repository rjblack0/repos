#include <iostream>
#include <string>

using namespace std;

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

int main() {
    cout << "Created by Ryan Blackburn CS-410 Project 1\n";     //Required output statement
    cout << "Hello! Welcome to our Investment Company\n";

    answer = CheckUserPermissionAccess();                       //Call CheckUserPermissionAccess, loops until answer = 1

    if (answer != 1) {
        cout << "Invalid Password. Please try again\n";
    }

    while (answer != 1) {
        answer = CheckUserPermissionAccess();
        if (answer != 1)
        {
            cout << "Invalid Password. Please try again\n";
        }
    }

    while (true) {                                              //Main loop, displays menu choices.
        cout << "What would you like to do?\n";
        cout << "DISPLAY the client list (enter 1)\n";
        cout << "CHANGE a client's choice (enter 2)\n";
        cout << "Exit the program.. (enter 3)\n";

        cin >> choice;
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

int CheckUserPermissionAccess() {                   //Permission check
    cout << "Enter your username: \n";      //Accepts usernames and passwords
    cin >> username;

    cout << "Enter your password: \n";
    string passwordInput;
    cin >> passwordInput;

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

void ChangeCustomerChoice() {       //ChangeCustomerChoice loop
    cout << "Enter the number of the client that you wish to change\n";
    cin >> changechoice;

    cout << "Please enter the client's new service choice (1 = Brokerage, 2 = Retirement)\n";
    cin >> newservice;

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
}

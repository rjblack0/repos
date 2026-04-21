/*
Ryan Blackburn
10-17-2024
CS-210, SNHU
Richard Foster

Item Tracker which processes a list of groceries from text file, and offers the following functions in a menu:
Search for Item - Displaying the amount of that item which appears in the list
Display Item Frequency - Displaying all items followed by how many times they appear in the list
Display Histogram - Displaying all items, with *'s providing a visual reference to how frequently the item appears in the list
Exit

This program helps the grocer analyze item popularity to maximize store layout.
*/

#include <iostream>                     //Standard array
#include <fstream>
#include <map>
#include <string>
#include <conio.h>                      //Allows for pausing in the menu 

using std::cin;                         //Setting up all use statements for increased readability
using std::cout;
using std::endl;
using std::ifstream;
using std::ofstream;
using std::map;
using std::string;

                                        //Declaring all functions
void displayMenu();                                                     //Displays the menu
int getInteger(int, int, const string&);                                //Used for getting integer after it has been validated
bool openInputFile(ifstream& inFile, string fileName);                  //Opens the input file
bool openOutputFile(ofstream& outFile, string fileName);                //Opens the output file
map<string, int> readInputFile(ifstream& inFile);                       //Used to read items from input file
void writeOutputFile(ofstream& outFile, map<string, int> grocList);     //Used to write to the output file
void findItem(map<string, int>& grocList);                              //Pulls and displays the frequency of x item
void listItems(map<string, int>& grocList);                             //Pulls and displays all items and their frequencies
void printHistogram(map<string, int>& grocList);                        //Pulls and displays all items as the histogram
void pause(const string& message = "Press enter to continue... ");      //Used to pause the screen, increasing usability
void cls();                                                             //Clears and resets the screen for increased usability

int main() {                            //Start main and declare are variables
    ifstream inputFile;          //File stream for reading from input
    ofstream outputFile;         //File stream for writing to output
    map<string, int> grocList;   //Map for storing items and frequencies
    string item = "";            //Temp space for holding Item name during input/output operations
    int itemsAdded = 0;          //Map, Count of items
    int itemsUpdated = 0;        //Map, Count of items after update
    int selection = 0;           //Temp space for holding user's menu selection
    bool notDone = true;         //Flag to exit the program loop

    //Open input file
    if (!openInputFile(inputFile, "P3input.txt")) {                     
        return EXIT_FAILURE; //Exit if no input file
    } //Close Open Input

    //Open output file
    if (!openOutputFile(outputFile, "frequency.dat")) {
        return EXIT_FAILURE; // Exit if no output file
    } //Close open output

    //Populate the input file to the Map
    grocList = readInputFile(inputFile);

    //Populate the frequencies to the output file
    writeOutputFile(outputFile, grocList);

    //Loop for controlling and displaying the Main Menu
    do {
        displayMenu(); //Display the menu
        selection = getInteger(1, 4, "Please select menu option: "); //User input for menu

        //Switch for user selection
        switch (selection) {
        case 1:
            findItem(grocList); //Find an item by input
            pause();            //Pause after displaying results
            cls();              // Clear the screen
            break;
        case 2:
            listItems(grocList); //List all items with frequencies
            pause();             //Pause
            cls();               //Clear
            break;
        case 3:
            printHistogram(grocList); //Print histogram of frequencies
            pause();                  // Pause
            cls();                    // Clear
            break;
        case 4:
            notDone = false;    //Exit the program loop
            break;
        default:
            cout << "Invalid option. Please try again." << endl;    //If no correct option is selected, error
        } //Exit user selection switch
    } //Exit do loop 
    
    while (notDone); //Continue looping until Exit is selected

    return 0; // If Exit is selected, end the program
} //End do loop for main menu

//Function, displays the menu
void displayMenu() {
    cout << "\nMenu:\n";
    cout << "1. Search for an item\n";
    cout << "2. Display all item frequencies\n";
    cout << "3. Display histogram of frequencies\n";
    cout << "4. Exit\n";
}

//Function, gets only validated integer input
int getInteger(int min, int max, const string& prompt) {
    int selection; //Variable for menu selection
    do {
        cout << prompt;
        cin >> selection;
        if (cin.fail()) {           //Check if invalid
            cin.clear();            //Clear any error flags
            cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');                              //Clear invalid input from buffer
            cout << "Invalid input. Please enter a number between " << min << " and " << max << ".\n";  //Error message
        } //Close input validation Do loop
    } //Close Get interger loop for input validation
    
    while (selection < min || selection > max || cin.fail());   //Repeat loop until input is valid
    return selection;                                           // Return the validated input
} //End input validation function

//Function, opens input
bool openInputFile(ifstream& inFile, string fileName) {
    inFile.open(fileName);                                                  //Opens the file
    if (inFile.fail()) {                                                    //If there is a failure, start loop
        cout << "Error: Could not open input file " << fileName << endl;    //Display error message
        return false;                                                       //Tell the system that file was not received
    } //End failure check loop
    return true;                                                            //Proceed only if file opened successfully
} //End open input function

//Function, opens output
bool openOutputFile(ofstream& outFile, string fileName) {
    outFile.open(fileName);                                                 //Opens the file
    if (outFile.fail()) {                                                   //If there is a failure, start loop
        cout << "Error: Could not open output file " << fileName << endl;   //Display error message
        return false;                                                       //Tell the system that file was not received
    } //End failure check loop
    return true;                                                            //Proceed only if file opened successfully
} //End open output function

//Function, reads input data to the map
map<string, int> readInputFile(ifstream& inFile) {
    map<string, int> grocList;                      //Start Map to store frequencies
    string item = "";                               //Variable to store each line of the file

    while (getline(inFile, item)) {                 //Read each item in the list
        grocList[item]++;                           //Increment items in the list each time they are read
    } //Close read/write loop

    return grocList; //Return map with items listed and counted
} //Close input item reading to map

//Function, writes items from the map to output file
void writeOutputFile(ofstream& outFile, map<string, int> grocList) {
    for (const auto& pair : grocList) {             //Write each item from map to output
        outFile << pair.first << " " << pair.second << endl;
    } //Close write to output loop
} //Close write output function

//Function, searchs and outputs the frequency of one item
void findItem(map<string, int>& grocList) {                 //Read the map
    string item = "";                                       //Hold users input
    cout << "Enter an item: ";                              //Prompt user
    cin.ignore();                                           //Prevent errors from newline input
    getline(cin, item);                                     //Store user selection

    if (grocList.count(item)) {                             //Start loop only if item exits
        cout << item << " " << grocList[item] << endl;      //Display the item that they selected followed by the number of that item counted
    } //End display feedback loop

    //Error loop if user input is invalid
    else {
        cout << item << " not found in the list." << endl;
    } //End error loop
} //End single item display function

//Function, outputs all items and their frequencies
void listItems(map<string, int>& grocList) {                //Access map of all items
    for (const auto& pair : grocList) {                     //Iterate through the map and print each item
        cout << pair.first << ": " << pair.second << endl;
    } //End printing loop
} //End display each item function

//Function, displays histogram
void printHistogram(map<string, int>& grocList) {           //Access map for histogram
    for (const auto& pair : grocList) {                     //Iterate through the map and print each item
        cout << pair.first << " " << string(pair.second, '*') << endl;
    } //End printing loop
} //End display histogram function

//Function, pauses the screen
void pause(const string& message) {
    cout << message;                    //Display the pause message
    cin.ignore();                       //Ignore any input clutter
    cin.get();                          //Continue after any input is received
}

//Function, clears the screen
void cls() {
    cout << "\033[2J\033[H";            //Standard escape code
    cout.flush();                       //Clears the output stream
}


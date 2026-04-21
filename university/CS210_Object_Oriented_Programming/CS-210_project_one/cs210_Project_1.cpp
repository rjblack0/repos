/*
Ryan Blackburn
CS210 Project One (Single File)
This program first asks a user for input (Hours, minutes, seconds) and displays two clocks-- one 12 hour and one 24 hour-- side by side
It then allows the user to add hours, minutes, and seconds to the clock, or will exit when prompted.
*/

#include <iostream>             // Allows for standard input and output
#include <iomanip>              // Allows setw and setfill to format output
#include <string>               // Allows standard string rules

using namespace std;            // Allows standard namespace rules

            // Structure for use later in the program for formatting the clock
struct TimeClock {
    int hour = 0;               // Initiate hours, minutes and seconds as 0.
    int minutes = 0;
    int seconds = 0;
    string amPm = "AM";         // Keeps track of whether the time is AM or PM for 12-hour clock

    TimeClock() = default;      // This tells the structure that the current status of TimeClock is the default. This allows better clarity for the programs function.
};  //Ends TimeClock structure

            // This section sets the MAXIMUM value for valid input ranges
const int MAX_HOURS = 23;               // Maximum valid hour value for 24-hour format
const int MAX_MINUTES_SECONDS = 59;     // Maximum valid minute/second value

// Function to generate a string of 'length' characters 'fillChar'
string nCharString(size_t length, char fillChar) {
    return string(length, fillChar);    // Create and return a string of 'length' 'fillChar' characters
}

// Function to center text within a given length and fill with a specified character
string centerText(string text, int length, char fill = ' ') {
    int textLength = text.length(); // Get the length of the text to be centered
    string centeredText = ""; // Stores final version of text with padding

    if (textLength >= length) {
        return text; // If the text is longer than the line, return original text
    }
    else {
        int charsNeeded = (length - textLength); // Calculate how many characters are needed
        int paddingNeeded = charsNeeded / 2; // Determine left and right padding
        string leftPadding = string(paddingNeeded, fill);
        string rightPadding = leftPadding;
        centeredText = leftPadding + text + rightPadding;

        if (charsNeeded % 2 != 0) { // Add an extra padding character if needed
            centeredText.insert(0, 1, fill);
        }
        return centeredText;
    }
}

            /* Function to get valid user input within a specific range
                When called in Main, the function sets the following parameters:
                    The first value will be the min, which is 0
                    The second value will be the max, which is either 23 or 59 depending on whether it calls MAX_HOUR or MAX_MINUTES_SECONDS
                    Which prompt (hours, minutes, seconds) to use
                It then checks to ensure that the values are valid.
                    If not, it produces an error, repeats the request, and asks for the next value
                When successful it stores value and ends
            */
int getValidInput(int min, int max, const string& prompt) {     //Sets all parameters
    int value;                                                  //Inititalizes value variable, used to store user input
    cout << prompt;                                             //Asks user for prompt as defined in the parameters
    cin >> value;                                               //Adds the users input to value
    while ((value < min) || (value > max)) {                    //Performs a check to verify that the value is valid
        cout << "Invalid input. Please enter a value between " << min << " and " << max << "." << endl;
        cout << prompt;
        cin >> value;                                           //While loop to get a new value
    } //Ends while loop
    return value;                                               //Finalizes the value of the 'value' variable.
} //Ends getValidInput function

            // Function to format numbers as two digits
string twoDigitString(int num) {        //This variable twoDigitString is used in the next function to ensure it's formatted correctly
    if (num < 10) {
        return "0" + to_string(num);    //Add leading 0 for numbers less than 10
    } else {
        return to_string(num);          //If not, number gets returned as it was.
    } //Ends if/else statement
} //Ends twoDigitString function

            //First function which displays time in 12 hour format.
string displayTime12Hour(TimeClock& clock) {    //This passes an instance of TimeClock, and allows the function in Main to define this as the 12hr clock
    int displayHour = clock.hour % 12;          //When using this clock type, 12 is Max
    string period;                              //Variable for storing whether the time is AM or PM.
    if (displayHour == 0) displayHour = 12;     //When there is a 0, convert to 12 for handling midnight and noon
    if (clock.hour >= 12) {         //Simple if/else which will determine whether to use AM or PM
        period = " PM";
    } else {
        period = " AM";
    } //Ends if/else statement
            //Now that I have my properly formatted number, store it inside twoDigitString
    return twoDigitString(displayHour) + ":" +
           twoDigitString(clock.minutes) + ":" +
           twoDigitString(clock.seconds) + period;
} //Ends displayTime12Hour function

            //The 24 hour function is able to forgoe the checking and converting, since the maximum and minimum are already verified.
            //Therefore it simply prints the value of clock.hour in TimeClock
string displayTime24Hour(TimeClock& clock) {
    return twoDigitString(clock.hour) + ":" +
           twoDigitString(clock.minutes) + ":" +
           twoDigitString(clock.seconds);
} //Ends displayTime24Hour function

/* This function displays both clocks together side by side, calling the individual 12 hour and 24 hour clocks.
    After calling the parameter set displayClocks, it will next generate the menus based on a width of 27 for the top and bottom
    And format calling displayTime to fit in the middle
*/
// Function to display both clocks side by side with centered text
void displayClocks(TimeClock& clock) {
    const int totalWidth = 27;  // Define total width for each clock's section
    
    // Create the top borders
    cout << nCharString(totalWidth, '*') << "   " << nCharString(totalWidth, '*') << endl;
    
    // Create the clock labels, centered in each section
    cout << "*" << centerText("12-Hour Clock", totalWidth - 2) << "*"
         << "   "
         << "*" << centerText("24-Hour Clock", totalWidth - 2) << "*" << endl;
    
    // Display the clock times
    string clock12HourDisplay = displayTime12Hour(clock);
    string clock24HourDisplay = displayTime24Hour(clock);
    
    // Dynamically center the time displays
    cout << "*" << centerText(clock12HourDisplay, totalWidth - 2) << "*"
         << "   "
         << "*" << centerText(clock24HourDisplay, totalWidth - 2) << "*" << endl;
    
    // Create the bottom borders
    cout << nCharString(totalWidth, '*') << "   " << nCharString(totalWidth, '*') << endl;
}

// User Menu
    //Beginning here I display all of the users options first
// Function to display the user menu with centered text
void displayMenu() {
    const int totalWidth = 27;  // Define total width for the menu

    cout << nCharString(totalWidth, '*') << endl;       //Top border
    cout << "*" << centerText("1 - Add One Hour", totalWidth - 2) << "*" << endl;
    cout << "*" << centerText("2 - Add One Minute", totalWidth - 2) << "*" << endl;
    cout << "*" << centerText("3 - Add One Second", totalWidth - 2) << "*" << endl;
    cout << "*" << centerText("4 - Exit Program", totalWidth - 2) << "*" << endl;
    cout << nCharString(totalWidth, '*') << endl;       //Bottom border
    cout << "Enter your choice: ";
} //End menu display

/*Functions to add one to each of the hours, minutes and seconds
    Hours value will wrap around to 0 once it reaches 24
    Minutes will wrap around to 0 once it reaches 60, and also will call addOneHour() to increase the hours by 1
    Seconds will wrap around to 0 once it reaches 60, and also will call addOneMinute() to increase the minutes by 1
This allows the clock to function as it should normally inside Main()
*/ 

// Function to add one hour, wrapping around to 0 after 24
void addOneHour(TimeClock& clock) {
    clock.hour = (clock.hour + 1) % 24;         //Increase by 1 and wrap after 24
} //Ends addOneHour function

// Function to add one minute, wrapping around to 0 after 60, and increment hours if necessary
void addOneMinute(TimeClock& clock) {
    clock.minutes = (clock.minutes + 1) % 60;   //Increase by 1 and wrap after 60
    if (clock.minutes == 0) {                   //If minutes wrap to 0, increment hour
        addOneHour(clock);
    } 
} //Ends addOneMinute function

// Function to add one second, wrapping around to 0 after 60, and increment minutes if necessary
void addOneSecond(TimeClock& clock) {
    clock.seconds = (clock.seconds + 1) % 60;   //Increase by 1 and wrap after 60
    if (clock.seconds == 0) {                   //If seconds wrap to 0, increment minute
        addOneMinute(clock);
    } 
} //Ends addOneSecond function

/* Main function
    First initialize the structure TimeClock and call the specific .clock it's using
 */
int main() {
    TimeClock clock;                //Initialize clock structure
    
    int userChoice = 0;             //Initializes a variable userChoice for storing the users input
                            //This function gets the users initial time input, calling getValidInput to ensure it will only accept times between 0-23 or 0-59
    clock.hour = getValidInput(0, MAX_HOURS, "Enter the initial hour (0-23): ");
    clock.minutes = getValidInput(0, MAX_MINUTES_SECONDS, "Enter the initial minutes (0-59): ");
    clock.seconds = getValidInput(0, MAX_MINUTES_SECONDS, "Enter the initial seconds (0-59): ");

                        //Programs main While Loop which utilizes input from previously defined functions
    while (userChoice != 4) {        //Avoiding while(true), this will execute as long as the user does not enter 4.
                        //This will display the Clock, which contains both 12 and 24 hour times
        displayClocks(clock);

        displayMenu();
        cin >> userChoice;              //Ask the user for their input
        //Perform the following actions depending on the users choice:
        switch (userChoice) {
            case 1:
                addOneHour(clock);      // Add one hour
                break;
            case 2:
                addOneMinute(clock);    // Add one minute
                break;
            case 3:
                addOneSecond(clock);    // Add one second
                break;
            case 4:                     //Case 4 has no function to call; it displays the end message and ends the program.
                cout << "Exiting program..." << endl;
                return 0;                   //This ends the program
                        //If no proper choice is entered, display the default error message
            default:
                cout << "Invalid choice. Please try again." << endl;
        } //Ends the userChoice switch
    } //Ends the Main function
    
    return 0;           //After all is said and done, failsafe to end the program
}
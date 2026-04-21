#include <iostream>             
#include <iomanip>              
#include <string>               

using namespace std;            

struct TimeClock {
    int hour = 0;               
    int minutes = 0;
    int seconds = 0;
    string amPm = "AM";         

    TimeClock() = default;      
};  

const int MAX_HOURS = 23;               
const int MAX_MINUTES_SECONDS = 59;     

string nCharString(size_t length, char fillChar) {
    return string(length, fillChar);    
}

string centerText(string text, int length, char fill = ' ') {
    int textLength = text.length(); 
    string centeredText = ""; 

    if (textLength >= length) {
        return text; 
    }
    else {
        int charsNeeded = (length - textLength); 
        int paddingNeeded = charsNeeded / 2; 
        string leftPadding = string(paddingNeeded, fill);
        string rightPadding = leftPadding;
        centeredText = leftPadding + text + rightPadding;

        if (charsNeeded % 2 != 0) { 
            centeredText.insert(0, 1, fill);
        }
        return centeredText;
    }
}

int getValidInput(int min, int max, const string& prompt) {     
    int value;                                                  
    cout << prompt;                                             
    cin >> value;                                               
    while ((value < min) || (value > max)) {                    
        cout << "Invalid input. Please enter a value between " << min << " and " << max << "." << endl;
        cout << prompt;
        cin >> value;                                           
    } 
    return value;                                               
} 

string twoDigitString(int num) {        
    if (num < 10) {
        return "0" + to_string(num);    
    } else {
        return to_string(num);          
    } 
} 

string displayTime12Hour(TimeClock& clock) {    
    int displayHour = clock.hour % 12;          
    string period;                              
    if (displayHour == 0) displayHour = 12;     
    if (clock.hour >= 12) {
        period = " PM";
    } else {
        period = " AM";
    } 
    return twoDigitString(displayHour) + ":" +
           twoDigitString(clock.minutes) + ":" +
           twoDigitString(clock.seconds) + period;
} 

string displayTime24Hour(TimeClock& clock) {
    return twoDigitString(clock.hour) + ":" +
           twoDigitString(clock.minutes) + ":" +
           twoDigitString(clock.seconds);
} 

void displayClocks(TimeClock& clock) {
    const int totalWidth = 27;  
    
    cout << nCharString(totalWidth, '*') << "   " << nCharString(totalWidth, '*') << endl;
    
    cout << "*" << centerText("12-Hour Clock", totalWidth - 2) << "*"
         << "   "
         << "*" << centerText("24-Hour Clock", totalWidth - 2) << "*" << endl;
    
    string clock12HourDisplay = displayTime12Hour(clock);
    string clock24HourDisplay = displayTime24Hour(clock);
    
    cout << "*" << centerText(clock12HourDisplay, totalWidth - 2) << "*"
         << "   "
         << "*" << centerText(clock24HourDisplay, totalWidth - 2) << "*" << endl;
    
    cout << nCharString(totalWidth, '*') << "   " << nCharString(totalWidth, '*') << endl;
}

void displayMenu() {
    const int totalWidth = 27;  

    cout << nCharString(totalWidth, '*') << endl;
    cout << "*" << centerText("1 - Add One Hour", totalWidth - 2) << "*" << endl;
    cout << "*" << centerText("2 - Add One Minute", totalWidth - 2) << "*" << endl;
    cout << "*" << centerText("3 - Add One Second", totalWidth - 2) << "*" << endl;
    cout << "*" << centerText("4 - Exit Program", totalWidth - 2) << "*" << endl;
    cout << nCharString(totalWidth, '*') << endl;
    cout << "Enter your choice: ";
}

void addOneHour(TimeClock& clock) {
    clock.hour = (clock.hour + 1) % 24;         
} 

void addOneMinute(TimeClock& clock) {
    clock.minutes = (clock.minutes + 1) % 60;   
    if (clock.minutes == 0) {                   
        addOneHour(clock);
    } 
} 

void addOneSecond(TimeClock& clock) {
    clock.seconds = (clock.seconds + 1) % 60;   
    if (clock.seconds == 0) {                   
        addOneMinute(clock);
    } 
} 

int main() {
    TimeClock clock;                
    
    int userChoice = 0;             
    clock.hour = getValidInput(0, MAX_HOURS, "Enter the initial hour (0-23): ");
    clock.minutes = getValidInput(0, MAX_MINUTES_SECONDS, "Enter the initial minutes (0-59): ");
    clock.seconds = getValidInput(0, MAX_MINUTES_SECONDS, "Enter the initial seconds (0-59): ");

    while (userChoice != 4) {        
        displayClocks(clock);
        displayMenu();
        cin >> userChoice;              

        switch (userChoice) {
            case 1:
                addOneHour(clock);      
                break;
            case 2:
                addOneMinute(clock);    
                break;
            case 3:
                addOneSecond(clock);    
                break;
            case 4:                     
                cout << "Exiting program..." << endl;
                return 0;                   
            default:
                cout << "Invalid choice. Please try again." << endl;
        } 
    } 
    
    return 0;           
}
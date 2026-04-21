#include <iostream>               // Includes the input/output stream library for cin and cout
#include <iomanip>                // Includes the iomanip library for setprecision
using namespace std;              // Allows the use of standard names like cout and cin without the std:: prefix

int main() {

   double gasMileage, gasCostPerGallon;   // Declares two double variables to store gas mileage and gas cost per gallon

   cin >> gasMileage >> gasCostPerGallon; // Takes input from the user for gas mileage and gas cost per gallon

   cout << fixed << setprecision(2);      // Sets the output to display exactly 2 decimal places

   // Outputs the cost to drive 20 miles, calculated by (20 miles / gas mileage) * gas cost per gallon
   cout << (20.0 / gasMileage) * gasCostPerGallon << " ";

   // Outputs the cost to drive 75 miles, calculated by (75 miles / gas mileage) * gas cost per gallon
   cout << (75.0 / gasMileage) * gasCostPerGallon << " ";

   // Outputs the cost to drive 500 miles, calculated by (500 miles / gas mileage) * gas cost per gallon
   cout << (500.0 / gasMileage) * gasCostPerGallon << endl;

   return 0;  // Returns 0, signaling successful execution of the program
}
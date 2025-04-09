#include <iostream>
using namespace std;

int main () {
   int hourlyWage;
   
   hourlyWage = 20;

   cout << "Annual salary is: ";
   cout << hourlyWage * 40 * 50;
   cout << endl;

   cout << "Monthly salary is: ";
   cout << ((hourlyWage * 40 * 50) / 12);
   cout << endl;

   return 0;
}
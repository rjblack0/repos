#include <iostream>
#include <iomanip>
using namespace std;

int main() {   
   double miles = 765.4261;
      
   cout << "setprecision(p) sets # digits" << endl;
   cout << miles << " (default p is 6)" << endl;
   cout << setprecision(8) << miles << " (p = 8)" << endl;
   cout << setprecision(5) << miles << " (p = 5)" << endl;
   cout << setprecision(2) << miles << " (p = 2)" << endl;
   cout << miles << endl << endl;
      
   // fixed uses fixed point notation
   cout << fixed;
   cout << "fixed: " << miles << endl;
   
   // scientific uses scientific notation
   cout << scientific;
   cout << "scientific: " << miles << endl;
   
   return 0;
}
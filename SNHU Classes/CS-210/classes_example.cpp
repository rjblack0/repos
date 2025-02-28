/*
Example 1
*/

#include <iostream>
#include <string>
using namespace std;

class Message
{
private:
    string Msg;
public:
    void SetMessage(string M) { Msg = M;}
    void PrintMessage() { cout << Msg << endl;}
};

int main()
{
    Message myMsg;
    myMsg.SetMessage("Welcome to class");
    myMsg.PrintMessage();

   return 0;

}

/*
Example 2
*/

class Restaurant {                          // Info about a restaurant   
   public:                                          
      void SetName(string restaurantName);  // Sets the restaurant's name              
      void SetRating(int userRating);       // Sets the rating (1-5, with 5 best)      
      void Print();                         // Prints name and rating on one line   

   ...
};

/*
Example 3
*/


int main() {
   Restaurant favLunchPlace;
   Restaurant favDinnerPlace;

   favLunchPlace.SetName("Central Deli");
   favLunchPlace.SetRating(4);

   favDinnerPlace.SetName("Friends Cafe");
   favDinnerPlace.SetRating(5);

   cout << "My favorite restaurants: " << endl;
   favLunchPlace.Print();
   favDinnerPlace.Print();

   return 0;
}

/*
My favorite restaurants: 
Central Deli -- 4
Friends Cafe -- 5
*/

/*
Example 4
*/

//Strings are Classes
//String class public member functions:

char& at(size_t pos);   // Returns a reference to the character at position pos in the string.

size_t length() const;  // Returns the number of characters in the string

void push_back(char c); // Appends character c to the string's end (increasing length by 1)

/*
In-line Member Functions
*/

A mutator function may modify ("mutate") a class' data members.
An accessor function accesses data members but does not modify a class' data members.


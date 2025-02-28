#include <iostream>                     //Standard for input/output operations.
using namespace std;

#include "ItemToPurchase.h"             //This allows Main to use the ItemToPurchase class file.

int main() {
   ItemToPurchase item1;                //Declaring two objects that are of the ItemToPurchase class
   ItemToPurchase item2;

   string name;                         //Declaring variables
   int price;
   int quantity;

   cout << "Item 1" << endl;            //Gathering user input for Item 1 Name
   cout << "Enter the item name:" << endl;          //Programming standards, using a new line for each prompt
   getline(cin, name);
   item1.SetName(name);                      //Setter for the Name of Item 1

   cout << "Enter the item price:" << endl;    //Gathering user input for Item 1 Price
   cin >> price;
   item1.SetPrice(price);                    //Setter for the Price of Item 1

   cout << "Enter the item quantity:" << endl; //Gathering user input for Item 1 Quantity
   cin >> quantity;
   item1.SetQuantity(quantity);              //Setter for the Quantity of Item 1

   cin.ignore();

                                        //Repeating all previous tasks, for item 2
   cout << "\nItem 2" << endl;               //Item 2 Name
   cout << "Enter the item name:" << endl; 
   getline(cin, name);
   item2.SetName(name); 

   cout << "Enter the item price:" << endl;         //Item 2 Price
   cin >> price;
   item2.SetPrice(price);

   cout << "Enter the item quantity:" << endl;      //Item 2 Quantity
   cin >> quantity; 
   item2.SetQuantity(quantity); 

   cout << "\nTOTAL COST" << endl;      //Output TOTAL COSt header

                                             //Display Item 1 Name, Quantity, Price, and Total cost.
   cout << item1.GetName() << " " << item1.GetQuantity() << " @ $" 
        << item1.GetPrice() << " = $" 
        << item1.GetQuantity() * item1.GetPrice() << endl;

                                             //Display Item 2 Name, Quantity, Price, and Total cost.
   cout << item2.GetName() << " " << item2.GetQuantity() << " @ $" 
        << item2.GetPrice() << " = $" 
        << item2.GetQuantity() * item2.GetPrice() << endl;

                                        //Combine items into total cost overall
   int totalCost = (item1.GetQuantity() * item1.GetPrice()) + 
                   (item2.GetQuantity() * item2.GetPrice()); 
   cout << "\nTotal: $" << totalCost << endl;

   return 0;  // End of the main function.
}  // End of main()
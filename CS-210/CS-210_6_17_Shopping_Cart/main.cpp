#include <iostream>
using namespace std;

#include "ItemToPurchase.h"

int main() {
   
   ItemToPurchase item1;
   ItemToPurchase item2;

   string name;
   int price;
   int quantity;

   // Input for item 1
   cout << "Item 1" << endl;
   cout << "Enter the item name: ";
   getline(cin, name);
   item1.SetName(name);
   
   cout << "Enter the item price: ";
   cin >> price;
   item1.SetPrice(price);

   cout << "Enter the item quantity: ";
   cin >> quantity;
   item1.SetQuantity(quantity);

   cin.ignore();  // To clear newline for the next getline

   // Input for item 2
   cout << "\nItem 2" << endl;
   cout << "Enter the item name: ";
   getline(cin, name);
   item2.SetName(name);

   cout << "Enter the item price: ";
   cin >> price;
   item2.SetPrice(price);

   cout << "Enter the item quantity: ";
   cin >> quantity;
   item2.SetQuantity(quantity);

   // Output the total cost
   cout << "\nTOTAL COST" << endl;
   cout << item1.GetName() << " " << item1.GetQuantity() << " @ $" << item1.GetPrice() 
        << " = $" << item1.GetQuantity() * item1.GetPrice() << endl;
   cout << item2.GetName() << " " << item2.GetQuantity() << " @ $" << item2.GetPrice() 
        << " = $" << item2.GetQuantity() * item2.GetPrice() << endl;

   int totalCost = (item1.GetQuantity() * item1.GetPrice()) + (item2.GetQuantity() * item2.GetPrice());
   cout << "\nTotal: $" << totalCost << endl;

   
   return 0;
}
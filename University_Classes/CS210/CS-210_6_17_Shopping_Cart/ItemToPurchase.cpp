#include <iostream>                    //Standard
using namespace std;

#include "ItemToPurchase.h"            //This allows this program to use the ItemToPurchase class file.

ItemToPurchase::ItemToPurchase() {     //Initialize all variables
   itemName = "none";                     //All values are set to default values
   itemPrice = 0; 
   itemQuantity = 0;
}//End ItemToPurchase

void ItemToPurchase::SetName(string name) {     //Create the Mutator for Name
   itemName = name;                             //Assigns input to name
} //End SetName

void ItemToPurchase::SetPrice(int price) {      //Create the Mutator for Price
   itemPrice = price;                           //Assigns input to price
}  //End SetPrice

void ItemToPurchase::SetQuantity(int quantity) {   //Create the Mutator for Quantity
   itemQuantity = quantity;                        //Assigns input to quantity
}  //End SetQuantity

string ItemToPurchase::GetName() const {        //Access item Name
   return itemName;                                //Retrieves the value of the itemName
}  //End GetName

int ItemToPurchase::GetPrice() const {          //Access item Price
   return itemPrice;                               //Retrieves the value of the itemPrice
}  //End GetPrice

int ItemToPurchase::GetQuantity() const {       //Access item Quantity
   return itemQuantity;                            //Retrieves the value of the itemQuantity
}  //End GetQuantity
#include <iostream>
using namespace std;

#include "ItemToPurchase.h"

// Default constructor
ItemToPurchase::ItemToPurchase() {
   itemName = "none";
   itemPrice = 0;
   itemQuantity = 0;
}

// Setters
void ItemToPurchase::SetName(string name) {
   itemName = name;
}

void ItemToPurchase::SetPrice(int price) {
   itemPrice = price;
}

void ItemToPurchase::SetQuantity(int quantity) {
   itemQuantity = quantity;
}

// Getters
string ItemToPurchase::GetName() const {
   return itemName;
}

int ItemToPurchase::GetPrice() const {
   return itemPrice;
}

int ItemToPurchase::GetQuantity() const {
   return itemQuantity;
}
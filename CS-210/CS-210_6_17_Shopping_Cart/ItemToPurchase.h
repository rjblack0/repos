#ifndef ITEM_TO_PURCHASE_H
#define ITEM_TO_PURCHASE_H

#include <string>
using namespace std;

class ItemToPurchase {
   private:
      string itemName;
      int itemPrice;
      int itemQuantity;

   public:
      // Default constructor
      ItemToPurchase();

      // Setters
      void SetName(string name);
      void SetPrice(int price);
      void SetQuantity(int quantity);

      // Getters
      string GetName() const;
      int GetPrice() const;
      int GetQuantity() const;
};

#endif
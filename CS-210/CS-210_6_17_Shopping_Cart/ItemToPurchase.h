#ifndef ITEM_TO_PURCHASE_H             //Standard, restricts to this class type
#define ITEM_TO_PURCHASE_H

#include <string>                      //Standard, allows strings, standard names
using namespace std;

class ItemToPurchase {                 //Inititalize the Class ItemToPurchase
   private:                               //Start out with the private variables that I want to be accessed inside this class Only.
      string itemName;
      int itemPrice;
      int itemQuantity;

   public:
      ItemToPurchase();                //Also declare one public variable for sharing with the other functions

      // Setter methods (mutators)
      void SetName(string name);       //Mutator for itemName
      void SetPrice(int price);        //Mutator for itemPrice
      void SetQuantity(int quantity);  //Mutator for itemQuantity

      string GetName() const;          //Getter used for itemName
      int GetPrice() const;            //Getter used for itemPrice
      int GetQuantity() const;         //Getter used for itemQuantity
};  //End ItemToPurchase

#endif  // End class ItemToPurchase
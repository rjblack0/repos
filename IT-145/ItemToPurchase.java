public class ItemToPurchase {
    //Private fields - itemName, itemPrice, and itemQuanity
    private String itemName;      //These create the empty shells for each variable, and make sure that they're the correct type
    private int itemPrice;
    private int itemQuantity;
 
    /*Default Constructor
     itemName - Initialized to "none"
     itemPrice - Initialized to 0
     itemQuantity - Initialized ito 0
    */
     
    public ItemToPurchase() {     //Here we initialize each variable to ensure they don't remain undefined
       itemName = "none";
       itemPrice = 0;
       itemQuantity = 0;
    }
     
    //public member methods (mutators & accessors)
    
    //setName() & getName() 
    
    public void setName(String name) {     //Method to set the name of the item
       itemName = name;
    }
    public String getName() {              //Method to get the name of the item
       return itemName;
    }
    
    //setPrice() & getPrice() 
    
    public void setPrice(int price) {      //Method to set the price of the item
       itemPrice = price;
    }
    public int getPrice() {                //Method to get the price of the item
       return itemPrice;
    }
    
    //setQuantity() & getQuantity() 
    
    public void setQuantity(int quantity) {   //Method to set the quantity of the item
       itemQuantity = quantity;
    }
    public int getQuantity() {                //Method to get the quantity of the item
       return itemQuantity;
    }
    
    //print item to purchase
    
    public void printItemPurchase() {
       System.out.println(itemName + " " + itemQuantity + " @ $" + itemPrice + " = $" + (itemPrice * itemQuantity));
    }
 }
 
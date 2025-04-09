import java.util.Scanner;

public class ShoppingCartPrinter {
   public static void main(String[] args) {
      Scanner scnr = new Scanner(System.in);
      int i = 0;
      String productName;
      int productPrice = 0;
      int productQuantity = 0;
      int cartTotal = 0;
  
      ItemToPurchase item1 = new ItemToPurchase();
      ItemToPurchase item2 = new ItemToPurchase();

      // Get item 1 details from user, create itemToPurchase object
      System.out.println("Item 1");                   //Formatted per the example
      System.out.println("Enter the item name: ");      //Asks the user for the item
      item1.setName(scnr.nextLine());                 //Sets that value to Name
      System.out.println("Enter the item price: ");     //Asks the user for the price
      item1.setPrice(scnr.nextInt());                 //Sets that value to Price
      System.out.println("Enter the item quantity: ");  //Asks the user for the quantity
      item1.setQuantity(scnr.nextInt());              //Sets that value to Quantity

      // Consume the remaining newline
      scnr.nextLine();

      // Get item 2 details from user, create itemToPurchase object
      System.out.println();
      System.out.println("Item 2");                   //All of these are repeats of above, set to item 2
      System.out.println("Enter the item name: ");      
      item2.setName(scnr.nextLine());
      System.out.println("Enter the item price: ");
      item2.setPrice(scnr.nextInt());
      System.out.println("Enter the item quantity: ");
      item2.setQuantity(scnr.nextInt());      

      // Add costs of two items and print total
      cartTotal = (item1.getPrice() * item1.getQuantity()) + (item2.getPrice() * item2.getQuantity());
      
      // Total Cost
      System.out.println();
      System.out.println("TOTAL COST");    //Formatted per example
      
      // item one information
      item1.printItemPurchase();             //These use provided variables to output per direction
      // item two information
      item2.printItemPurchase();

      // Total output
      System.out.println();
      System.out.println("Total: $" + cartTotal);
      
      return;
   }
}
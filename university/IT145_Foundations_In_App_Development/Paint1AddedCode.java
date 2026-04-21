import java.util.Scanner;

public class Paint1 {

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        double wallHeight = 0.0;
        double wallWidth = 0.0;
        double wallArea = 0.0;
        double gallonsPaintNeeded = 0.0;

        final double squareFeetPerGallons = 350.0;

        // Implement a do-while loop to ensure input is valid
        boolean validInput = false; //Start out with my string condition which will auto fail if it doesn't pass my tests
        do {
            try {
                // Prompt user to input wall's height
                System.out.println("Enter wall height (feet): ");
                //Get only the next double from the input
                wallHeight = scnr.nextDouble();
                //Prevent the user from entering anything less than or equal to zero
                if (wallHeight <= 0) {
                    throw new Exception("Height must be greater than 0.");
                }
                validInput = true; //Now that my data validation is passed, we may continue.
            } catch (Exception e) { //If anything that is not the correct data type gets entered, we also error
                System.out.println("Invalid input. Please enter a valid number for wall height.");
                scnr.next(); //This is necessary here so that the bad input does not mess up the new input later.
            }
        } while (!validInput); //This code here forces the loop to continue iterating until a valid input is used.

        //This loop will operate identically to the one above, but for width. All bugs are commented with explanation of what was done.
        // Implement a do-while loop to ensure input is valid
        validInput = false;
        do {
            try {
                // Prompt user to input wall's width
                System.out.println("Enter wall width (feet): ");
                wallWidth = scnr.nextDouble(); //Bug 1: Changed to wallWidth, not wallHeight
                if (wallWidth <= 0) {
                    throw new Exception("Width must be greater than 0.");
                }
                validInput = true;
            } catch (Exception e) {
                System.out.println("Invalid input. Please enter a valid number for wall width.");
                scnr.next();
            }
        } while (!validInput);

        // Calculate and output wall area
        wallArea = wallHeight * wallWidth;
        System.out.println("Wall area: " + wallArea + " square feet"); //Bug2: Added wallArea to output

        // Calculate and output the amount of paint (in gallons) needed to paint the wall
        gallonsPaintNeeded = wallArea / squareFeetPerGallons;
        System.out.println("Paint needed: " + gallonsPaintNeeded + " gallons"); //Bug 3: Capitalization issue with variable name
    }
}
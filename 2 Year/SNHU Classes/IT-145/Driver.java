import java.util.ArrayList;
import java.util.Scanner;

public class Driver {
    // Added monkey array
    private static ArrayList<Dog> dogInventory = new ArrayList<>();         //Array for storing Dogs
    private static ArrayList<Monkey> monkeyInventory = new ArrayList<>();   //Array for storing Monkeys

    public static void main(String[] args) {
        initializeDogList();                        // Initialize lists with test data
        initializeMonkeyList();

        Scanner scanner = new Scanner(System.in);   //Initiate a new scanner
        boolean running = true;                     //Controls whether the menu is displayed

        //This is my menu, which will execute the following commands as long as running is set to true
        while (running) {
            showMenu();
            String userChoice = scanner.nextLine().trim().toLowerCase();    //Ensures that the users input doesnt get messed up based on how they input it

            switch (userChoice) {                   //The values for my menu are listed down
                case "1":
                    intakeNewDog(scanner);             // Add a new dog                
                    break;
                case "2":
                    intakeNewMonkey(scanner);          //Add a new monkey
                    break;
                case "3":
                    reserveAnimal(scanner);         //Make a reservation
                    break;
                case "4":
                    displayAnimals("dog");          //List contents of dog array
                    break;
                case "5":
                    displayAnimals("monkey");       //List contents of monkey array
                    break;
                case "6":
                    displayAnimals("available");    // Print all available (not reserved) animals
                    break;
                case "q":
                    running = false;                //When the user no longer needs to use the menu, this sets running to false and ends the menu loop
                    break;
                //This will execute if nothing else above is input
                default:
                    System.out.println("Invalid selection. Please choose a valid option.");
                    break;
            }
        }
        //Since the loop is exited, we tell the user and now can close the scanner.
        System.out.println("Exiting the application. Goodbye!");
        scanner.close();
    }

    // This method prints the menu options
    public static void showMenu() {
        System.out.println("\n\n");
        System.out.println("\t\t\t\tRescue Animal Management System");
        System.out.println("[1] Add a new dog");
        System.out.println("[2] Add a new monkey");
        System.out.println("[3] Reserve an animal");
        System.out.println("[4] List all dogs");
        System.out.println("[5] List all monkeys");
        System.out.println("[6] List all available animals");
        System.out.println("[q] Quit application");
        System.out.println();
        System.out.println("Enter your choice: ");
    }

    // Adds dogs to a list for testing
    public static void initializeDogList() {
        Dog dog1 = new Dog("Spot", "German Shepherd", "male", "1", "25.6", "05-12-2019", "United States", "intake", false, "United States");
        Dog dog2 = new Dog("Rex", "Great Dane", "male", "3", "35.2", "02-03-2020", "United States", "Phase I", false, "United States");
        Dog dog3 = new Dog("Bella", "Chihuahua", "female", "4", "25.6", "12-12-2019", "Canada", "in service", true, "Canada");

        dogInventory.add(dog1);
        dogInventory.add(dog2);
        dogInventory.add(dog3);
    }

    // Adds monkeys to a list for testing
    public static void initializeMonkeyList() {
        Monkey monkey1 = new Monkey("Larry", "Capuchin", "male", "4", "15.0", "08-20-2020", "Brazil", "in service", false, "Brazil");
        Monkey monkey2 = new Monkey("Curly", "Marmoset", "male", "3", "12.0", "06-18-2019", "Colombia", "Phase I", false, "Colombia");
        Monkey monkey3 = new Monkey("George", "Guenon", "male", "5", "18.0", "11-11-2018", "USA", "intake", true, "USA");

        monkeyInventory.add(monkey1);
        monkeyInventory.add(monkey2);
        monkeyInventory.add(monkey3);
    }

    // Beginning intakeNewDog method
    //This first part was already done for us
    public static void intakeNewDog(Scanner scanner) {
        System.out.println("Enter the dog's name:");
        String name = scanner.nextLine().trim();

        for (Dog dog : dogInventory) {
            if (dog.getName().equalsIgnoreCase(name)) {
                System.out.println("\nThis dog is already in our system.\n");
                return;
            }
        }

        //Begin by prompting the user to input all of the necessary information per instructions

        System.out.println("Enter breed:");                 //Each of these ask for input and
        String breed = scanner.nextLine().trim();               //then adds it to the appropriate variable in the array
        System.out.println("Enter gender (m/f):");
        String gender = scanner.nextLine().trim().toLowerCase();
        System.out.println("Enter age:");
        String age = scanner.nextLine().trim();
        System.out.println("Enter weight (in pounds):");
        String weight = scanner.nextLine().trim();
        System.out.println("Enter acquisition date (MM/DD/YYYY):");
        String acquisitionDate = scanner.nextLine().trim();
        System.out.println("Enter acquisition country:");
        String acquisitionCountry = scanner.nextLine().trim();
        System.out.println("Enter training status:");
        String trainingStatus = scanner.nextLine().trim();
        System.out.println("Is this dog reserved? (true/false):");
        boolean reserved = Boolean.parseBoolean(scanner.nextLine().trim());
        System.out.println("Enter in-service country:");
        String inServiceCountry = scanner.nextLine().trim();

        //Now we are creating a new array in order to house all of this information
        Dog newDog = new Dog(name, breed, gender, age, weight, acquisitionDate, acquisitionCountry, trainingStatus, reserved, inServiceCountry);
        dogInventory.add(newDog);
        System.out.println("New dog added successfully.");
    }

    //Now we do the same thing for Monkey
    //This first part was provided to us
    public static void intakeNewMonkey(Scanner scanner) {
        System.out.println("Enter the monkey's name:");
        String name = scanner.nextLine().trim();

        //Before starting the intake, this checks to see if the name is already in inventory. If it is, the next loop will not occur.
        for (Monkey monkey : monkeyInventory) {
            if (monkey.getName().equalsIgnoreCase(name)) {
                System.out.println("\nThis monkey is already in our system.\n");
                return;
            }
        }
        //Next we verify if the breed that is entered is valid. If not, we also end the intake process here.
        System.out.println("Enter the species (Capuchin, Guenon, Macaque, Marmoset, Squirrel monkey, Tamarin):");
        String species = scanner.nextLine().trim();
        if (!species.equalsIgnoreCase("Capuchin") && !species.equalsIgnoreCase("Guenon") && 
            !species.equalsIgnoreCase("Macaque") && !species.equalsIgnoreCase("Marmoset") && 
            !species.equalsIgnoreCase("Squirrel monkey") && !species.equalsIgnoreCase("Tamarin")) {
            System.out.println("Invalid species. Please enter a valid species.");
            return;
        }

        //Now that it's settled that we can take the monkey, gather all information the same as with dogs.
        System.out.println("Enter the gender (male/female):");
        String gender = scanner.nextLine().trim().toLowerCase();
        System.out.println("Enter the age:");
        String age = scanner.nextLine().trim();
        System.out.println("Enter the weight (in pounds):");
        String weight = scanner.nextLine().trim();
        System.out.println("Enter the acquisition date (MM-DD-YYYY):");
        String acquisitionDate = scanner.nextLine().trim();
        System.out.println("Enter the acquisition country:");
        String acquisitionCountry = scanner.nextLine().trim();
        System.out.println("Enter the training status:");
        String trainingStatus = scanner.nextLine().trim();
        System.out.println("Is the monkey reserved? (true/false):");
        boolean reserved = Boolean.parseBoolean(scanner.nextLine().trim());
        System.out.println("Enter the in-service country:");
        String inServiceCountry = scanner.nextLine().trim();

        //Add to array and to inventory
        Monkey newMonkey = new Monkey(name, species, gender, age, weight, acquisitionDate, acquisitionCountry, trainingStatus, reserved, inServiceCountry);
        monkeyInventory.add(newMonkey);
        System.out.println("New monkey added successfully.");       //Give the user the good news
    }

    // Next we need to reserve the animal.
    public static void reserveAnimal(Scanner scanner) {
        System.out.println("Enter animal type:");           //Ask user for animal type and service country, and read to the variable
        String animalType = scanner.nextLine().trim();
        System.out.println("Enter in-service country:");
        String inServiceCountry = scanner.nextLine().trim();

    //Begin a nested loop which is going to check for animal type and service country, and then reserve it
    //It will check for dogs first, then monkeys, operating the same for both

        if (animalType.equalsIgnoreCase("dog")) {
            for (Dog dog : dogInventory) {
                if (dog.getInServiceLocation().equalsIgnoreCase(inServiceCountry) && !dog.getReserved()) {
                    dog.setReserved(true);
                    System.out.println(dog.getName() + " has been reserved.");
                    return;
                }
            }
        } else if (animalType.equalsIgnoreCase("monkey")) {
            for (Monkey monkey : monkeyInventory) {
                if (monkey.getInServiceLocation().equalsIgnoreCase(inServiceCountry) && !monkey.getReserved()) {
                    monkey.setReserved(true);
                    System.out.println(monkey.getName() + " has been reserved.");
                    return;
                }
            }
    //If neither are entered, the system will ask for a valid option
        } else {
            System.out.println("Invalid animal type. Please enter 'dog' or 'monkey'.");
        }
    //If there are no reservations available, it will produce an error.
        System.out.println("No available " + animalType + " in " + inServiceCountry + ".");
    }

    //Finally we need to output lists of animals based on which options the user chooses
    //We do this in another nested loop, first resolving if the available choice are entered,
    //Then terminating with an error if no valid choice is entered.
    public static void displayAnimals(String type) {
        if (type.equalsIgnoreCase("dog")) {
            System.out.println("List of all dogs:");
            for (Dog dog : dogInventory) {
                System.out.println(dog.getName() + ", Status: " + dog.getTrainingStatus() + ", Location: " + dog.getAcquisitionLocation() + ", Reserved: " + dog.getReserved());
            }
        } else if (type.equalsIgnoreCase("monkey")) {
            System.out.println("List of all monkeys:");
            for (Monkey monkey : monkeyInventory) {
                System.out.println(monkey.getName() + ", Status: " + monkey.getTrainingStatus() + ", Location: " + monkey.getAcquisitionLocation() + ", Reserved: " + monkey.getReserved());
            }
        } else if (type.equalsIgnoreCase("available")) {
            System.out.println("List of all available animals:");
            for (Dog dog : dogInventory) {
                if (dog.getTrainingStatus().equalsIgnoreCase("in service") && !dog.getReserved()) {
                    System.out.println(dog.getName() + ", Status: " + dog.getTrainingStatus() + ", Location: " + dog.getAcquisitionLocation());
                }
            }
            for (Monkey monkey : monkeyInventory) {
                if (monkey.getTrainingStatus().equalsIgnoreCase("in service") && !monkey.getReserved()) {
                    System.out.println(monkey.getName() + ", Status: " + monkey.getTrainingStatus() + ", Location: " + monkey.getAcquisitionLocation());
                }
            }
        } else {
            System.out.println("Invalid option. Please select a valid option.");
        }
    }
}
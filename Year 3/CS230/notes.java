//Using the INSTANCEOF keyword

public class Vehicle {
}

public class TwoWheeled extends Vehicle {
}

public class Bicycle extends TwoWheeled {
}

public class Driver {

    public static void main(String[] args) {

        Bicycle myBike = new Bicycle();

        System.out.println("\nmyBike \"Instance of\" Checks");
        if (myBike instanceof Bicycle)
            System.out.println("Instance of Bicycle: True");
        else
            System.out.println("Instance of Bicycle: False");

        if (myBike instanceof TwoWheeled)
            System.out.println("Instance of TwoWheeled: True");
        else
            System.out.println("Instance of TwoWheeled: False");

        if (myBike instanceof Vehicle)
            System.out.println("Instance of Vehicle: True");
        else
            System.out.println("Instance of Vehicle: False");

        if (myBike instanceof Object)
            System.out.println("Instance of Object: True");
        else
            System.out.println("Instance of Object: False");
    }
}

//Developed OOP Class

public class Bicycle extends TwoWheeled {

    // instance variable declarations
    private int gears = 0;
    private double cost = 0.0;
    private double weight = 0.0;
    private String color = "";

    // method to output Bicycle's information
    public void outputData() {
        System.out.println("\nBicycle Details:");
        System.out.println("Gears  : " + this.gears);
        System.out.println("Cost   : " + this.cost);
        System.out.println("Weight : " + this.weight + " lbs");
        System.out.println("Color  : " + this.color);
    } 

//Setters

public void setGears(int nbr) {
    this.gears = nbr;
    }
   public void setCost(double amt) {
    this.cost = amt;
    }
   public void setWeight(double lbs) {
    this.weight = lbs;
    }
   public void setColor(String theColor) {
    this.color = theColor;
    }
   }

//Drive class; evokes method

public class Driver {

    public static void main(String[] args) {

        Bicycle myBike = new Bicycle();

        myBike.setGears(24);
        myBike.setCost(319.99);
        myBike.setWeight(13.5);
        myBike.setColor("Purple");

        myBike.outputData();
    }
}
public class Monkey extends RescueAnimal {
    //We're creating a new variable used separately from rescueAnimal, so making it private
    private String species;

    //Now making this array of the monkeys information public
    //Defining the array, then initializing
    public Monkey(String name, String species, String gender, String age, String weight, String acquisitionDate, String acquisitionLocation, String trainingStatus, boolean reserved, String inServiceCountry) {
        setName(name);
        setSpecies(species);
        setGender(gender);
        setAge(age);
        setWeight(weight);
        setAcquisitionDate(acquisitionDate);
        setAcquisitionLocation(acquisitionLocation);
        setTrainingStatus(trainingStatus);
        setReserved(reserved);
        setInServiceCountry(inServiceCountry);
    }

    //Finally adding the accessor and mutator methods so that driver.java can access this and use it to set information
    public String getSpecies() {
        return species;
    }

    public void setSpecies(String species) {
        this.species = species;
    }
}
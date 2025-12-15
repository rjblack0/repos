// Contact class represents a single contact record in memory.

public class Contact {
    private final String contactId;
    private String firstName;
    private String lastName;
    private String phone;
    private String address;


    public Contact(String contactId, String firstName, String lastName,             //Constructor for Contact object, enforcing validation rules
                   String phone, String address) {

        if (contactId == null || contactId.length() > 10) {             //contactID is not over 10, not null, not updatable
            throw new IllegalArgumentException("Invalid contactId");
        }

        if (firstName == null || firstName.length() > 10) {             //firstName not over 10, not null
            throw new IllegalArgumentException("Invalid firstName");
        }

        if (lastName == null || lastName.length() > 10) {               //lastName not over 10, not null
            throw new IllegalArgumentException("Invalid lastName");
        }

        if (phone == null || phone.length() != 10 || !phone.matches("\\d{10}")) {   //Exactly 10 digits, not null
            throw new IllegalArgumentException("Invalid phone");
        }

        if (address == null || address.length() > 30) {                 //Address not over 30, not null.
            throw new IllegalArgumentException("Invalid address");
        }

        this.contactId = contactId;                                     //If passed, fields assigned
        this.firstName = firstName;
        this.lastName = lastName;
        this.phone = phone;
        this.address = address;
    }

    public String getContactId() {                                      //contactID getter. No setter, ID cannot be changed.
        return contactId;
    }

    public String getFirstName() {                                      //firstName getter and setter.
        return firstName;
    }
    public void setFirstName(String firstName) {
        if (firstName == null || firstName.length() > 10) {
            throw new IllegalArgumentException("Invalid firstName");
        }
        this.firstName = firstName;
    }
    public String getLastName() {                                       //lastName getter and setter         
        return lastName;
    }
    public void setLastName(String lastName) {
        if (lastName == null || lastName.length() > 10) {
            throw new IllegalArgumentException("Invalid lastName");
        }
        this.lastName = lastName;
    }
    public String getPhone() {                                          //getPhone getter and setter
        return phone;
    }
    public void setPhone(String phone) {
        if (phone == null || phone.length() != 10 || !phone.matches("\\d{10}")) {
            throw new IllegalArgumentException("Invalid phone");
        }
        this.phone = phone;
    }
    public String getAddress() {                                        //Address getter and setter.
        return address;
    }

    public void setAddress(String address) {
        if (address == null || address.length() > 30) {
            throw new IllegalArgumentException("Invalid address");
        }
        this.address = address;
    }
}

import java.util.HashMap;
import java.util.Map;

public class ContactService {               //Class manages Contact objects

    // Internal storage for contacts.
    // The key is the contactId, which must be unique.
    private final Map<String, Contact> contacts = new HashMap<>();      //contactID storage, enforces unique

    public void addContact(String contactId, String firstName, String lastName,     //Add new contact, enforces requirements and checks for duplicates.
                           String phone, String address) {

        if (contacts.containsKey(contactId)) {                                  //duplicate check
            throw new IllegalArgumentException("Contact ID already exists");
        }
        Contact contact = new Contact(contactId, firstName, lastName, phone, address);  //create new contact, validated in constructor
        contacts.put(contactId, contact);       //Store contact in map
    }

    public void deleteContact(String contactId) {                           //Contact deletion function, with error exception
        if (!contacts.containsKey(contactId)) {
            throw new IllegalArgumentException("Contact ID not found");
        }
        contacts.remove(contactId);
    }

    public void updateFirstName(String contactId, String firstName) {       //Update firstName, validated in setter.
        Contact contact = getContact(contactId);
        contact.setFirstName(firstName);
    }

    public void updateLastName(String contactId, String lastName) {         //Update lastName, validated in setter.
        Contact contact = getContact(contactId);
        contact.setLastName(lastName);
    }

    public void updatePhone(String contactId, String phone) {               //update phone number
        Contact contact = getContact(contactId);
        contact.setPhone(phone);
    }

    public void updateAddress(String contactId, String address) {           //update address
        Contact contact = getContact(contactId);
        contact.setAddress(address);
    }

    private Contact getContact(String contactId) {                      //Retrieve contact by ID, with error handling
        Contact contact = contacts.get(contactId);
        if (contact == null) {
            throw new IllegalArgumentException("Contact ID not found");
        }
        return contact;
    }

    public Contact getContactForTest(String contactId) {                //verification, ContactService is storing correct
        return contacts.get(contactId);
    }
}

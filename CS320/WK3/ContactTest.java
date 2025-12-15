package cs320_Project_Milestone_Ryan_Blackburn_v2;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class ContactTest {

    @Test
    void testValidContactCreation() {                              //Test Happy Path
        Contact contact = new Contact("12345", "John", "Doe",
                                      "1234567890", "123 Main Street");

        assertEquals("12345", contact.getContactId());
        assertEquals("John", contact.getFirstName());
        assertEquals("Doe", contact.getLastName());
        assertEquals("1234567890", contact.getPhone());
        assertEquals("123 Main Street", contact.getAddress());
    }

    // === Constructor validation tests ===

    @Test
    void testContactIdNull() {                                     //Invalid: null ID
        assertThrows(IllegalArgumentException.class, () -> {
            new Contact(null, "John", "Doe",
                        "1234567890", "123 Main Street");
        });
    }

    @Test
    void testContactIdTooLong() {                                  //Invalid: ID > 10 chars
        String longId = "12345678901";                             //11 characters
        assertTrue(longId.length() > 10);

        assertThrows(IllegalArgumentException.class, () -> {
            new Contact(longId, "John", "Doe",
                        "1234567890", "123 Main Street");
        });
    }

    @Test
    void testFirstNameNull() {                                     //Invalid: null firstName
        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("12345", null, "Doe",
                        "1234567890", "123 Main Street");
        });
    }

    @Test
    void testFirstNameTooLong() {                                  //Invalid: firstName > 10
        String longName = "LongFirstName";
        assertTrue(longName.length() > 10);

        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("12345", longName, "Doe",
                        "1234567890", "123 Main Street");
        });
    }

    @Test
    void testLastNameNull() {                                      //Invalid: null lastName
        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("12345", "John", null,
                        "1234567890", "123 Main Street");
        });
    }

    @Test
    void testLastNameTooLong() {                                   //Invalid: lastName > 10
        String longName = "LongLastName";
        assertTrue(longName.length() > 10);

        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("12345", "John", longName,
                        "1234567890", "123 Main Street");
        });
    }

    @Test
    void testPhoneNull() {                                         //Invalid: null phone
        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("12345", "John", "Doe",
                        null, "123 Main Street");
        });
    }

    @Test
    void testPhoneWrongLength() {                                  //Invalid: phone != 10 digits
        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("12345", "John", "Doe",
                        "123456789", "123 Main Street");           //9 digits
        });
    }

    @Test
    void testPhoneNonDigits() {                                    //Invalid: phone has non-digits
        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("12345", "John", "Doe",
                        "12345abcde", "123 Main Street");
        });
    }

    @Test
    void testAddressNull() {                                       //Invalid: null address
        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("12345", "John", "Doe",
                        "1234567890", null);
        });
    }

    @Test
    void testAddressTooLong() {                                    //Invalid: address > 30 chars
        String longAddress = "123 This Address Is Way Too Long For The Rule";
        assertTrue(longAddress.length() > 30);

        assertThrows(IllegalArgumentException.class, () -> {
            new Contact("12345", "John", "Doe",
                        "1234567890", longAddress);
        });
    }

    // === Setter validation tests ===

    @Test
    void testSetFirstNameValid() {                                 //Valid firstName update
        Contact contact = new Contact("12345", "John", "Doe",
                                      "1234567890", "123 Main Street");

        contact.setFirstName("James");
        assertEquals("James", contact.getFirstName());
    }

    @Test
    void testSetFirstNameNull() {                                  //Invalid: null firstName in setter
        Contact contact = new Contact("12345", "John", "Doe",
                                      "1234567890", "123 Main Street");

        assertThrows(IllegalArgumentException.class, () -> {
            contact.setFirstName(null);
        });
    }

    @Test
    void testSetFirstNameTooLong() {                               //Invalid: firstName > 10 in setter
        Contact contact = new Contact("12345", "John", "Doe",
                                      "1234567890", "123 Main Street");

        String longName = "LongFirstName";
        assertTrue(longName.length() > 10);

        assertThrows(IllegalArgumentException.class, () -> {
            contact.setFirstName(longName);
        });
    }

    @Test
    void testSetLastNameValid() {                                  //Valid lastName update
        Contact contact = new Contact("12345", "John", "Doe",
                                      "1234567890", "123 Main Street");

        contact.setLastName("Smith");
        assertEquals("Smith", contact.getLastName());
    }

    @Test
    void testSetLastNameNull() {                                   //Invalid: null lastName in setter
        Contact contact = new Contact("12345", "John", "Doe",
                                      "1234567890", "123 Main Street");

        assertThrows(IllegalArgumentException.class, () -> {
            contact.setLastName(null);
        });
    }

    @Test
    void testSetLastNameTooLong() {                                //Invalid: lastName > 10 in setter
        Contact contact = new Contact("12345", "John", "Doe",
                                      "1234567890", "123 Main Street");

        String longName = "LongLastName";
        assertTrue(longName.length() > 10);

        assertThrows(IllegalArgumentException.class, () -> {
            contact.setLastName(longName);
        });
    }

    @Test
    void testSetPhoneValid() {                                     //Valid phone update
        Contact contact = new Contact("12345", "John", "Doe",
                                      "1234567890", "123 Main Street");

        contact.setPhone("0987654321");
        assertEquals("0987654321", contact.getPhone());
    }

    @Test
    void testSetPhoneNull() {                                      //Invalid: null phone in setter
        Contact contact = new Contact("12345", "John", "Doe",
                                      "1234567890", "123 Main Street");

        assertThrows(IllegalArgumentException.class, () -> {
            contact.setPhone(null);
        });
    }

    @Test
    void testSetPhoneWrongLength() {                               //Invalid: phone wrong length in setter
        Contact contact = new Contact("12345", "John", "Doe",
                                      "1234567890", "123 Main Street");

        assertThrows(IllegalArgumentException.class, () -> {
            contact.setPhone("123456789");                          //9 digits
        });
    }

    @Test
    void testSetPhoneNonDigits() {                                 //Invalid: non-digits in phone setter
        Contact contact = new Contact("12345", "John", "Doe",
                                      "1234567890", "123 Main Street");

        assertThrows(IllegalArgumentException.class, () -> {
            contact.setPhone("12345abcde");
        });
    }

    @Test
    void testSetAddressValid() {                                   //Valid address update
        Contact contact = new Contact("12345", "John", "Doe",
                                      "1234567890", "123 Main Street");

        contact.setAddress("456 Oak Avenue");
        assertEquals("456 Oak Avenue", contact.getAddress());
    }

    @Test
    void testSetAddressNull() {                                    //Invalid: null address in setter
        Contact contact = new Contact("12345", "John", "Doe",
                                      "1234567890", "123 Main Street");

        assertThrows(IllegalArgumentException.class, () -> {
            contact.setAddress(null);
        });
    }

    @Test
    void testSetAddressTooLong() {                                 //Invalid: address > 30 in setter
        Contact contact = new Contact("12345", "John", "Doe",
                                      "1234567890", "123 Main Street");

        String longAddress = "123 This Address Is Way Too Long For The Rule";
        assertTrue(longAddress.length() > 30);

        assertThrows(IllegalArgumentException.class, () -> {
            contact.setAddress(longAddress);
        });
    }
}

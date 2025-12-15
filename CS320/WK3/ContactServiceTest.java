package cs320_Project_Milestone_Ryan_Blackburn_v2;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class ContactServiceTest {                          //ContactService tests

    private ContactService service;

    @BeforeEach
    void setUp() {                                         //Initialize service
        service = new ContactService();
    }

    @Test
    void testAddContactSuccess() {                         //Test adding contact
        service.addContact("1", "John", "Doe",
                           "1234567890", "123 Main Street");

        Contact contact = service.getContactForTest("1");
        assertNotNull(contact);
        assertEquals("John", contact.getFirstName());
        assertEquals("Doe", contact.getLastName());
        assertEquals("1234567890", contact.getPhone());
        assertEquals("123 Main Street", contact.getAddress());
    }

    @Test
    void testAddDuplicateContactThrowsException() {        //Test duplicate ID
        service.addContact("1", "John", "Doe",
                           "1234567890", "123 Main Street");

        assertThrows(IllegalArgumentException.class, () -> {
            service.addContact("1", "Jane", "Smith",
                               "0987654321", "456 Oak Avenue");
        });
    }

    @Test
    void testDeleteContactSuccess() {                      //Test deleting contact
        service.addContact("1", "John", "Doe",
                           "1234567890", "123 Main Street");

        service.deleteContact("1");

        Contact contact = service.getContactForTest("1");
        assertNull(contact);
    }

    @Test
    void testDeleteNonExistingContactThrowsException() {   //Test delete non-existing
        assertThrows(IllegalArgumentException.class, () -> {
            service.deleteContact("999");
        });
    }

    @Test
    void testUpdateFirstName() {                           //Test firstName update
        service.addContact("1", "John", "Doe",
                           "1234567890", "123 Main Street");

        service.updateFirstName("1", "James");

        Contact contact = service.getContactForTest("1");
        assertEquals("James", contact.getFirstName());
    }

    @Test
    void testUpdateLastName() {                            //Test lastName update
        service.addContact("1", "John", "Doe",
                           "1234567890", "123 Main Street");

        service.updateLastName("1", "Smith");

        Contact contact = service.getContactForTest("1");
        assertEquals("Smith", contact.getLastName());
    }

    @Test
    void testUpdatePhone() {                               //Test phone update
        service.addContact("1", "John", "Doe",
                           "1234567890", "123 Main Street");

        service.updatePhone("1", "0987654321");

        Contact contact = service.getContactForTest("1");
        assertEquals("0987654321", contact.getPhone());
    }

    @Test
    void testUpdateAddress() {                             //Test address update
        service.addContact("1", "John", "Doe",
                           "1234567890", "123 Main Street");

        service.updateAddress("1", "456 Oak Avenue");

        Contact contact = service.getContactForTest("1");
        assertEquals("456 Oak Avenue", contact.getAddress());
    }

    @Test
    void testUpdateNonExistingContactThrowsException() {   //Test update non-existing
        assertThrows(IllegalArgumentException.class, () -> {
            service.updateFirstName("999", "NewName");
        });
    }
}

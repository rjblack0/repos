package cs320_Project_Milestone_Ryan_Blackburn_v2;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class TaskTest {

    @Test
    void testValidTaskCreation() {                                   //Valid constructor
        Task task = new Task("T001", "Do Homework",
                             "Complete CS-320 milestone");

        assertEquals("T001", task.getTaskId());
        assertEquals("Do Homework", task.getName());
        assertEquals("Complete CS-320 milestone", task.getDescription());
    }

    @Test
    void testTaskIdNull() {                                          //Null ID
        assertThrows(IllegalArgumentException.class, () -> {
            new Task(null, "Do Homework", "Description");
        });
    }

    @Test
    void testTaskIdTooLong() {                                       //Too-long ID
        String longId = "12345678901";                               //11 characters
        assertTrue(longId.length() > 10);

        assertThrows(IllegalArgumentException.class, () -> {
            new Task(longId, "Do Homework", "Description");
        });
    }

    @Test
    void testNameNull() {                                            //Null name
        assertThrows(IllegalArgumentException.class, () -> {
            new Task("T001", null, "Description");
        });
    }

    @Test
    void testNameTooLong() {                                         //Too-long name
        String longName = "This name is definitely too long";
        assertTrue(longName.length() > 20);

        assertThrows(IllegalArgumentException.class, () -> {
            new Task("T001", longName, "Description");
        });
    }

    @Test
    void testDescriptionNull() {                                     //Null description
        assertThrows(IllegalArgumentException.class, () -> {
            new Task("T001", "Do Homework", null);
        });
    }

    @Test
    void testDescriptionTooLong() {                                  //Too-long description
        String longDescription = "This description is going to exceed fifty "
                + "characters so that it triggers the rule.";
        assertTrue(longDescription.length() > 50);

        assertThrows(IllegalArgumentException.class, () -> {
            new Task("T001", "Do Homework", longDescription);
        });
    }

    // === Setter tests for extra coverage ===

    @Test
    void testSetNameValid() {                                        //Valid name update
        Task task = new Task("T001", "Do Homework",
                             "Complete CS-320 milestone");

        task.setName("Do Laundry");
        assertEquals("Do Laundry", task.getName());
    }

    @Test
    void testSetNameNull() {                                         //Null in setName
        Task task = new Task("T001", "Do Homework",
                             "Complete CS-320 milestone");

        assertThrows(IllegalArgumentException.class, () -> {
            task.setName(null);
        });
    }

    @Test
    void testSetNameTooLong() {                                      //Too-long name in setName
        Task task = new Task("T001", "Do Homework",
                             "Complete CS-320 milestone");

        String longName = "Another name that is way too long";
        assertTrue(longName.length() > 20);

        assertThrows(IllegalArgumentException.class, () -> {
            task.setName(longName);
        });
    }

    @Test
    void testSetDescriptionValid() {                                 //Valid description update
        Task task = new Task("T001", "Do Homework",
                             "Complete CS-320 milestone");

        task.setDescription("Updated description for this task");
        assertEquals("Updated description for this task",
                     task.getDescription());
    }

    @Test
    void testSetDescriptionNull() {                                  //Null in setDescription
        Task task = new Task("T001", "Do Homework",
                             "Complete CS-320 milestone");

        assertThrows(IllegalArgumentException.class, () -> {
            task.setDescription(null);
        });
    }

    @Test
    void testSetDescriptionTooLong() {                               //Too-long description in setDescription
        Task task = new Task("T001", "Do Homework",
                             "Complete CS-320 milestone");

        String longDescription = "This description is again going to exceed "
                + "the fifty character limit for tasks.";
        assertTrue(longDescription.length() > 50);

        assertThrows(IllegalArgumentException.class, () -> {
            task.setDescription(longDescription);
        });
    }
}

package cs320_Project_Milestone_Ryan_Blackburn_v2;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class TaskServiceTest {

    private TaskService taskService;

    @BeforeEach
    void setUp() {                                                   //Initialize service
        taskService = new TaskService();
    }

    @Test
    void testAddTaskValid() {                                        //Valid add
        taskService.addTask("T001", "Do Homework",
                            "Complete CS-320 milestone");

        Task task = taskService.getTaskForTest("T001");
        assertNotNull(task);
        assertEquals("T001", task.getTaskId());
        assertEquals("Do Homework", task.getName());
    }

    @Test
    void testAddTaskNullIdThrowsException() {                        //Null ID in add
        assertThrows(IllegalArgumentException.class, () -> {
            taskService.addTask(null, "Do Homework",
                                "Complete CS-320 milestone");
        });
    }

    @Test
    void testAddDuplicateTaskThrowsException() {                     //Duplicate ID in add
        taskService.addTask("T001", "Do Homework",
                            "Complete CS-320 milestone");

        assertThrows(IllegalArgumentException.class, () -> {
            taskService.addTask("T001", "Another Task",
                                "Different description");
        });
    }

    @Test
    void testDeleteTaskValid() {                                     //Valid delete
        taskService.addTask("T001", "Do Homework",
                            "Complete CS-320 milestone");

        taskService.deleteTask("T001");

        Task task = taskService.getTaskForTest("T001");
        assertNull(task);
    }

    @Test
    void testDeleteNonexistentTaskThrowsException() {                //Delete non-existing ID
        assertThrows(IllegalArgumentException.class, () -> {
            taskService.deleteTask("DOES_NOT_EXIST");
        });
    }

    @Test
    void testDeleteTaskNullIdThrowsException() {                     //Null ID in delete
        assertThrows(IllegalArgumentException.class, () -> {
            taskService.deleteTask(null);
        });
    }

    @Test
    void testUpdateNameValid() {                                     //Valid name update
        taskService.addTask("T001", "Do Homework",
                            "Complete CS-320 milestone");

        taskService.updateName("T001", "Do Laundry");

        Task task = taskService.getTaskForTest("T001");
        assertEquals("Do Laundry", task.getName());
    }

    @Test
    void testUpdateDescriptionValid() {                              //Valid description update
        taskService.addTask("T001", "Do Homework",
                            "Complete CS-320 milestone");

        taskService.updateDescription("T001",
                                      "Updated description for this task");

        Task task = taskService.getTaskForTest("T001");
        assertEquals("Updated description for this task",
                     task.getDescription());
    }

    @Test
    void testUpdateNameNonExistingTaskThrowsException() {            //Update name on non-existing task
        assertThrows(IllegalArgumentException.class, () -> {
            taskService.updateName("DOES_NOT_EXIST", "New Name");
        });
    }

    @Test
    void testUpdateDescriptionNonExistingTaskThrowsException() {     //Update description on non-existing task
        assertThrows(IllegalArgumentException.class, () -> {
            taskService.updateDescription("DOES_NOT_EXIST",
                                          "New Description");
        });
    }
}

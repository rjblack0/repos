import java.util.HashMap;
import java.util.Map;

public class TaskService {                 //Class for Task objects, key is TaskId; must be unique

    private final Map<String, Task> tasks = new HashMap<>();    //taskId storage
    public void addTask(String taskId, String name, String description) {   //Add new task, enforces requirements and checks for duplicates.
        if (tasks.containsKey(taskId)) {                                   //duplicate check
            throw new IllegalArgumentException("Task ID already exists");
        }

        Task task = new Task(taskId, name, description);                   //create new task, validated in constructor
        tasks.put(taskId, task);
    }

    public void deleteTask(String taskId) {                                //Task deletion function, handles error exceptions
        if (!tasks.containsKey(taskId)) {
            throw new IllegalArgumentException("Task ID not found");
        }
        tasks.remove(taskId);
    }

    public void updateName(String taskId, String name) {                   //Update task name
        Task task = getTask(taskId);
        task.setName(name);
    }

    public void updateDescription(String taskId, String description) {     //Update task description
        Task task = getTask(taskId);
        task.setDescription(description);
    }

    private Task getTask(String taskId) {                                  //Retrieve task by ID, with error handling,
        Task task = tasks.get(taskId);
        if (task == null) {
            throw new IllegalArgumentException("Task ID not found");
        }
        return task;
    }

    public Task getTaskForTest(String taskId) {         //verification, TaskService is storing correct
        return tasks.get(taskId);
    }
}

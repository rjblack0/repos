public class Task {
    private final String taskId;
    private String name;
    private String description;

    public Task(String taskId, String name, String description) {   //Constructor for Task object, enforcing validation rules

        if (taskId == null || taskId.length() > 10) {               //taskId not over 10, not null
            throw new IllegalArgumentException("Invalid taskId");
        }

        if (name == null || name.length() > 20) {                   //name not over 20, not null
            throw new IllegalArgumentException("Invalid name");
        }
        if (description == null || description.length() > 50) {         //description not over 50, not null
            throw new IllegalArgumentException("Invalid description");
        }

        this.taskId = taskId;                   //If passed, fields get assigned
        this.name = name;
        this.description = description;
    }

    public String getTaskId() {                 //taskId getter. No setter, ID cannot be changed.
        return taskId;
    }

    public String getName() {                   //name getter and setter.
        return name;
    }

    public void setName(String name) {                              //validator
        if (name == null || name.length() > 20) {
            throw new IllegalArgumentException("Invalid name");
        }
        this.name = name;
    }

    public String getDescription() {                          //description getter and setter.
        return description;
    }

    public void setDescription(String description) {
        if (description == null || description.length() > 50) {         //validator for updates
            throw new IllegalArgumentException("Invalid description");
        }
        this.description = description;
    }
}

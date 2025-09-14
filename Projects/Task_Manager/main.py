from tasks import add_task, view_tasks, update_task, delete_task
from notifications import schedule_task_reminder
from database import create_tables  # Import create_tables to initialize the database

def main():
    # Initialize the database and tables
    create_tables()

    while True:
        choice = input("1. Add Task\n2. View Tasks\n3. Update Task\n4. Delete Task\n5. Exit\nChoose an option: ")
        
        if choice == '1':
            title = input("Task title: ")
            description = input("Task description: ")
            due_date = input("Due date (YYYY-MM-DD HH:MM:SS): ")
            priority = input("Priority (low, medium, high): ")
            add_task(title, description, due_date, priority)
            schedule_task_reminder(1, title, due_date)
        
        elif choice == '2':
            tasks = view_tasks()
            for task in tasks:
                print(task)
        
        elif choice == '3':
            task_id = int(input("Task ID to update: "))
            title = input("New title (or leave blank): ")
            description = input("New description (or leave blank): ")
            due_date = input("New due date (YYYY-MM-DD HH:MM:SS) (or leave blank): ")
            priority = input("New priority (low, medium, high) (or leave blank): ")
            update_task(task_id, title, description, due_date, priority)
        
        elif choice == '4':
            task_id = int(input("Task ID to delete: "))
            delete_task(task_id)
        
        elif choice == '5':
            break

if __name__ == "__main__":
    main()

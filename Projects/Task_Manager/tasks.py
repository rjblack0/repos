#Task Management Logic

from database import connect_db

def add_task(title, description, due_date, priority):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO tasks (title, description, due_date, priority)
                      VALUES (?, ?, ?, ?)''', (title, description, due_date, priority))
    
    conn.commit()
    conn.close()
    print(f"Task '{title}' added successfully!")

def view_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    
    conn.close()
    
    return tasks

def update_task(task_id, title=None, description=None, due_date=None, priority=None):
    conn = connect_db()
    cursor = conn.cursor()
    
    if title:
        cursor.execute('UPDATE tasks SET title = ? WHERE id = ?', (title, task_id))
    if description:
        cursor.execute('UPDATE tasks SET description = ? WHERE id = ?', (description, task_id))
    if due_date:
        cursor.execute('UPDATE tasks SET due_date = ? WHERE id = ?', (due_date, task_id))
    if priority:
        cursor.execute('UPDATE tasks SET priority = ? WHERE id = ?', (priority, task_id))
    
    conn.commit()
    conn.close()
    print(f"Task {task_id} updated successfully!")

def delete_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    print(f"Task {task_id} deleted successfully!")

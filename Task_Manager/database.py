import sqlite3

def connect_db():
    # Connect to the SQLite database (or create it if it doesn’t exist)
    conn = sqlite3.connect('task_manager.db')
    return conn

def create_tables():
    # Create the tasks table if it doesn't exist
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT,
                        due_date TEXT,
                        priority TEXT,
                        status TEXT DEFAULT 'pending'
                      )''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()

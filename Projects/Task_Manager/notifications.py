from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

# Create and start the scheduler (this runs in the background)
scheduler = BackgroundScheduler()
scheduler.start()

def schedule_task_reminder(task_id, title, due_date):
    # Convert due_date to a datetime object
    due_datetime = datetime.strptime(due_date, '%Y-%m-%d %H:%M:%S')
    
    # Schedule a reminder 10 minutes before the task is due
    reminder_time = due_datetime - timedelta(minutes=10)
    
    scheduler.add_job(func=remind_task, trigger='date', run_date=reminder_time, args=[task_id, title])
    print(f"Reminder set for task '{title}' at {reminder_time}")

def remind_task(task_id, title):
    # Function to send a notification
    print(f"Reminder: Task '{title}' is due soon!")

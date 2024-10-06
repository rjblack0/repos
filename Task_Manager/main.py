import os

# Debugging: Check the current working directory and ensure it's correct
print(f"Current Working Directory: {os.getcwd()}")

# More Debugging: Check if the script is being executed
print("Starting script execution...")

try:
    print("Hello World")
    
    from apscheduler.schedulers.background import BackgroundScheduler
    import plyer

    print("Libraries imported successfully!")
except Exception as e:
    print(f"Error occurred: {e}")
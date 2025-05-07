import json
import os
from datetime import datetime

TASK_FILE = "tasks.json"

# Load existing tasks or create an empty list
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task():
    task_name = input("Enter task name: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks = load_tasks()
    tasks.append({"task": task_name, "due": due_date})
    save_tasks(tasks)
    print("✅ Task added!\n")

# Show tasks due today
def show_today_tasks():
    today = datetime.today().strftime("%Y-%m-%d")
    tasks = load_tasks()
    print(f"\n📅 Tasks due today ({today}):")
    found = False
    for task in tasks:
        if task["due"] == today:
            print("🔔", task["task"])
            found = True
    if not found:
        print("No tasks due today.\n")

# Main menu loop
def main():
    while True:
        print("\n📌 Simple Reminder Bot")
        print("1. Add Task")
        print("2. Show Today's Tasks")
        print("3. Exit")
        choice = input("Choose an option (1, 2, or 3): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_today_tasks()
        elif choice == "3":
            print("👋 Exiting. Have a nice day!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

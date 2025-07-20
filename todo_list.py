import json
import os

TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found.\n")
        return
    print("\n📝 Your Tasks:")
    for idx, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}. {task['task']} [{status}]")
    print()

def add_task(tasks):
    new_task = input("Enter your new task: ")
    tasks.append({"task": new_task, "done": False})
    save_tasks(tasks)
    print("✅ Task added successfully!")

def mark_done(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as done: "))
        tasks[task_num - 1]["done"] = True
        save_tasks(tasks)
        print("🎉 Task marked as done!")
    except (ValueError, IndexError):
        print("⚠️ Invalid task number.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"🗑️ Task '{removed['task']}' deleted.")
    except (ValueError, IndexError):
        print("⚠️ Invalid task number.")

def todo_menu():
    tasks = load_tasks()
    while True:
        print("\n📌 TO-DO LIST MENU")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("👋 Exiting To-Do List App!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Start the app
if __name__ == "__main__":
    todo_menu()

#To do list with Hashing
#Hash table to store values
# To-Do List with Hashing (Python Dictionary)
tasks = {}

# Function to add a task
def add_task(task_name):
    if task_name in tasks:
        print(f"'{task_name}' already exists.")
    else:
        tasks[task_name] = "Pending"
        print(f"Task '{task_name}' added successfully!")

# Function to mark a task as done
def mark_done(task_name):
    if task_name in tasks:
        tasks[task_name] = "Done"
        print(f"Task '{task_name}' marked as Done!")
    else:
        print(f"Task '{task_name}' not found.")

# Function to delete a task
def delete_task(task_name):
    if task_name in tasks:
        del tasks[task_name]
        print(f"Task '{task_name}' deleted successfully!")
    else:
        print(f"Task '{task_name}' not found.")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\n--- To-Do List ---")
        for task, status in tasks.items():
            print(f"{task} --> {status}")
        print("------------------")

# Main program loop
while True:
    print("\n1. Add Task")
    print("2. Mark Task as Done")
    print("3. Delete Task")
    print("4. View Tasks")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        task = input("Enter task name: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter task name to mark as done: ")
        mark_done(task)
    elif choice == "3":
        task = input("Enter task name to delete: ")
        delete_task(task)
    elif choice == "4":
        view_tasks()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

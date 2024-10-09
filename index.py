import json

# Define the Task class
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

# Function to load tasks from a JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
        return
    for i, task in enumerate(tasks):
        status = 'Completed' if task.completed else 'Pending'
        print(f"{i + 1}. {task.title} [{task.category}] - {status}")

# Main function to interact with the user
def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category (e.g., Work, Personal, Urgent): ")
            tasks.append(Task(title, description, category))

        elif choice == '2':
            display_tasks(tasks)

        elif choice == '3':
            display_tasks(tasks)
            task_num = int(input("Enter task number to mark completed: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num].mark_completed()

        elif choice == '4':
            display_tasks(tasks)
            task_num = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_num < len(tasks):
                del tasks[task_num]

        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
tasks = []

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

def add_task():
    task_description = input("Enter task description: ")
    tasks.append(task_description)
    print("Task added successfully!")

def view_tasks():
    print("\n--- Tasks ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def mark_completed():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            completed_task = tasks.pop(task_index)
            print(f"Task '{completed_task}' marked as completed.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            print("Exiting the program. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()












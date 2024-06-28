def display_menu():
    print("\nTask Manager")
    print("1. Add a task")
    print("2. Complete a task")
    print("3. Remove a task")
    print("4. Show all tasks")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f'Task "{task}" added.')

def complete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the number of the task to mark as complete: ")) - 1
            if 0 <= task_number < len(tasks):
                tasks[task_number]["completed"] = True
                print(f'Task "{tasks[task_number]["task"]}" marked as complete.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def remove_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the number of the task to remove: ")) - 1
            if 0 <= task_number < len(tasks):
                removed_task = tasks.pop(task_number)
                print(f'Task "{removed_task["task"]}" removed.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Incomplete"
            print(f'{i}. {task["task"]} - {status}')

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            complete_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            show_tasks(tasks)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()

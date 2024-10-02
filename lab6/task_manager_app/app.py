# A list to store tasks, where each task is represented as a dictionary with keys 'name' and 'done'
tasks = []


# Function to display the list of tasks
def show_tasks():
    # If the list is empty, print a message that no tasks are available
    if not tasks:
        print("Список завдань порожній.")
    else:
        # Loop through the tasks and display their index, name, and status (done or not done)
        for i, task in enumerate(tasks, 1):
            # Mark the task as done with [✓] or not done with [✗]
            status = "[✓]" if task['done'] else "[✗]"
            print(f"{i}. {task['name']} {status}")


# Function to add a new task to the task list
def add_task():
    # Ask the user for a task name
    task_name = input("Введіть назву завдання: ")
    # Append a new dictionary representing the task to the 'tasks' list, initially marked as not done
    tasks.append({"name": task_name, "done": False})


# Function to edit an existing task's name
def edit_task():
    # Show the current list of tasks
    show_tasks()
    try:
        # Ask the user which task number they want to edit
        task_number = int(input("Введіть номер завдання для редагування: "))
        # Check if the entered number is valid (within the range of the task list)
        if 1 <= task_number <= len(tasks):
            # Ask the user for a new name for the task
            new_name = input("Введіть нову назву завдання: ")
            # Update the task name in the list
            tasks[task_number - 1]["name"] = new_name
        else:
            print("Неправильний номер завдання.")
    except ValueError:
        # Handle invalid input (e.g., when the user enters a non-numeric value)
        print("Будь ласка, введіть число.")


# Function to delete a task from the task list
def delete_task():
    # Show the current list of tasks
    show_tasks()
    try:
        # Ask the user which task number they want to delete
        task_number = int(input("Введіть номер завдання для видалення: "))
        # Check if the entered number is valid
        if 1 <= task_number <= len(tasks):
            # Remove the task from the list
            tasks.pop(task_number - 1)
        else:
            print("Неправильний номер завдання.")
    except ValueError:
        # Handle invalid input
        print("Будь ласка, введіть число.")


# Function to mark a task as done
def mark_task_done():
    # Show the current list of tasks
    show_tasks()
    try:
        # Ask the user which task number they want to mark as done
        task_number = int(input("Введіть номер завдання для позначення як виконане: "))
        # Check if the entered number is valid
        if 1 <= task_number <= len(tasks):
            # Mark the task as done by setting the 'done' key to True
            tasks[task_number - 1]["done"] = True
        else:
            print("Неправильний номер завдання.")
    except ValueError:
        # Handle invalid input
        print("Будь ласка, введіть число.")


# Main function that contains the program loop
def main():
    # Infinite loop to keep the program running until the user chooses to exit
    while True:
        # Display the menu of options
        print("\n1. Додати завдання")
        print("2. Переглянути завдання")
        print("3. Відредагувати завдання")
        print("4. Видалити завдання")
        print("5. Позначити як виконане")
        print("6. Вийти")

        # Ask the user to choose an action by entering a number
        action = input("Виберіть дію: ")

        # Perform the corresponding action based on the user's input
        if action == '1':
            add_task()  # Add a new task
        elif action == '2':
            show_tasks()  # Display the list of tasks
        elif action == '3':
            edit_task()  # Edit an existing task
        elif action == '4':
            delete_task()  # Delete a task
        elif action == '5':
            mark_task_done()  # Mark a task as done
        elif action == '6':
            # Exit the program
            print("Вихід з програми.")
            break
        else:
            # If the user enters an invalid option, display an error message
            print("Невідома дія, спробуйте ще раз.")


# If this script is executed directly (not imported), run the main function
if __name__ == "__main__":
    main()
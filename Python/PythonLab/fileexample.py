import os

def add_task(filename):
    task = input("Enter task to add: ")
    with open(filename, "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

def view_tasks(filename):
    if not os.path.exists(filename):
        print("No tasks found. Add some tasks first.")
        return
    with open(filename, "r") as file:
        tasks = file.readlines()
        if not tasks:
             print("No tasks found. Add some tasks first.")
             return
        print("\n--- To-Do List ---")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task.strip()}")

def remove_task(filename):
     view_tasks(filename)
     if not os.path.exists(filename):
          return
     with open(filename, "r") as file:
          tasks = file.readlines()
     if not tasks:
          return
     while True:
        try:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                break
            else:
                print("Invalid task number. Please enter a number within the valid range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

     removed_task = tasks.pop(task_number - 1).strip()
     with open(filename, "w") as file:
          file.writelines(tasks)
     print(f"Task '{removed_task}' removed successfully!")

def main():
    filename = "tasks.txt"
    while True:
        print("\n--- Menu ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(filename)
        elif choice == "2":
            view_tasks(filename)
        elif choice == "3":
            remove_task(filename)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})

def edit_task(index, new_task):
    if 0 <= index < len(tasks):
        tasks[index]["task"] = new_task

def remove_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]

def mark_as_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

def display_tasks():
    for index, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index+1}. {task['task']} - {status}")

while True:
    print("Todo List App")
    print("1. Add task")
    print("2. Edit task")
    print("3. Remove task")
    print("4. Mark task as done")
    print("5. Display tasks")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task: ")
        add_task(task)
    elif choice == 2:
        index = int(input("Enter index of task to edit: ")) - 1
        new_task = input("Enter new task: ")
        edit_task(index, new_task)
    elif choice == 3:
        index = int(input("Enter index of task to remove: ")) - 1
        remove_task(index)
    elif choice == 4:
        index = int(input("Enter index of task to mark as done: ")) - 1
        mark_as_done(index)
    elif choice == 5:
        display_tasks()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please enter a valid option.")

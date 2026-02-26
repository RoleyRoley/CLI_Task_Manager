# Command line task management tool

tasks = []

def create_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks.append({"title": title, "description": description})
    print("Task created successfully!")
    




while True:
    print("Welcome to the Task Manager!\n1. Create Task\n2. View Tasks\n3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        create_task()
    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for id, task in enumerate(tasks, start=1):
                print(f"\n{id}. {task['title']}: {task['description']}\n")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
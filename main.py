# Command line task management tool

tasks = []

def create_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks.append({"title": title, "description": description})
    print("Task created successfully!")
    
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\n==== Task List ====")
        
        for id, task in enumerate(tasks, start=1):
            print(f"\n{id}. {task['title']}: {task['description']}\n")
        
        print("===================")
            
def mark_task_completed():
    view_tasks()
    task_id = int(input("Enter the task # to mark as completed: "))
    if 1 <= task_id <= len(tasks):
        tasks.pop(task_id - 1)
        print("\nTask marked as completed and removed from the list.")
    else:
        print("Invalid task ID.")
    




while True:
    print("\n\n============================\nWelcome to the Task Manager!\n============================\n1. Create Task\n2. View Tasks\n3. Mark Task as Completed\n4. Exit\n============================")
    choice = input("Enter your choice: ")
    if choice == "1":
        create_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_completed()
    elif choice == "4":
        print("Exiting the Task Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
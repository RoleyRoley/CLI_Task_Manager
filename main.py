# Command line task management tool
import sqlite3
from pathlib import Path

DB_PATH = Path("data/tasks.db")


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)


def initialize_database():
    with get_connection() as con:
        con.execute(
            """CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0,
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        )"""
        )

        existing_columns = {
            row[1] for row in con.execute("PRAGMA table_info(tasks)").fetchall()
        }
        if "description" not in existing_columns:
            con.execute("ALTER TABLE tasks ADD COLUMN description TEXT NOT NULL DEFAULT ''")


def create_task():
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    with get_connection() as con:
        con.execute(
            "INSERT INTO tasks (title, description) VALUES (?, ?)",
            (title, description),
        )

    print("Task created successfully!")


def get_active_tasks():
    with get_connection() as con:
        return con.execute(
            "SELECT id, title, description FROM tasks WHERE completed = 0 ORDER BY id"
        ).fetchall()


def view_tasks():
    tasks = get_active_tasks()

    if not tasks:
        print("No tasks available.")
        return

    print("\n==== Task List ====")
    for index, task in enumerate(tasks, start=1):
        _, title, description = task
        print(f"\n{index}. {title}: {description}\n")
    print("===================")


def mark_task_completed():
    tasks = get_active_tasks()
    if not tasks:
        print("No tasks available.")
        return

    view_tasks()

    try:
        task_number = int(input("Enter the task # to mark as completed: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if not (1 <= task_number <= len(tasks)):
        print("Invalid task ID.")
        return

    task_id, title, _ = tasks[task_number - 1]
    with get_connection() as con:
        con.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))

    print(f"\nTask: {title} marked as completed and removed from the list.")


def main():
    initialize_database()

    while True:
        print(
            "\n\n============================\n"
            "Welcome to the Task Manager!\n"
            "============================\n"
            "1. Create Task\n"
            "2. View Tasks\n"
            "3. Mark Task as Completed\n"
            "4. Exit\n"
            "============================"
        )
        choice = input("Enter your choice: ").strip()

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


if __name__ == "__main__":
    main()

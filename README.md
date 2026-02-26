
# CLI Task Manager

A lightweight command-line task management tool built with Python and SQLite.

## Features

- Create tasks with a title and description
- View all active (incomplete) tasks
- Mark tasks as completed
- Persistent storage using SQLite (`data/tasks.db`)
- Automatic database/table initialization on startup
- Simple and intuitive CLI interface

## Installation

```bash
git clone <repository-url>
cd CLI_Task_Manager
```

No third-party packages are required.

## Usage

```bash
python main.py
```

On Windows, if `python` does not work, use:

```bash
py main.py
```

## Database

- Database file: `data/tasks.db`
- Main table: `tasks`
- Completed tasks are kept in the database with `completed = 1`

## Requirements

- Python 3.8+

## License

MIT

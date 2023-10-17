import sqlite3
import datetime
def create_database():
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            deadline DATE,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()
def add_task(title, description, deadline):
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, description, deadline, status)
        VALUES (?, ?, ?, ?)
    ''', (title, description, deadline, "Not Started"))
    conn.commit()
    conn.close()
def view_tasks():
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)
    conn.close()
def complete_task(task_id):
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status="Completed" WHERE id=?', (task_id,))
    conn.commit()
    conn.close()
def main():
    create_database()
    while True:
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Complete a task")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == "1":
            title = input("Enter the title: ")
            description = input("Enter the description: ")
            deadline = input("Enter the deadline (YYYY-MM-DD): ")
            add_task(title, description, deadline)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = input("Enter the number you want to mark as completed: ")
            complete_task(task_id)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.todo_db  # Connect to "todo_db"
tasks_collection = db.tasks  # Connect to "tasks" collection

# Create function (Add Task)
def create_task(description):
    task = {
        'description': description
    }
    result = tasks_collection.insert_one(task)
    print(f'Task created with id: {result.inserted_id}')

# Read function (View Tasks)
def read_tasks():
    tasks = tasks_collection.find()
    tasks_list = list(tasks)  # Convert cursor to a list
    if len(tasks_list) == 0:
        print("No tasks to display.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks_list, start=1):
            desc = task.get('description', '[No description]')
            print(f"{i}. - {desc}")

# Edit function (Update Task)
def edit_task():
    tasks = list(tasks_collection.find())
    if not tasks:
        print("No tasks to edit.")
        return

    read_tasks()  # Show existing tasks
    try:
        task_num = int(input("Enter the task number to edit: "))
        if 1 <= task_num <= len(tasks):
            new_desc = input("Enter new description: ")
            task_id = tasks[task_num - 1]['_id']
            tasks_collection.update_one({'_id': task_id}, {'$set': {'description': new_desc}})
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete function (Remove Task)
def delete_task():
    tasks = list(tasks_collection.find())
    if not tasks:
        print("No tasks to delete.")
        return

    read_tasks()  # Show existing tasks
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            task_id = tasks[task_num - 1]['_id']
            tasks_collection.delete_one({'_id': task_id})
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main Loop
while True:
    print("\n1. Create Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        description = input("Enter task description: ")
        create_task(description)
    elif choice == '2':
        read_tasks()
    elif choice == '3':
        edit_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")

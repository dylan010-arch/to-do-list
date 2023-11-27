import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. Title: {task.title}\n   Description: {task.description}\n   Date: {task.due_date}\n")

    def edit_task(self, task_index, new_title, new_description, new_due_date):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.title = new_title
            task.description = new_description
            task.due_date = new_due_date
            print("Task updated successfully")
        else:
            print("Invalid task index")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task deleted successfully")
        else:
            print("Invalid task index")


todo_list = ToDoList()

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Edit Task\n4. Delete Task\n5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        due_date = input("Enter due date (DD-MM-YYYY): ")
        todo_list.add_task(title, description, due_date)
        print("Task added successfully")

    elif choice == "2":
        print("\n--- Task List ---")
        todo_list.view_tasks()

    elif choice == "3":
        task_index = int(input("Enter the index of the task to edit: "))
        new_title = input("Enter new task title: ")
        new_description = input("Enter new task description: ")
        new_due_date = input("Enter new due date (DD-MM-YYYY): ")
        todo_list.edit_task(task_index, new_title, new_description, new_due_date)

    elif choice == "4":
        task_index = int(input("Enter the index of the task to delete: "))
        todo_list.delete_task(task_index)

    elif choice == "5":
        print("Exiting program")
        break

    else:
        print("Please enter a number between 1 and 5")

import json
import os
from datetime import datetime

class TodoList:
    def __init__(self, filename="todo_list.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, description, priority="medium"):
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "priority": priority,
            "completed": False,
            "created_at": datetime.now().isoformat()
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {description}")

    def list_tasks(self, show_completed=False):
        if not self.tasks:
            print("No tasks found.")
            return

        for task in self.tasks:
            if not show_completed and task["completed"]:
                continue
            status = "[✓]" if task["completed"] else "[ ]"
            print(f"{task['id']}. {status} {task['description']} (Priority: {task['priority']})")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                task["completed_at"] = datetime.now().isoformat()
                self.save_tasks()
                print(f"Task {task_id} marked as completed.")
                return
        print(f"Task {task_id} not found.")

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                del self.tasks[i]
                self.save_tasks()
                print(f"Task {task_id} deleted.")
                return
        print(f"Task {task_id} not found.")

    def search_tasks(self, keyword):
        results = [task for task in self.tasks if keyword.lower() in task["description"].lower()]
        if results:
            for task in results:
                status = "[✓]" if task["completed"] else "[ ]"
                print(f"{task['id']}. {status} {task['description']} (Priority: {task['priority']})")
        else:
            print("No tasks found matching the keyword.")

def main():
    todo = TodoList()

    while True:
        print("\nTodo List Manager")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Search tasks")
        print("6. Show all tasks (including completed)")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter priority (high/medium/low): ").lower()
            if priority not in ["high", "medium", "low"]:
                priority = "medium"
            todo.add_task(description, priority)
        elif choice == "2":
            todo.list_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: "))
                todo.complete_task(task_id)
            except ValueError:
                print("Invalid task ID.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                todo.delete_task(task_id)
            except ValueError:
                print("Invalid task ID.")
        elif choice == "5":
            keyword = input("Enter search keyword: ")
            todo.search_tasks(keyword)
        elif choice == "6":
            todo.list_tasks(show_completed=True)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
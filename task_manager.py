class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a task to the list."""
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def remove_task(self, task):
        """Remove a task from the list."""
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print(f"Task '{task}' not found.")

    def list_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Current Tasks:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Complete homework")
    manager.add_task("Write GitHub Actions")
    manager.list_tasks()
    manager.remove_task("Complete homework")
    manager.list_tasks()


class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task not in self.tasks:
            raise ValueError("Task not found.")

        self.tasks.remove(task)

    def mark_task_as_complete(self, task):
        if task not in self.tasks:
            raise ValueError("Task not found.")

        task.completed = True

    def get_incomplete_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def get_complete_tasks(self):
        return [task for task in self.tasks if task.completed]

    def get_task_by_name(self, name):
        for task in self.tasks:
            if task.name == name:
                return task
        return None

    def print_list(self):
        print("To-Do List:")
        for task in self.get_incomplete_tasks():
            print(f"- {task.name} ({task.priority})")

        print("Completed Tasks:")
        for task in self.get_complete_tasks():
            print(f"- {task.name} (DONE)")

def main():
    to_do_list = ToDoList()

    while True:
        command = input("What would you like to do? (add, remove, mark, print, quit)")

        if command == "add":
            name = input("Task name: ")
            priority = input("Task priority (low, medium, high): ")

            task = Task(name, priority)
            to_do_list.add_task(task)

        elif command == "remove":
            name = input("Task name to remove: ")
            task = to_do_list.get_task_by_name(name)
            if task is not None:
                to_do_list.remove_task(task)
            else:
                print("Task not found.")

        elif command == "mark":
            name = input("Task name to mark as complete: ")

            task = to_do_list.get_task_by_name(name)
            if task is not None:
                to_do_list.mark_task_as_complete(task)
            else:
                print("Task not found.")
        elif command == "print":
            to_do_list.print_list()
        elif command == "quit":
            break

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

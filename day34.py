class task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = "not completed"

    def mark_done(self):
        self.status = "completed"

    def __str__(self):
        return f"{self.title} - {self.description} - {self.status}"




class todo_list:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        new_task = task(title, description)
        self.tasks.append(new_task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.status = "completed"
                break

    def list_tasks(self):
        for task in self.tasks:
            print(f"Task: {task.title}, Description: {task.description}, Status: {task.status}")
        pass


if __name__ == "__main__":
    my_list = todo_list()

    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Complete task")
        print("4. List tasks")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            my_list.add_task(title, description)
            print(f"Task '{title}' added.")
        elif choice == "2":
            title = input("Enter task title to remove: ")
            my_list.remove_task(title)
            print(f"Task '{title}' removed.")
        elif choice == "3":
            title = input("Enter task title to complete: ")
            my_list.complete_task(title)
            print(f"Task '{title}' marked as completed.")
        elif choice == "4":
            my_list.list_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


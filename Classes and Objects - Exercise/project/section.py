from Animal import Task

class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for section_task in self.tasks:
            if section_task.name == new_task.name:
                return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        cleaned = 0
        for element in self.tasks:
            if element.completed:
                cleaned += 1
                self.tasks.remove(element)
        return f"Cleared {cleaned} tasks."

    def view_section(self):
        result = f"Section {self.name}:"
        for element in self.tasks:
            result += '\n' + element.details()

        return result


# from task import Task
from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        # for current_task in self.tasks:
        #     if current_task.details() == new_task.details():
        #         return f"Task {new_task.details()} is already in the section {self.name}"
        try:
            current_task = next(filter(lambda t: t.details() == new_task.details(), self.tasks))
        except StopIteration:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        try:
            searched_task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        self.tasks[self.tasks.index(searched_task)].completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        completed_tasks = [specific_task.name for specific_task in self.tasks if specific_task.completed == True]
        [[self.tasks.remove(current_task) for current_task in self.tasks if current_task.name == specific_task]
         for specific_task in completed_tasks]
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self):
        tasks_details = '\n'.join([final_task.details() for final_task in self.tasks])
        return f"Section {self.name}:\n" \
               f"{tasks_details}"


##########################################################################
task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
# print(50 * '-')
# third_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
# print(section.add_task(third_task))
# print(50 * '-')
# print(section.complete_task("Make bed"))
# print(50 * '-')
# print(section.complete_task("Go to University"))
# print(section.complete_task(second_task.name))
# print(50 * '-')
print(section.clean_section())
print(section.view_section())
# --------------------------------------------------------------------------
# Output_1:
# Go to University
# 28.05.2020
# Don't forget laptop and notebook
# Name: Go to University - Due Date: 28.05.2020
# Task Name: Go to University - Due Date: 28.05.2020 is added to the section
# Cleared 0 tasks.
# Section Daily tasks:
# Name: Go to University - Due Date: 28.05.2020
# Name: Make bed - Due Date: 27/05/2020
# ###########################################################################

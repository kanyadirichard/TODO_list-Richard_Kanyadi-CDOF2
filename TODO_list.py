class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added successfully!')

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            deleted_task = self.tasks.pop(task_index)
            print(f'Task: "{deleted_task["task"]}" deleted successfully!')
        else:
            print('The given task index  is invalid. Please try again.')

    def show_tasks(self):
        if not self.tasks:
            print('The task list is empty.')
        else:
            print('\nTodo List:')
            for index, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Pending"
                print(f'{index + 1}. {task["task"]} - {status}')

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f'Task: "{self.tasks[task_index]["task"]}" marked as completed!')
        else:
            print('Invalid task index. Please try again.')

def main():
    todo_list = TodoList()

    while True:
        print('\n1. Add Task\n2. Delete Task\n3. Complete Task\n4. Show Tasks\n5. Exit')
        choice = input('Enter your choice of command (1-5): ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.show_tasks()
            index = int(input('Enter the task index to delete: '))
            todo_list.delete_task(index - 1)
        elif choice == '3':
            todo_list.show_tasks()
            index = int(input('Enter the task index to mark as complete: '))
            todo_list.complete_task(index - 1)
        elif choice == '4':
            todo_list.show_tasks()
        elif choice == '5':
            print('The application is closing.')
            break
        else:
            print('Invalid choice. Please choose a number between 1 and 5.')

if __name__ == "__main__":
    main()

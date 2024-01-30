class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added successfully!')

def main():
    todo_list = TodoList()

    while True:
        print('\n1. Add Task\n5. Exit')
        choice = input('Enter your choice of command (1-5): ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '5':
            print('The application is closing.')
            break
        else:
            print('Invalid choice. Please choose a number between 1 and 5.')

if __name__ == "__main__":
    main()

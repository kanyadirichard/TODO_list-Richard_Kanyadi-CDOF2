# TODO list
A console based application to help keep track of tasks. You should be able to add, delete, complete tasks.

## Getting Started

These instructions will guide you on setting up and running the Todo List application on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your machine:

- Python 3.x: [Download Python](https://www.python.org/downloads/)


### Installing

1. Clone the repository to your local machine:

    ```Open git bash
    git clone https://github.com/kanyadirichard/TODO_list-Richard_Kanyadi-CDOF2.git
    ```

2. Navigate to the project directory:

    ```bash
    cd TODO_list-Richard_Kanyadi-CDOF2/
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Using the application

The application is very intuitive and guides the user step by step what to do. 

1. Run the application:

    ```bash
    python todo_app.py
    ```

2. You will see a menu with options:

    - **Add Task:** Add a new task to the Todo list.
    - **Delete Task:** Remove a task from the Todo list.
    - **Complete Task:** Mark a task as completed.
    - **Show Tasks:** Display the current list of tasks.
    - **Exit:** Close the application.

3. To choose one of the above listed options enter the corresponding number.

4. Follow the prompts to add, delete, or complete tasks.

5. To exit the application, choose the "Exit" option.

## Example

1. Add a Task:

    ```
    Enter your choice (1-5): 1
    Enter the task: Complete README.md

    Task "Complete README.md" added successfully!
    ```

2. Show Tasks:

    ```
    Enter your choice (1-5): 4

    Todo List:
    1. Complete README.md - Pending
    ```

3. Complete a Task:

    ```
    Enter your choice (1-5): 3

    Todo List:
    1. Complete README.md - Pending
    Enter the task index to mark as complete: 1

    Task "Complete README.md" marked as completed!
    ```

4. Show Tasks:

    ```
    Enter your choice (1-5): 4

    Todo List:
    1. Complete README.md - Completed
    ```

5. Delete Task:

    ```
    Enter your choice (1-5): 2

    Todo List:
    1. Complete README.md - Pending
    Enter the task index to delete: 1

    Task: "Complete README.md" deleted successfully!
    ```
6. Show Tasks:

    ```
    Enter your choice (1-5): 4

    The task list is empty.
    ```

## Contributing

You can contribute to the application in numerous ways.
For example:
    * Implementing file handling
    * Allowing users to set due dates or reminders
    * Implementing undo for marking a task completed
    * Making the application multi-user and adding authentication
    **    Making shared tasks between users
    * Addressing any bugs or issues found in the application


## Authors

* **Richárd Kányádi** - *Initial work*

See also the list of [contributors](https://github.com/kanyadirichard/TODO_list-Richard_Kanyadi-CDOF2/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
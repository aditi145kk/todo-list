TO-DO LIST

This is a task management application that provides basic CRUD (Create, Read, Update, Delete) functionalities, along with user authentication and task reordering features. 



Project Overview


1. User Authentication:
Login: Redirects authenticated users to the task list page.
Registration: Handles user registration, logs in the user upon successful registration, and redirects authenticated users to the task list page.
Logout: Logs out the user and renders a custom logout message.

2. Task Management:
Task List: Displays a list of tasks for the logged-in user, with options to filter tasks based on a search input. Shows the number of incomplete tasks.
Task Detail: Shows detailed information about a specific task.
Task Create: Allows users to create a new task and automatically assigns the task to the currently logged-in user.
Task Update: Provides functionality to update the details of an existing task.
Task Delete: Deletes a specific task and ensures that users can only delete tasks they own.

4. Task Reordering:
Task Reorder: Handles the reordering of tasks based on a user-defined order.



Working

User Authentication:
Users can log in and register.
Upon logging out, they are shown a custom logout page.






Task Management:
After logging in, users can view, create, update, and delete their tasks.
Tasks can be filtered by title using a search input.









Setup and Running the Project Locally

Before running the project, ensure you have the following installed:

Version


(Python 3.12.3)

(Django 5.0.3)




To Start the Django development server to run the project locally :







1. Open this Repository on Code Editor (VS Code) -




2. Open a terminal or command prompt.





3. Clone the repository using Git: git clone https://github.com/aditi145kk/todo-list.git



4. Navigate into the project directory




5. On the command Prompt :- pip install python






6. Again on the command Propmt :- pip install django


  





7. Go to Terminal and enter:-  python manage.py runserver












Resources Used (For Reference)-



https://www.geeksforgeeks.org/





https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/


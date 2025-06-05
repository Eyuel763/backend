Django Task Manager API
This is a straightforward API for managing tasks. It's built using Django (a Python web framework) and Django REST Framework (for building web APIs), storing all your task data in an SQLite database.

What it Does (Features)
You can use this API to:

Get All Tasks: GET /api/tasks

Add a New Task: POST /api/tasks

Get a Single Task: GET /api/tasks/:id

Mark Task as Completed: PUT /api/tasks/:id/mark_completed/

Update a Task (Fully): PUT /api/tasks/:id

Update a Task (Partially): PATCH /api/tasks/:id

Delete a Task: DELETE /api/tasks/:id

How to Get Started (Setup)
Follow these steps to run the API on your computer:

Get the Code:

git clone https://github.com/Eyuel763/backend.git
cd backend

Set Up Python Environment:

Create a dedicated space for project files:

python -m venv venv

Activate it:

macOS/Linux: source venv/bin/activate

Windows: venv\Scripts\activate

Install Required Software:

pip install Django djangorestframework

Prepare the Database:

python manage.py makemigrations
python manage.py migrate

Start the API:

python manage.py runserver

Your API will be ready at http://127.0.0.1:8000/api/.

How to Use the API (Examples)
You can test the API using tools like curl (command line) or Postman. All examples use http://127.0.0.1:8000/api/ as the base URL.

Get All Tasks:

curl http://127.0.0.1:8000/api/tasks/

Create a Task:

curl -X POST -H "Content-Type: application/json" -d '{"title": "My first task", "description": "Details about my task"}' http://127.0.0.1:8000/api/tasks/

Get One Task (replace 1 with the task's ID):

curl http://127.0.0.1:8000/api/tasks/1/

Mark as Completed (replace 1 with the task's ID):

curl -X PUT http://127.0.0.1:8000/api/tasks/1/mark_completed/

Update a Task (Full update - replace 1 with ID):

curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated task title", "description": "New description", "completed": true}' http://127.0.0.1:8000/api/tasks/1/

Update a Task (Partial update - replace 1 with ID):

curl -X PATCH -H "Content-Type: application/json" -d '{"description": "Just updating the description"}' http://127.0.0.1:8000/api/tasks/1/

Delete a Task (replace 1 with the task's ID):

curl -X DELETE http://127.0.0.1:8000/api/tasks/1/

Testing with Postman
Postman is a great tool for testing APIs.

Download Postman: Postman's official website

Create new requests in Postman for each endpoint, setting the correct method (GET, POST, etc.), URL, and body/headers as shown in the examples above.

Contributing
Feel free to help improve this project! Fork it, make changes, and send a pull request.
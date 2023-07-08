# Flask Todo App

This is a simple todo app built using Flask, a Python web framework. It provides basic functionality to manage and manipulate to-do items through a RESTful API.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```
3. Run the Flask app using the following command:

```bash
python app.py
```
## API Endpoints

The app exposes the following API endpoints:

- `GET /tasks`: Retrieves all the todo items.
- `POST /task`: Creates a new todo item.
- `PUT /task/<task_id>`: Updates an existing todo item.
- `DELETE /task/<task_id>`: Deletes an existing todo item.
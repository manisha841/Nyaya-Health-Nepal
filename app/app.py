'''
Question 6: Create todo app with flask framework and implement Rest API with your own
and explain the code with comment on line.

'''

from os import abort
from flask import Flask, jsonify, request

app = Flask(__name__)

# create a list to store tasks 
tasks = [
    {
        'id': 1,
        'title': 'Buy Groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]

# GET /tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    #get all the tasks from the server
    return jsonify({'tasks': tasks})

#Post data to the server
@app.route('/task', methods=['POST'])
def create_task():
    data = request.get_json()

    # Return an error response if the request body is empty 
    if not data:
        return jsonify({'error': 'Invalid request body'}), 400

    done_value = data.get('done', None)
    
    # Create a new task
    task = {
        'id': len(tasks) + 1, # Assign a unique ID to the task
        'title': data['title'], # Retrieve the title from the request data
        'description': data.get('description', ''),  # Retrieve the description if it exists, otherwise assign an empty string
        'done': done_value if done_value is not None else False  # Assign the 'done' value from the request data if it exists, otherwise assign False
    }
    # Add the new task to the tasks list
    tasks.append(task)

    # Return a JSON response with the newly created task 
    return jsonify({'task': task}), 201


# PUT /task/<id> - update existing task
@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    # Get all the tasks in the list which matches the given task_id
    task = [task for task in tasks if task['id'] == task_id]

    # Return a 400 Bad Request if the request body is empty or not valid JSON data
    if not request.json:
        abort(400)
 
    # Return a 400 Bad Request if the 'title' field in the request body is present but not of type string
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)

    # Return a 400 Bad Request if the 'description' field in the request body is present but not of type string
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    
    # Return a 400 Bad Request if the 'done' field in the request body is present but not of type bool
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)

    # Get the JSON data from the request body
    data = request.get_json()

    # Get the task to be updated from the tasks list
    todo = task[0]

    # Update the task with the new data
    if 'title' in data:
        todo['title'] = data['title']
    if 'description' in data:
        todo['description'] = data['description']
    if 'done' in data:
        todo['done'] = data['done']

    # Return the updated task as a JSON response
    return jsonify({'todo': todo})

# DELETE /task/<id> - delete existing task
@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # Find the task in the list with the given task_id
    task = [task for task in tasks if task['id'] == task_id]

    # Remove the task from the tasks list
    tasks.remove(task[0])

    # Return a JSON response indicating a successful deletion
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)


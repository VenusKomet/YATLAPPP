import uuid
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# initial IDs
todo_list_1_id = '1318d3d1-d979-47e1-a225-dab1751dbe75'
todo_list_2_id = '3062dc25-6b80-4315-bb1d-a7c86b014c65'
todo_list_3_id = '44b02e00-03bc-451d-8d01-0c67ea866fee'

todo_1_id = uuid.uuid4()
todo_2_id = uuid.uuid4()
todo_3_id = uuid.uuid4()
todo_4_id = uuid.uuid4()

# data
todo_lists = [
    {'id': todo_list_1_id, 'name': 'Einkaufsliste'},
    {'id': todo_list_2_id, 'name': 'Arbeit'},
    {'id': todo_list_3_id, 'name': 'Privat'},
]
todos = [
    {'id': todo_1_id, 'name': 'Milch', 'description': '', 'list': todo_list_1_id},
    {'id': todo_2_id, 'name': 'Arbeitsblätter ausdrucken', 'description': '', 'list': todo_list_2_id},
    {'id': todo_3_id, 'name': 'Kinokarten kaufen', 'description': '', 'list': todo_list_3_id},
    {'id': todo_3_id, 'name': 'Eier', 'description': '', 'list': todo_list_1_id},
]

# ------------------ CORS ------------------

@app.after_request
def apply_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# ------------------ routes ------------------

@app.route('/todo-list', methods=['GET'])
def getTodoList():
    return jsonify(todo_lists), 200

@app.route('/todo-list', methods=['POST'])
def createTodoList():
    new_list = request.get_json(force=True)

    print('Got new Task to add new List: {}'.format(new_list))

    new_list['id'] = uuid.uuid4()
    todo_lists.append(new_list)

    return jsonify(new_list), 201

@app.route('/todo-list/<list_id>', methods=['GET'])
def getTodoListEntries(list_id):
    list_item = None

    for todolist in todo_lists:
        if todolist['id'] == list_id:
            list_item = todolist
            break

    if not list_item:
        abort(404)

    print('returning todolist...')
    return jsonify(item for item in todos if item['list'] == list_id), 200

@app.route('/todo-list/<list_id>', methods=['DELETE'])
def deleteTodoList(list_id):
    list_item = None

    for todolist in todo_lists:
        if todolist['id'] == list_id:
            list_item = todolist
            break

    if not list_item:
        abort(404)

    print('Deleting todo list...')
    todo_lists.remove(list_item)
    return '', 204

@app.route('/todo-list/<list_id>', methods=['POST'])
def addTodoListEntry(list_id):
    list_item = None

    for todolist in todo_lists:
        if todolist['id'] == list_id:
            list_item = todolist
            break

    if not list_item:
        abort(404)

    new_todo = request.get_json(force=True)
    print('Got new Task for adding a new Task to a List: {}'.format(new_todo))

    new_todo['id'] = uuid.uuid4()
    new_todo['list'] = list_id

    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/todo-list/entry/<entry_id>', methods=['PATCH'])
def modifyTodolistEntry(entry_id):
    entry_item = None

    for entry in todos:
        if entry['id'] == entry_id:
            entry_item = entry
            break

    if not entry_item:
        abort(404)

    modified_todo = request.get_json(force=True)
    print('Got new Task to modify a Todo: {}'.format(modified_todo))

    for entry in todos:
        if entry['id'] == entry_id:
            entry = modified_todo
            break

@app.route('/todo-list/entry/<entry_id>', methods=['DELETE'])
def deleteTodoListEntry(list_id):
    list_item = None

    for todolist in todo_lists:
        if todolist['id'] == list_id:
            list_item = todolist
            break

    if not list_item:
        abort(404)

    print('Deleting todo list...')
    todo_lists.remove(list_item)
    return '', 204

# ------------------ run ------------------

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

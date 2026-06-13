import uuid
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

def generate_id():
    return str(uuid.uuid4())

# initial IDs
todo_list_1_id = generate_id()
todo_list_2_id = generate_id()
todo_list_3_id = generate_id()

todo_1_id = generate_id()
todo_2_id = generate_id()
todo_3_id = generate_id()
todo_4_id = generate_id()

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
    {'id': todo_4_id, 'name': 'Eier', 'description': '', 'list': todo_list_1_id},
]

# ------------------ helpers ------------------

def find_list(list_id):
    return next((l for l in todo_lists if l['id'] == list_id), None)

def find_todo(entry_id):
    return next((t for t in todos if t['id'] == entry_id), None)

# ------------------ CORS ------------------

@app.after_request
def apply_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE,PATCH'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# ------------------ routes ------------------

@app.route('/todo-list', methods=['GET'])
def get_todo_lists():
    return jsonify(todo_lists), 200


@app.route('/todo-list', methods=['POST'])
def create_todo_list():
    new_list = request.get_json(force=True)
    new_list['id'] = generate_id()
    todo_lists.append(new_list)
    return jsonify(new_list), 201


@app.route('/todo-list/<list_id>', methods=['GET'])
def get_todo_list_entries(list_id):
    if not find_list(list_id):
        abort(404)

    result = [item for item in todos if item['list'] == list_id]
    return jsonify(result), 200


@app.route('/todo-list/<list_id>', methods=['DELETE'])
def delete_todo_list(list_id):
    list_item = find_list(list_id)

    if not list_item:
        abort(404)

    todo_lists.remove(list_item)

    # also remove associated todos
    global todos
    todos = [t for t in todos if t['list'] != list_id]

    return '', 204


@app.route('/todo-list/<list_id>', methods=['POST'])
def add_todo_list_entry(list_id):
    if not find_list(list_id):
        abort(404)

    new_todo = request.get_json(force=True)
    new_todo['id'] = generate_id()
    new_todo['list'] = list_id

    todos.append(new_todo)
    return jsonify(new_todo), 201


@app.route('/todo-list/entry/<entry_id>', methods=['PATCH'])
def modify_todo_list_entry(entry_id):
    entry = find_todo(entry_id)

    if not entry:
        abort(404)

    updates = request.get_json(force=True)

    # update only allowed fields
    entry.update({
        'name': updates.get('name', entry['name']),
        'description': updates.get('description', entry['description'])
    })

    return jsonify(entry), 200


@app.route('/todo-list/entry/<entry_id>', methods=['DELETE'])
def delete_todo_list_entry(entry_id):
    entry = find_todo(entry_id)

    if not entry:
        abort(404)

    todos.remove(entry)
    return '', 204


# ------------------ run ------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
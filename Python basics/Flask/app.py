from flask import Flask, jsonify, request

app = Flask(__name__)


items = [
    {'id': 1, 'name': 'Item 1', 'price': 10.99},
    {'id': 2, 'name': 'Item 2', 'price': 12.99},
    {'id': 3, 'name': 'Item 3', 'price': 15.99}
]
@app.route('/')
def home():
    return "Welcome to the To do app!"

@app.route('/items', methods = ['GET']) ## Retrieve all the items 
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])  # Retrieve a specific item by ID
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404
    
@app.route('/items', methods=['POST'])  # Create a new item
def create_item():
    if not request.json or 'name' not in request.json or 'price' not in request.json:
        return jsonify({'error': 'Bad Request'}), 400
    new_item = {
        'id': items[-1]['id'] + 1,
        'name': request.json['name'],
        'price': request.json['price']
    }
    items.append(new_item)
    return jsonify(new_item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])  # Update an existing item
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    if not request.json or 'name' not in request.json or 'price' not in request.json:
        return jsonify({'error': 'Bad Request'}), 400
    item['name'] = request.json['name']
    item['price'] = request.json['price']
    return jsonify(item)

@app.route('/items/<int:item_id>', methods=['DELETE'])  # Delete an item
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'result': True, 'message': 'Item deleted successfully'}), 200




if __name__ == '__main__':
    app.run(debug=True)

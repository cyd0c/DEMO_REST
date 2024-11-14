from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
# Swagger UI Configuration
SWAGGER_URL = '/docs'  # URL for accessing Swagger UI
API_URL = '/swagger.yaml'  # Path to the Swagger YAML file

# Swagger UI Blueprint setup
swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Item Management API"})
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

items = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'},
    {'id': 3, 'name': 'Item 3'}
]

@app.route('/')
def home():
    
    return "Welcome to the Flask API!"

# Get all items (GET request)
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Create a new item (POST request)
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()  # Get the data from the request
    items.append(new_item)  # Add the new item to the list
    return jsonify(new_item), 201  # Return the new item with a 201 status code

# Update an item (PUT request)
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((i for i in items if i['id'] == item_id), None)
    if item is None:
        return jsonify({'message': 'Item not found'}), 404

    updated_data = request.get_json()  # Get the updated data from the request
    item.update(updated_data)  # Update the item
    return jsonify(item), 200  # Return the updated item with a 200 status code

# Delete an item (DELETE request)
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]  # Remove the item by ID
    return jsonify({'message': 'Item deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)

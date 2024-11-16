# SAMPLE REST API

## Introduction
The Item Management API is a simple RESTful API built with Flask to manage a list of items. It supports operations to retrieve, create, update, and delete items. The API uses Swagger UI for interactive documentation and testing.

## Features
- Retrieve all items.
- Add a new item.
- Update an existing item by its ID.
- Delete an item by its ID.
- Interactive API documentation with Swagger UI.

## Installation and Setup

### Prerequisites
- Python 3.7+
- Flask
- Flask-Swagger-UI

### Steps

#### Clone the Repository

```bash
git clone https://github.com/your-repo/item-management-api.git
cd item-management-api
```
Install Dependencies

```bash
pip install flask flask-swagger-ui
```
Run the Application
```bash
python app.py
```
Access the API
```
Home page: http://localhost:5000/
Swagger UI: http://localhost:5000/docs
```
API Endpoints
1. GET /
Description: Returns a welcome message.
Response:

```json
"Welcome to the Flask API!"
```
2. GET /items
Description: Retrieves a list of all items.
Response:

```json

[
  {"id": 1, "name": "Item 1"},
  {"id": 2, "name": "Item 2"},
  {"id": 3, "name": "Item 3"}
]
```
3. POST /items
Description: Creates a new item.
Request Body:

```json

{
  "id": 4,
  "name": "Item 4"
}
```
Response:

```json

{
  "id": 4,
  "name": "Item 4"
}
```
4. PUT /items/{item_id}
Description: Updates an existing item.
Request Parameters:

item_id (integer) - ID of the item to update.
Request Body:
```json

{
  "name": "Updated Item 1"
}
```
Response:

```json

{
  "id": 1,
  "name": "Updated Item 1"
}
```
5. DELETE /items/{item_id}
Description: Deletes an item by ID.
Request Parameters:

item_id (integer) - ID of the item to delete.
Response:
```json

{
  "message": "Item deleted"
}
```
Swagger UI Integration
What is Swagger UI?
Swagger UI provides an interactive web interface to test API endpoints. It uses a YAML file to define the API schema, making it easier for developers and testers to understand and interact with the API.

Configuring Swagger UI

```python

from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/docs'
API_URL = '/static/swagger.yaml'
swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Item Management API"})
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
```
Create swagger.yaml
The swagger.yaml file defines the API endpoints, parameters, and responses. Place it in the static directory.

YAML File Explanation
The swagger.yaml file uses the Swagger 2.0 format to define the API schema:

Title and Description
Provides details about the API.

```yaml

info:
  title: "Item Management API"
  description: "A simple API to manage items"
  version: "1.0.0"
Paths
Defines endpoints, methods, parameters, and responses.

```
Example: GET /items

```yaml

/items:
  get:
    summary: "Get all items"
    description: "Returns a list of all items."
    responses:
      200:
        description: "A list of items"
        schema:
          type: "array"
          items:
            type: "object"
            properties:
              id:
                type: "integer"
              name:
                type: "string"

```
Testing the API
Open Swagger UI: http://localhost:5000/docs
Test endpoints directly from the web interface by clicking on the available routes and providing the necessary input.
View the JSON response and status codes for each request.
Conclusion
This API demonstrates how to build a RESTful service with Flask and document it using Swagger. The interactive Swagger UI makes it easy to test and understand the API. Future enhancements can include database integration, authentication, and more advanced features.

from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

# Temporary storage for tasks
tasks = []
task_id_counter = 1

# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# GET all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# POST a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    global task_id_counter
    title = request.form.get('title')
    
    task = {
        'id': task_id_counter,
        'title': title,
        'completed': False
    }
    tasks.append(task)
    task_id_counter += 1
    return redirect(url_for('index'))  # Redirect back to the index page

# PUT to update a task
@app.route('/tasks/<int:task_id>', methods=['POST'])
def update_task(task_id):
    title = request.form.get('title')
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    task['title'] = title  # Update title
    return redirect(url_for('index'))  # Redirect back to the index page

# DELETE a task
@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return redirect(url_for('index'))  # Redirect back to the index page

if __name__ == '__main__':
    app.run(debug=True)

from flask import jsonify
from flask import request
from models import task_db

def index():
    return jsonify(task_db.tasks)

def create():
    if request.is_json:
        task = request.get_json()
        task['id'] = task_db.newId()
        task['done'] = False
        
        task_db.tasks.append(task)

        return jsonify({"message": "Task created successfully"}), 201
    
    return jsonify({"message": "Error: Content-Type must be application/json"}), 415

def read(id):
    for task in task_db.tasks:
        if task['id'] == id:
            return jsonify(task)

    return jsonify({"message": "Task not found"}), 404

def update(id):
    for task in task_db.tasks:
        if task['id'] == id:
            if request.is_json:
                task['title'] = request.get_json()['title']
                return jsonify({"message": "Task updated successfully"}), 200
            
            return jsonify({"message": "Error: Content-Type must be application/json"}), 415
    
    return jsonify({"message": "Task not found"}), 404

def destroy(id):
    for task in task_db.tasks:
        if task['id'] == id:
            task_db.tasks.remove(task)
            return jsonify({"message": "Task deleted successfully"}), 200
        
    return jsonify({"message": "Task not found"}), 404

def destroy_all():
    for task in task_db.tasks:
        if len(task) != 0:
            task_db.tasks.clear()
            return jsonify({"message": "All tasks deleted successfully"}), 200
        
    return jsonify({"message": "No tasks found"}), 404
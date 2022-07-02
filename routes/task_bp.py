from flask import Blueprint
from controllers.task_controller import index, create, read, update, destroy, destroy_all

task_bp = Blueprint('task_bp', __name__)
task_bp.route('/', methods=['GET'])(index)
task_bp.route('/', methods=['POST'])(create)
task_bp.route('/<int:id>', methods=['GET'])(read)
task_bp.route('/<int:id>', methods=['PUT', 'PATCH'])(update)
task_bp.route('/<int:id>', methods=['DELETE'])(destroy)
task_bp.route('/destroy', methods=['DELETE'])(destroy_all)
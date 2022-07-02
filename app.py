from flask import Flask
from routes.task_bp import task_bp

app = Flask(__name__)

app.register_blueprint(task_bp, url_prefix = '/tasks')

if __name__ == '__main__':
    app.debug = True
    app.run()
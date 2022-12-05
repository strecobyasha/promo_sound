from flask import Flask, Blueprint
from flask_executor import Executor

UPLOAD_FOLDER = 'uploaded'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def create_app():
    from routes.index import bp as index_bp

    root_bp = Blueprint('root', __name__, url_prefix=f'')
    root_bp.register_blueprint(index_bp)

    app.register_blueprint(root_bp)

    return app


app = create_app()

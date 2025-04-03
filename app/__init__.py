from flask import Flask
from flask_bootstrap import Bootstrap

# def create_app():
#     app = Flask(__name__)
#     Bootstrap(app)
#     with app.app_context():
#         from . import routes
#     return app



def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    from app.routes import blueprint
    app.register_blueprint(blueprint)

    return app
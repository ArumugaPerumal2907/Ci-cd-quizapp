from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        from . import app as main_app
        app.register_blueprint(main_app)

    return app

app = create_app()
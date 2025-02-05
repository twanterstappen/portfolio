#!/usr/bin/env python3

import os
from flask import Flask
from .extensions import db
from .routes import main, error
from dotenv import load_dotenv
load_dotenv()
from werkzeug.serving import is_running_from_reloader


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Load global configuration from root config.py
    config_type = os.getenv('FLASK_ENV', 'production').capitalize()
    print(config_type)

    app.config.from_object(f'flaskr.config.{config_type}Config')

    # Optionally load environment-specific overrides from instance/config.py
    app.config.from_pyfile('env.py', silent=True)

    # Initialize database
    db.init_app(app)

    # Initialize the database tables if there is no database file
    with app.app_context():
        db.create_all()

    # Register blueprints
    app.register_blueprint(main.bp)
    app.register_blueprint(error.bp)

    return app


if __name__ == "__main__":
    app = create_app()

    # Run the app on a free port if the default is unavailable
    def find_free_port(default_port=5000):
        import socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('0.0.0.0', default_port))
                return default_port
            except OSError:
                s.bind(('0.0.0.0', 0))
                return s.getsockname()[1]

    if not is_running_from_reloader():
        port = find_free_port(int(os.environ.get('PORT', 5000)))

        print(f"Starting server on port {port}...")
    else:
        port = 5000

    app.run(debug=app.config['DEBUG'], host='0.0.0.0',
            port=port, use_reloader=app.config['USER_RELOAD'])

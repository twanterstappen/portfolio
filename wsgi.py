#!/usr/bin/env python3
from flaskr import create_app


app = create_app()

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=5000, use_reloader=app.config['USER_RELOAD'])

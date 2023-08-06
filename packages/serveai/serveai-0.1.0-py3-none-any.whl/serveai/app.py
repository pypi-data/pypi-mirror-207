#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

from config import DEBUG, SERVER_PORT
from database import initialize_database
from middlewares import cors_middleware, rate_limit_middleware
from routes import routes_blueprint


if __name__ == "__main__":
    app = Flask(__name__)

    initialize_database(app)

    app.after_request(cors_middleware)
    # app.before_request(rate_limit_middleware)

    # Register routes
    app.register_blueprint(routes_blueprint)

    app.run(debug=DEBUG, port=SERVER_PORT)

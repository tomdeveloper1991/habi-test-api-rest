from flask import Flask, request
from application.api.property import property


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(property, url_prefix=property.url_prefix)
    return app

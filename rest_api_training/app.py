from flask import Flask
from flask_restful import Api

import custom_resources

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///videos.db"

    return app

def create_api(app: Flask):
    api = Api(app)
    register_resources(api)

def register_resources(api: Api):
    api.add_resource(custom_resources.HelloWorld, "/helloworld")
    api.add_resource(custom_resources.People, "/people/<string:name>")
    api.add_resource(custom_resources.Video, "/video/<int:video_id>")

from flask_restful import Resource

class HelloWorld(Resource):
    def __init__(self):
        self.data = {"data" : "Hello World"}

    def get(self):
        return self.data

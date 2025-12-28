from flask_restful import Resource

class People(Resource):
    def __init__(self):
        self.people = {
            "John" : {"age": 48, "weight" : 70},
            "Chris" : {"age": 23, "weight" : 72},
            "Adam" : {"age": 47, "weight" : 73},
            "Anna" : {"age": 32, "weight" : 60},
        }

    def get(self, name):
        return self.people[name]

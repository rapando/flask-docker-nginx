from flask_restful import Resource
from flask import current_app


class Index(Resource):

    def __init__(self):
        self.log = current_app.logger
        self.log.info("initializing the Index resource")

    def get(self):
        self.log.info("Get request to sample index")
        return "Hey alien, Are you lost? You are on Earth"

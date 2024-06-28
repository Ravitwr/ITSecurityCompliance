from flask import Blueprint, jsonify, make_response
from flask_restx import Api, Resource  # type: ignore

app = Blueprint("health", __name__)
api = Api(app)

class HealthCheck(Resource):
    def get(self):
        return make_response(jsonify({"result": "ok"}))


api.add_resource(HealthCheck, "/health")

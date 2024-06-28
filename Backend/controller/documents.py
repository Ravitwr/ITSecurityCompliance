from flask_restx import Resource  # type: ignore

from service.documents import DocumentsService

class Documents(Resource):
    def get(self):
        res = DocumentsService.get()
        return res.__dict__

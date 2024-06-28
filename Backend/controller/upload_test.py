from flask_restx import Resource  # type: ignore

# from service.documents import DocumentsService
from gpt.embedder import Embedder
from flask import request


class UploadTest(Resource):
    def get(self):
        directory_path = request.args.get('directory_path')
        Embedder.storeDocEmbeds(directory_path)
        return "success"

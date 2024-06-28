from flask_restx import Resource  # type: ignore
from service.filtered_documents import FilterDocumentService
from flask import request

class FilteredDocuments(Resource):
    def get(self):
        industry = request.args.get('industry')
        region = request.args.get('region')
        res = FilterDocumentService.get(industry,region)
        return res.__dict__

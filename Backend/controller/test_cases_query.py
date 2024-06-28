from flask_restx import Resource  # type: ignore
from flask import request
from service.test_cases_query import TestCasesQueryService


class TestCasesQuery(Resource):
    def post(self):

        data = request.json
        if not data:
            return {"error": "No data provided"}, 400
        doc_list = data.get('doc_list', [])
        query = data.get('query', '').lower()
        res=TestCasesQueryService.get_testcase(query=query,doc_list=doc_list)
        return res.__dict__
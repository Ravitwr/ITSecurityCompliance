from flask import Blueprint
from flask_restx import Api  # type: ignore

app = Blueprint("/api/v1", __name__)
api = Api(app)

import controller.error_handler # type: ignore  # noqa: F401, E402, I001
from controller.documents import Documents # noqa: E402
from controller.filtered_documents import FilteredDocuments # noqa: E402
from controller.test_cases_query import TestCasesQuery # noqa: E402
from controller.upload_test import UploadTest # noqa: E402
from controller.evidence_upload import UploadEvidence # noqa: E402

api.add_resource(
    Documents,
    "/documents",
    endpoint="documents"
)

api.add_resource(
    FilteredDocuments,
    "/documents/filtered",
    endpoint="filtered-documents"
)

api.add_resource(
    TestCasesQuery,
    "/test_cases_query",
    endpoint="test-cases-query"
)

api.add_resource(
    UploadTest,
    "/upload_query",
    endpoint="upload-query"
)

api.add_resource(
    UploadEvidence,
    "/verify_evidence",
    endpoint="upload-evidence"
)




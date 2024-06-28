from flask_restx import Resource  # type: ignore

from flask import request
from service.evidence_upload import EvidenceUploadService


class UploadEvidence(Resource):
    def post(self):
        if not request.is_json:
            return {"error": "Missing JSON in request"}, 400

        data = request.get_json()
        processed_data = []
        for evidence in data:
            id = evidence.get('id')
            name = evidence.get('name')
            description = evidence.get('description')
            evidence_desc = evidence.get('evidence')
            filename = evidence.get('filename')

            processed_entry = {
                "id": id,
                "name": name, 
                "description": description,
                "evidence": evidence_desc,
                "filename": filename
            }
            processed_data.append(processed_entry)
        result=EvidenceUploadService.verify_evidence(processed_data)
        return result.__dict__

















    
    # def post(self):
    #     if 'file' not in request.files:
    #         return {"error": "No file part"}, 400

    #     file = request.files['file']
    #     if file.filename == '':
    #         return {"error": "No selected file"}, 400

    #     if file:
    #         stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
    #         csv_input = pd.read_csv(stream)

    #         expected_columns = ["id","Control Family", "Domain", "Sub-Domain", "Control Description", "Test Procedure", "Accepted Evidence"]
    #         if csv_input.empty or not all(column in csv_input.columns for column in expected_columns):
    #             return {"error": "CSV file is empty or does not contain the required columns"}, 400

    #         controls_info = []
    #         for _, row in csv_input.iterrows():
    #             control_data = {
    #                 "id": row["id"],
    #                 "control_family": row["Control Family"],
    #                 "domain": row["Domain"],
    #                 "sub_domain": row["Sub-Domain"],
    #                 "control_description": row["Control Description"],
    #                 "test_procedure": row["Test Procedure"],
    #                 "accepted_evidence": row["Accepted Evidence"]
    #             }
    #             controls_info.append(control_data)
            
    #         return controls_info, 200

    #     else:
    #         return {"error": "Invalid file"}, 400






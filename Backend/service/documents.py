from typing import Any, Dict
from database import db
from model import (
    Industry,
    Region,
    IndustrySchema,
    RegionSchema,
)
from model.common_response import CommonResponse

class DocumentsService:
    @staticmethod
    def get() -> CommonResponse:
        industry_list = db.session.query(Industry).all()
        region_list = db.session.query(Region).all()
        industry_data = IndustrySchema(many=True).dump(industry_list)
        region_data = RegionSchema(many=True).dump(region_list)
        result: Dict[str, Any] = {
            "IndustryList": industry_data,
            "RegionList": region_data,
        }
        return CommonResponse(status="success", result=result)

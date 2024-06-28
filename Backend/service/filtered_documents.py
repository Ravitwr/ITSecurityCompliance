from typing import Any, Dict, Optional
from database import db
from model import (
    Document,
    DocumentSchema,
    Industry,
    Region,
    DocumentIndustry,
    DocumentRegion,
)
from model.common_response import CommonResponse


class FilterDocumentService:
    @staticmethod
    def get(industry: Optional[str] = None, region: Optional[str] = None) -> CommonResponse:

        query = db.session.query(Document)
            
        if industry:
            query = query.join(DocumentIndustry).join(Industry).filter(Industry.IndustryName == industry)
        
        if region:
            query = query.join(DocumentRegion).join(Region).filter(Region.RegionName == region)

        documents = query.all()
        documents_list=DocumentSchema(many=True).dump(documents)
        # Constructing the result dictionary
        result: Dict[str, Any] = {
            "Documents": documents_list
        }
        # Returning a CommonResponse object with the serialized data
        return CommonResponse(status="success", result=result)
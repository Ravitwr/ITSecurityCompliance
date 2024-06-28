from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import Base, ma

class Document(Base):
    __tablename__ = "Documents"

    DocumentID: Mapped[int] = mapped_column(Integer, primary_key=True)
    DocumentName: Mapped[str] = mapped_column(String(255))

class Industry(Base):
    __tablename__ = "Industries"

    IndustryID: Mapped[int] = mapped_column(Integer, primary_key=True)
    IndustryName: Mapped[str] = mapped_column(String(100))

class Region(Base):
    __tablename__ = "Regions"

    RegionID: Mapped[int] = mapped_column(Integer, primary_key=True)
    RegionName: Mapped[str] = mapped_column(String(100))

class DocumentIndustry(Base):
    __tablename__ = "DocumentIndustries"

    DocumentID: Mapped[int] = mapped_column(Integer, ForeignKey('Documents.DocumentID'), primary_key=True)
    IndustryID: Mapped[int] = mapped_column(Integer, ForeignKey('Industries.IndustryID'), primary_key=True)

class DocumentRegion(Base):
    __tablename__ = "DocumentRegions"

    DocumentID: Mapped[int] = mapped_column(Integer, ForeignKey('Documents.DocumentID'), primary_key=True)
    RegionID: Mapped[int] = mapped_column(Integer, ForeignKey('Regions.RegionID'), primary_key=True)

class DocumentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Document

class IndustrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Industry

class RegionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Region

class DocumentIndustrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DocumentIndustry

class DocumentRegionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DocumentRegion
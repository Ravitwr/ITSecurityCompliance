from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


class Base(DeclarativeBase, MappedAsDataclass):
    pass


db = SQLAlchemy(model_class=Base)
ma = Marshmallow()


def init_db(app: Flask):
    db.init_app(app)


def init_ma(app: Flask):
    ma.init_app(app)

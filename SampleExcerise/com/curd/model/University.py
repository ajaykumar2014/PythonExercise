from dataclasses import dataclass
from typing import Any
from com.curd.config import db, ma


# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()


# @dataclass(init=True)
class University(db.Model):
    __tablename__ = 'universityTable'
    index = db.Column(db.Integer, primary_key='True', autoincrement=True)
    name = db.Column(db.String)
    country = db.Column(db.String)
    Domains = db.Column(db.String)
    WebPages = db.Column(db.String)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        print(f'kwargs{kwargs}')
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return "<University: {}, {}, {}, {} >".format(self.name, self.country, self.Domains, self.WebPages)


class UniversitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = University
        instance_load = True
        sqla_session = db.session
        # field = ('name', 'country', 'Domains', 'WebPages')


universitySchema = UniversitySchema()
universitysSchema = UniversitySchema(many=True)

# class UniversitySchema(SQLAlchemySchema):
#     class Meta:
#         model = University
#         load_instance = True  # Optional: deserialize to model instances
#
#     id = auto_field()
#     name = auto_field()
#     country = auto_field()
#     Domains = auto_field()
#     WebPages = auto_field()

from sqlalchemy import Column, Integer
from sqlalchemy.orm import declared_attr


# Declare base class
class Base:

    @declared_attr
    def id(self):
        return Column(Integer, primary_key=True)

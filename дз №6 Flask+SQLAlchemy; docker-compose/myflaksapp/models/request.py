from sqlalchemy import Column, Integer, String, Boolean

from .database import db


class Request(db.Model):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, default=f"name")
    email = Column(String, nullable=False, default=f"none")
    phone = Column(String, nullable=False, default=f"88005553555")



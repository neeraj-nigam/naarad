from .db import Base
from sqlalchemy import Column, Integer, String

class Ip(Base):
    __tablename__ = "scanned_ip"
    _id = Column(Integer, primary_key=True)
    ip = Column(String)
    open_ports = Column(String)

    def __repr__(self):
        return self.value

class Banners(Base):
    __tablename__ = "banners"
    _id = Column(Integer, primary_key=True)
    value = Column(String)

    def __repr__(self):
        return self.value

class Server(Base):
    __tablename__ = "server"
    _id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return self.value[:10]
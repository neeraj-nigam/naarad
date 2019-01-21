# define models for parsing headers from web

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


engine = create_engine("sqlite:///:memory:",echo=True)
Base = declarative_base()

from .models import Ip, Banners, Server

def create_all(self):
    self.Base.metadata.create_all()
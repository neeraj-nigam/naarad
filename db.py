# define models for parsing headers from web

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


engine = create_engine()
Base = declarative_base()


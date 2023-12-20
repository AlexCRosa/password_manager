from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine
from sqlalchemy.orm import declarative_base

db_url = 'sqlite:///database.db'

engine = create_engine(db_url)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    website = Column(String)

    def __init__(self, name, email):
        self.name = name
        self.email = email

Base.metadata.create_all(engine)
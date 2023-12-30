from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from typing import List
from typing import Optional
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

db_url = 'sqlite:///database.db'

engine = create_engine(db_url, echo=True)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(128), nullable=False)

    @property
    def password_hash(self):
        raise AttributeError('password is not a readable attribute!')

    @password_hash.setter
    def password_hash(self, password_hash):
        self.password = generate_password_hash(password_hash)

    def verify_password(self, password_hash):
        return check_password_hash(self.password, password_hash)

    # Create A String
    def __repr__(self):
        return '<Name %r>' % self.name

Base.metadata.create_all(engine)

u = User()
u.password_hash = 'cat'
print(u.password)


"""
# --------------------
from sqlalchemy import select
from sqlalchemy.orm import Session

session = Session(engine)

teste1 = session.query(session.query(User).filter_by(password='kjsahdsad987').exists()).scalar()

print(teste1)

teste2 = session.query(session.query(User).filter_by(email='stark@email.com').exists()).scalar()

print(teste2)

"""
# FILEPATH: /home/joosef/ohtuminiprojekti/ohtu_kandi_viitteet/src/schema.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint


Base = declarative_base()

class User(Base):
    __tablename__ = 'Users_Table'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

class Reference(Base):
    __tablename__ = 'References_Table'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    visible = Column(Boolean)
    author = Column(String)
    title = Column(String)
    journal = Column(String)
    year = Column(String)
    volume = Column(String)
    publisher = Column(String)
    booktitle = Column(String)
    number = Column(String)
    pages = Column(String)
    month = Column(String)
    doi = Column(String)
    note = Column(String)
    key = Column(String)
    series = Column(String)
    address = Column(String)
    edition = Column(String)
    url = Column(String)
    editor = Column(String)
    organization = Column(String)



class UserReference(Base):
    __tablename__ = 'UserReferences_Table'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users_Table.id'))
    reference_id = Column(Integer, ForeignKey('References_Table.id'))
    user = relationship("User")
    reference = relationship("Reference")
    __table_args__ = (UniqueConstraint('user_id', 'reference_id'),)

class Tag(Base):
    __tablename__ = 'Tags_Table'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    reference_id = Column(Integer, ForeignKey('References_Table.id'))
    reference = relationship("Reference")



#Fundamantal base object that is to be inharitated
from sqlalchemy.ext.declarative import declarative_base
#Basic column and type of the field
from sqlalchemy import Column, Integer, String
#engine for connection DBMS
from sqlalchemy import create_engine
#for foreign key setting
from sqlalchemy import ForeignKey
#for make a relationship between tables
from sqlalchemy.orm import relationship, backref

Base=declarative_base()

class Address(Base):
    
    __tablename__='addresses' #name of table
    
    #list of column
    index = Column(Integer, primary_key=True)
    email_address = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.index'))
    
    #make a relationship between this class and class 'User'
    user = relationship("User", backref="addresses")
    
    #This is instructor
    def __init__(self, email_address):
        self.email_address = email_address

    #This returns general information of this class
    def __repr__(self):
        return "<Address('%s')>"%self.email_address

class User(Base):
    __tablename__='users'

    index = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s','%s')>"%(self.name, self.fullname, self.password)

engine=create_engine("mysql://root:wjdtnsgud1!@localhost/sqlalchemytest", encoding='utf8', echo=True)
Base.metadata.create_all(engine)



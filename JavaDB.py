from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

Base=declarative_base()

class PhoneInfo(Base):
    __tablename__='phoneinfo'
    name = Column(String(50), primary_key=True)
    phonenum = Column(String(50), nullable=False)
    phoneuniv = relationship("PhoneUnivInfo", backref="phoneinfo")
    phinecompany = relationship("PhoneCompanyInfo", backref="phoneinfo")

class PhoneUnivInfo(Base):
    __tablename__='phoneunivinfo'
    name = Column(String(50), ForeignKey('phoneinfo.name'))
    major = Column(String(50),nullable=False)
    year = Column(Srring(50), nullable=False)

class PhoneCompanyInfo(Base):
    __tablename__='phonecompanyinfo'
    name = Column(String(50), ForeignKey('phoneinfo.name'))
    company = Column(String(50), nullable=False)
    
engine=create_engine("mysql://root:wjdtnsgud1!@localhost/sqlalchemytest", encoding='utf8', echo=True)
Base.metadata.create_all(engine)



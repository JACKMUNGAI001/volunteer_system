from sqlalchemy import create_engine, Column, Date, Integer, String 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    location = Column(String, nullable=False)
    required_skills = Column(String)
    assignments = relationship("Assignment", back_populates="event")

class Volunteer(Base):
    __tablename__ = 'volunteers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String)
    skills = Column(String)
    assignments = relationship("Assignment", back_populates="volunteer")

engine = create_engine('sqlite:///volunteer_system.db')
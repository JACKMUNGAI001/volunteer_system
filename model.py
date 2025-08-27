from sqlalchemy import create_engine, Column, Date, Integer, String 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


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

class Assignment(Base):
    __tablename__ = 'assignments'
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)
    volunteer_id = Column(Integer, ForeignKey('volunteers.id'), nullable=False)
    assignment_date = Column(Date, nullable=False)
    status = Column(String, default="pending")
    event = relationship("Event", back_populates="assignments")
    volunteer = relationship("Volunteer", back_populates="assignments")

engine = create_engine('sqlite:///volunteer_system.db')
Base.metadata.create_all(engine)
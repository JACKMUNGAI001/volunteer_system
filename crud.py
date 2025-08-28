from sqlalchemy.orm import sessionmaker
from model import engine, Event, Volunteer, Assignment
from datetime import datetime
import re
from typing import List, Optional

Session = sessionmaker(bind=engine)

def create_event(name: str, date: str, location: str, required_skills: str) -> Event:
    session = Session()
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        event = Event(name=name, date=date_obj, location=location, required_skills=required_skills)
        session.add(event)
        session.commit()
        return event
    except ValueError:
        session.rollback()
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_all_events() -> List[Event]:
    session = Session()
    try:
        events = session.query(Event).all()
        return events
    finally:
        session.close()

def get_event_by_id(event_id: int) -> Optional[Event]:
    session = Session()
    try:
        event = session.query(Event).filter_by(id=event_id).first()
        return event
    finally:
        session.close()

def create_volunteer(name: str, email: str, phone: str, skills: str) -> Volunteer:
    session = Session()
    try:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")
        volunteer = Volunteer(name=name, email=email, phone=phone, skills=skills)
        session.add(volunteer)
        session.commit()
        return volunteer
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_all_volunteers() -> List[Volunteer]:
    session = Session()
    try:
        volunteers = session.query(Volunteer).all()
        return volunteers
    finally:
        session.close()

def get_volunteer_by_id(volunteer_id: int) -> Optional[Volunteer]:
    session = Session()
    try:
        volunteer = session.query(Volunteer).filter_by(id=volunteer_id).first()
        return volunteer
    finally:
        session.close()

def create_assignment(event_id: int, volunteer_id: int, assignment_date: str) -> Assignment:
    session = Session()
    try:
        assignment_date_obj = datetime.strptime(assignment_date, '%Y-%m-%d').date()
        assignment = Assignment(event_id=event_id, volunteer_id=volunteer_id, assignment_date=assignment_date_obj)
        session.add(assignment)
        session.commit()
        return assignment
    except ValueError:
        session.rollback()
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_assignments_by_event(event_id: int) -> List[Assignment]:
    session = Session()
    try:
        assignments = session.query(Assignment).filter_by(event_id=event_id).all()
        return assignments
    finally:
        session.close()

def delete_event(event_id: int) -> None:
    session = Session()
    try:
        event = session.query(Event).filter_by(id=event_id).first()
        if not event:
            raise ValueError(f"Event with ID {event_id} not found.")
        
        session.query(Assignment).filter_by(event_id=event_id).delete()
        session.delete(event)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def delete_volunteer(volunteer_id: int) -> None:
    session = Session()
    try:
        volunteer = session.query(Volunteer).filter_by(id=volunteer_id).first()
        if not volunteer:
            raise ValueError(f"Volunteer with ID {volunteer_id} not found.")
    
        session.query(Assignment).filter_by(volunteer_id=volunteer_id).delete()
        session.delete(volunteer)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
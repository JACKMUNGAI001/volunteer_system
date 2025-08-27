from sqlalchemy.orm import sessionmaker
from model import engine, Event
from datetime import datetime

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

def get_all_events():
    session = Session()
    try:
        events = session.query(Event).all()
        return events
    finally:
        session.close()

def get_event_by_id(event_id: int):
    session = Session()
    try:
        event = session.query(Event).filter_by(id=event_id).first()
        return event
    finally:
        session.close()
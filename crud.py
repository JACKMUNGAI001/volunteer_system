from sqlalchemy.orm import sessionmaker
from model import engine

Session = sessionmaker(bind=engine)
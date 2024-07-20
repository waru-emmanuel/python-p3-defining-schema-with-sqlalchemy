#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

def main():
    engine = create_engine('sqlite:///students.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Example: Adding a student
    new_student = Student(name="John Doe")
    session.add(new_student)
    session.commit()
    session.close()

if __name__ == '__main__':
    main()

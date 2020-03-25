import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import func
 
Base = declarative_base()

class LogEvent(Base):
    __tablename__ = "log_events"
    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    time = Column(DateTime(),  default=func.now())

    def __repr__(self):
        return f"{self.time}: {self.text}"

class ModuleStatus(Base):
    __tablename__ = "module_status"
    id = Column(Integer, primary_key=True)
    detid = Column(Integer, nullable = False, unique = True)
    screwed = Column(DateTime())
    pwr_status = Column(DateTime())
    opt_status = Column(DateTime())
    tested = Column(DateTime())
    test_status = Column(String(250))
    module_id = Column(String(250))

    def __repr__(self):
        return f"detid: {self.detid}\nmech. id: {self.module_id}\nscrewed: {self.screwed}\npower: {self.pwr_status}\noptical: {self.opt_status}\ntested: {self.tested}\nresults: {self.test_status}"

def db_session(infile = 'sqlite:///dee_builder.db'):
    engine = create_engine(infile)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session

engine = create_engine('sqlite:///dee_builder.db')
DBSession = sessionmaker(bind=engine)

if __name__ == "__main__":
    engine = create_engine('sqlite:///dee_builder.db')
    Base.metadata.create_all(engine)

    # seed some fake detids
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    objects = [
        {"module_id": "1000", "detid": 419697668, "screwed": func.now(), "tested":func.now(), "test_status": "OK"},
        {"module_id": "1001", "detid": 419697676, "screwed": func.now(), "tested":func.now(), "test_status": "DEAD" },
        {"module_id": "1002", "detid": 419705860, "screwed": func.now(), "tested":func.now(), "test_status": "OK" },
        {"module_id": "1003", "detid": 419705868, "screwed": func.now(), "tested":func.now(), "test_status": "OK" },
        {"module_id": "1004", "detid": 419722244, "screwed": func.now()},
        {"module_id": "1005", "detid": 419722252, "screwed": func.now()}
        ]
    session.add_all([ModuleStatus(**data) for data in objects])
    session.commit()

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    timesheets = relationship('Timesheet', back_populates='owner')


class Timesheet(Base):
    __tablename__ = 'timesheets'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, index=True)
    amount_of_hours = Column(Integer)
    emp_id = Column(Integer, ForeignKey('employees.id'))

    owner = relationship('Employee', back_populates='timesheets')
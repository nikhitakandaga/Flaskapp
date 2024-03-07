from sqlalchemy.orm import Session

from . import models, schemas


def get_employee(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.id == emp_id).first()


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()


def create_employee(db: Session, emp: schemas.EmployeeBase):
    db_emp = models.Employee(name=emp.name)
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)

    return db_emp

def get_timesheets_by_emp_id(db: Session, emp_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Timesheet).filter(models.Timesheet.emp_id == emp_id).offset(skip).limit(limit).all()

def get_timesheets_by_emp_date(db: Session, emp_id: int, timesheet_date: str, skip: int = 0, limit: int = 100):
    return db.query(models.Timesheet).filter(models.Timesheet.emp_id == emp_id, models.Timesheet.date == timesheet_date ).offset(skip).limit(limit).all()

def create_timesheets(db: Session, timesheet: schemas.Timesheet, emp_id: int):
    db_timesheet = models.Timesheet(**timesheet.dict(), emp_id=emp_id)
    db.add(db_timesheet)
    db.commit()
    db.refresh(db_timesheet)

    return db_timesheet

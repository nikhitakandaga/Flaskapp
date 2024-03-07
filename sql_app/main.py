from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/employee/', response_model=schemas.Employee)
def create_employee(emp: schemas.EmployeeBase, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, emp=emp)


@app.get('/employees/', response_model=List[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = crud.get_employees(db, skip=skip, limit=limit)

    return employees


@app.get('/employees/{emp_id}', response_model=schemas.Employee)
def read_employee(emp_id: int, db: Session = Depends(get_db)):
    db_emp = crud.get_employee(db, emp_id=emp_id)

    if not db_emp:
        raise HTTPException(status_code=404, detail="Employee not found.")
    return db_emp

@app.post('/employees/{emp_id}/timesheet/', response_model=schemas.Timesheet)
def create_timesheet_for_emp(emp_id: int, timesheet: schemas.TimesheetCreate, db: Session = Depends(get_db)):
    return crud.create_timesheets(db=db, timesheet=timesheet, emp_id=emp_id)

@app.get('/employees/{emp_id}/timesheet/{timesheet_date}', response_model=List[schemas.Timesheet])
def read_timesheet_for_emp(emp_id: int, timesheet_date: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    timesheet = crud.get_timesheets_by_emp_date(db, emp_id, timesheet_date, skip=skip, limit=limit)
    return timesheet

@app.get('/employees/{emp_id}/timesheet/', response_model=List[schemas.Timesheet])
def read_timesheet_for_emp(emp_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    timesheet = crud.get_timesheets_by_emp_id(db, emp_id, skip=skip, limit=limit)
    return timesheet



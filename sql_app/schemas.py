from typing import List, Optional
from pydantic import BaseModel




class EmployeeBase(BaseModel):
    name: str

class Employee(EmployeeBase):
    id: int
    
    class Config:
        orm_mode = True

class TimesheetBase(BaseModel):
    date: str
    amount_of_hours: int

class TimesheetCreate(TimesheetBase):
    pass


class Timesheet(TimesheetBase):
    id: int
    emp_id: int

    class Config:
        orm_mode = True
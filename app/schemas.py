# creating schemas 

from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    name: str
    phone_number: str
    email: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    contacts: List['Contact'] = []

    class Config:
        from_attributes = True

class ContactBase(BaseModel):
    name: str
    phone_number: str

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int
    owner_id: int
    class Config:
        from_attributes = True

class SpamReportBase(BaseModel):
    phone_number: str

class SpamReportCreate(SpamReportBase):
    reported_by_id: int

class SpamReport(SpamReportBase):
    id: int
    reported_by_id: int

    class Config:
        from_attributes = True

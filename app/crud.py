# doing crude operation in the database 

from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user_by_phone(db: Session, phone_number: str):
    return db.query(models.User).filter(models.User.phone_number == phone_number).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        phone_number=user.phone_number,
        email=user.email,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_contact(db: Session, contact: schemas.ContactCreate, user_id: int):
    db_contact = models.Contact(**contact.dict(), owner_id=user_id)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def create_spam_report(db: Session, spam_report: schemas.SpamReportCreate):
    db_spam_report = models.SpamReport(
        phone_number=spam_report.phone_number, 
        reported_by_id=spam_report.reported_by_id
    )
    db.add(db_spam_report)
    db.commit()
    db.refresh(db_spam_report)
    return db_spam_report

def search_users_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name.ilike(f"%{name}%")).all()

def search_users_by_phone(db: Session, phone_number: str):
    return db.query(models.User).filter(models.User.phone_number == phone_number).all()

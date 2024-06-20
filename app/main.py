# Main file 
from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

# Fast api instance 
app = FastAPI()

# Creating  database tables
models.Base.metadata.create_all(bind=database.engine)

# geting database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

#create new user 
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_phone(db, phone_number=user.phone_number)
    if db_user:
        raise HTTPException(status_code=400, detail="Phone number already registered")
    return crud.create_user(db=db, user=user)

# retrieve a user by id 
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/users/", response_model=List[schemas.User])
def read_users(  db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

@app.post("/users/{user_id}/contacts/", response_model=schemas.Contact)
def create_contact_for_user(user_id: int, contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    return crud.create_contact(db=db, contact=contact, user_id=user_id)

@app.post("/spam/", response_model=schemas.SpamReport)
def create_spam_report(spam_report: schemas.SpamReportCreate, db: Session = Depends(get_db)):
    return crud.create_spam_report(db=db, spam_report=spam_report)

@app.get("/search/users/", response_model=List[schemas.User])
def search_users(name: str, db: Session = Depends(get_db)):
    return crud.search_users_by_name(db, name=name)

@app.get("/search/phone/", response_model=List[schemas.User])
def search_users_by_phone(phone_number: str, db: Session = Depends(get_db)):
    return crud.search_users_by_phone(db, phone_number=phone_number)

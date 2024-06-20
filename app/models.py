# Creating model for database 
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


# creating tables ( User, Contact and SpamReport) 
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone_number = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True, nullable=True)
    password = Column(String)
    contacts = relationship("Contact", back_populates="owner")

class Contact(Base):
    __tablename__ = "contacts"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone_number = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="contacts")

class SpamReport(Base):
    __tablename__ = "spam_reports"
    
    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, index=True)
    reported_by_id = Column(Integer, ForeignKey("users.id"))
    reported_by = relationship("User")

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base
from student import student_course

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", secondary=student_course, back_populates="courses")
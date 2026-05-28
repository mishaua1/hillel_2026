from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id")),
    Column("course_id", Integer, ForeignKey("courses.id"))
)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    courses = relationship("Course", secondary=student_course, back_populates="students")
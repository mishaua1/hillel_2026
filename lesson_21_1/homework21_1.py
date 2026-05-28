from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, Session
import random

engine = create_engine("sqlite:///students.db")


class Base(DeclarativeBase):
    pass


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


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", secondary=student_course, back_populates="courses")


Base.metadata.create_all(engine)
print("таблиці створені")

with Session(engine) as session:
    courses = [
        Course(name="Python"),
        Course(name="SQL"),
        Course(name="JavaScript"),
        Course(name="HTML/CSS"),
        Course(name="Git"),
    ]
    session.add_all(courses)

    students = []
    for i in range(1, 21):
        s = Student(name=f"Студент {i}", email=f"student{i}@gmail.com")
        students.append(s)
    session.add_all(students)
    session.flush()

    for student in students:
        n = random.randint(1, 3)
        student.courses = random.sample(courses, n)

    session.commit()
    print("курси і студенти додані")


with Session(engine) as session:
    new_student = Student(name="David", email="david@gmail.com")
    session.add(new_student)
    session.flush()

    course = session.query(Course).filter(Course.name == "Python").first()
    new_student.courses.append(course)

    session.commit()
    print(f"доданий студент {new_student.name} на курс {course.name}")


with Session(engine) as session:
    course = session.query(Course).filter(Course.name == "Python").first()
    print(f"\nСтуденти на курсі {course.name}:")
    for s in course.students:
        print(f"  {s.name}")

    student = session.query(Student).filter(Student.name == "David").first()
    print(f"\nКурси студента {student.name}:")
    for c in student.courses:
        print(f"  {c.name}")


with Session(engine) as session:
    student = session.query(Student).filter(Student.name == "David").first()
    student.name = "David Test"
    student.email = "david.test@gmail.com"
    session.commit()
    print(f"\nоновлено: {student.name} {student.email}")

    student_to_delete = session.query(Student).filter(Student.name == "Студент 20").first()
    session.delete(student_to_delete)
    session.commit()
    print("студента видалено")
from sqlalchemy.orm import Session
from base import engine
from student import Student
from course import Course
import random

class Client:
    def __init__(self):
        self.session = Session(engine)

    def add_courses(self):
        courses = [
            Course(name="Python"),
            Course(name="SQL"),
            Course(name="JavaScript"),
            Course(name="HTML/CSS"),
            Course(name="Git"),
        ]
        self.session.add_all(courses)
        self.session.flush()
        return courses

    def add_students(self, courses):
        students = []
        for i in range(1, 21):
            s = Student(name=f"Студент {i}", email=f"student{i}@gmail.com")
            students.append(s)
        self.session.add_all(students)
        self.session.flush()
        for student in students:
            n = random.randint(1, 3)
            student.courses = random.sample(courses, n)
        self.session.commit()
        return students

    def add_student(self, name, email, course_name):
        student = Student(name=name, email=email)
        self.session.add(student)
        self.session.flush()
        course = self.session.query(Course).filter(Course.name == course_name).first()
        student.courses.append(course)
        self.session.commit()
        print(f"доданий студент {student.name} на курс {course.name}")

    def get_students_by_course(self, course_name):
        course = self.session.query(Course).filter(Course.name == course_name).first()
        print(f"\nСтуденти на курсі {course.name}:")
        for s in course.students:
            print(f"  {s.name}")

    def get_courses_by_student(self, student_name):
        student = self.session.query(Student).filter(Student.name == student_name).first()
        print(f"\nКурси студента {student.name}:")
        for c in student.courses:
            print(f"  {c.name}")

    def update_student(self, name, new_name, new_email):
        student = self.session.query(Student).filter(Student.name == name).first()
        student.name = new_name
        student.email = new_email
        self.session.commit()
        print(f"оновлено: {student.name} {student.email}")

    def delete_student(self, name):
        student = self.session.query(Student).filter(Student.name == name).first()
        self.session.delete(student)
        self.session.commit()
        print(f"студента видалено")

    def close(self):
        self.session.close()
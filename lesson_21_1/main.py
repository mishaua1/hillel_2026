from base import Base, engine
from client import Client

Base.metadata.create_all(engine)
print("таблиці створені")

client = Client()

courses = client.add_courses()
client.add_students(courses)
print("курси і студенти додані")

client.add_student("David", "david@gmail.com", "Python")

client.get_students_by_course("Python")
client.get_courses_by_student("David")

client.update_student("David", "David Test", "david.test@gmail.com")

client.delete_student("Студент 20")

client.close()
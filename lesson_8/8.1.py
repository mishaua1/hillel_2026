class Student:
    def __init__(self, name, surname, age, gpa):
        self.name = name
        self.surname = surname
        self.age = age
        self.gpa = gpa

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa


student1 = Student("Девід", "Бекхем", 45, 99)

print(student1.name)
print(student1.surname)
print(student1.age)
print(student1.gpa)

student1.update_gpa(75)
print(student1.gpa)
from abc import ABC, abstractmethod
import math

# Завдання 1

class Employee:
    def __init__(self, name, salary, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department

class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language,
        )
        self.team_size = team_size

def test_team_lead_attributes():
    lead = TeamLead(
        name="Donald",
        salary=5000,
        department="Test",
        programming_language="Python",
        team_size=6
    )
    assert hasattr(lead, "name"), "Відсутній атрибут name"
    assert hasattr(lead, "salary"), "Відсутній атрибут salary"
    assert hasattr(lead, "department"), "Відсутній атрибут department"
    assert hasattr(lead, "programming_language"), "Відсутній атрибут programming_language"
    assert hasattr(lead, "team_size"), "Відсутній атрибут team_size"
    print("Тест пройдено!")

test_team_lead_attributes()

# Завдання 2

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return  2 * math.pi * self.__radius

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.__width = width
        self.__height = height

    def area(self) -> float:
        return self.__width * self.__height

    def perimeter(self) -> float:
        return 2 * (self.__width + self.__height)

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Такий трикутник не існує")
        self.__a = a
        self.__b = b
        self.__c = c

    def area(self) -> float:
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    def perimeter(self) -> float:
        return self.__a + self.__b + self.__c

class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return 4 * self.__side

shapes = [
    Circle(5),
    Rectangle(4, 7),
    Triangle(3, 4, 5),
    Square(6),
]

for shape in shapes:
    print(f"{shape.__class__.__name__}: площа = {shape.area():.2f}, периметр = {shape.perimeter():.2f}")
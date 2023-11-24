class Person:
    def __init__(self, *args, **kwargs):
        self.name = args[0]
        self.surname = args[1]
        self.age = args[2]

    def introduce(self):
        return f"Hello, my name is {self.name} {self.surname}, I'm {self.age}"


class Student(Person):
    def __init__(self, name, surname, age, student_id, rating):
        super().__init__(name, surname, age)
        self.student_id = student_id
        self.rating = rating

    def study(self, subject):
        return f"{self.name} is studying {subject}"

    def exam(self, subject, rating):
        return f"{self.name} has a rating {rating} in {subject}"


class Teacher(Person):
    def __init__(self, name, surname, age, teacher_id, department, salary):
        super().__init__(name, surname, age)
        self.teacher_id = teacher_id
        self.department = department
        self.salary = salary

    def teach(self, subject):
        return f"{self.name} is teaching {subject}"

    def get_salary(self):
        return f"{self.name} gets {self.salary}"


person = Person("Tom", "Ford", "50")
student = Student("Jim", "Clark", 20, "JC123", "99")
teacher = Teacher("Roman", "Jackson", "35", "RJ123",
                  "Beetroot", "100000")


print(person.introduce())

print(student.introduce())
print(student.study("Python"))
print(student.exam("Python", "200"))

print(teacher.introduce())
print(teacher.teach("Python Development"))
print(teacher.get_salary())

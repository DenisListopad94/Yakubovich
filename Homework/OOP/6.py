# в разработке ещё
class Student:

    def __init__(self, name, *marks):
        self.name = name
        print(f"{self.name} сдал экзамены")


class Teacher:
    def get(self, *marks):
        Student.__marks = marks


Denis = Student("Denis")
Ivan = Teacher()
Ivan.get(10, 8, 9)


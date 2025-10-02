class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def info(self):
        print(f"Your name is {self.name}")
        print(f"You are {self.age }years old")
        print(f"Your grade is {self.grade}")

        student1 = Student("Kasra", 13 , 11)
        student2 = Student("Mehdi", 18 , 12)

        student1.info(self)
        student2.info(self)
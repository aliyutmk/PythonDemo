class Student:
    def __init__(self,name, level, grade):
        self.name = name
        self.level = level
        self.grade = grade
    def student_details(self):
        print(self.name, self.level, self.grade)
student1 = Student("Ali", 2, 10)
student2 = Student("Ruth", 2,8)

student1.student_details()
student2.student_details()
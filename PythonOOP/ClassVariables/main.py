class Student:
    
    class_year = 2024
    num_sudents = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_sudents += 1
        
student1 = Student("Ri Nguyen", 30)
student2 = Student("Nam Nguyen", 20)
student3 = Student("Tu Thanh", 56)
student4 = Student("Van Thanh", 98)

# print(student1.name)
# print(student2.age)
# print(student1.class_year)

print(f"My graduating class of {Student.class_year} has {Student.num_sudents} students")
      

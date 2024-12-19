class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count}"

student1 = Student("South Nguyen", 3.77)
student1 = Student("North Nguyen", 3.37)
student1 = Student("West Nguyen", 3.03)
student1 = Student("East Nguyen", 2.03)

print(Student.get_count())
print(Student.get_average_gpa())

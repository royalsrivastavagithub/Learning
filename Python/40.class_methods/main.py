class Student:

    count = 0 
    gpa = 0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count = Student.count + 1
        Student.gpa = Student.gpa + gpa

    def get_info(self):
        return f"{self.name} has a gpa of {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @classmethod
    def get_total_gpa(cls):
        return cls.gpa
    
    @classmethod
    def get_average_gpa(cls):

        if cls.count == 0:
            return 0
        else:
            return cls.gpa/cls.count
    
student1 = Student("Royal",4.0)
student2 = Student("Sumit",3.9)
student3 = Student("Rohit",3.8)

print(student1.get_info())
print(student2.get_info())
print(student3.get_info())
print(f"Total number of students: {Student.get_count()}")
print(f"Total gpa: {Student.get_total_gpa()}")
print(f"Average gpa: {Student.get_average_gpa()}")

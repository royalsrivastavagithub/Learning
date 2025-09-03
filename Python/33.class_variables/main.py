class Student:

    class_year = 2025
    num_students = 0 
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Royal",22)
student2 = Student("Sumit",21)
print(student1.name)
print(student1.age)
print(student1.class_year)
print(student2.name)
print(student2.age)
print(student2.class_year)

student2.class_year = 2024
print("Changing class year of student2 to 2024")
print(student1.class_year)
print(student2.class_year)

student3 = Student("Rohit",20)
student4 = Student("shreeya",20)
print(f"Total number of students: {Student.num_students}")
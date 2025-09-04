class Employee:
    def __init__(self, name , position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} is a {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["manager", "developer", "tester"]
        return position in valid_positions
    
employee1 = Employee("John", "manager")
employee2 = Employee("Mary", "vibe_coder")
print(employee1.get_info())
print("is valid position: ",Employee.is_valid_position(employee1.position))
print(employee2.get_info())
print("is valid position: ",Employee.is_valid_position(employee2.position))
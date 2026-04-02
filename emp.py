class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
    def employee_details(self):
        print("Name of Employee:", self.name)
        print("Age of Employee:", self.age)
        print("Salary of Employee:", self.salary)
        print("Gender of Employee:", self.gender)
emp1 = Employee("John Doe", 30, 50000, "Male")
emp1.employee_details()
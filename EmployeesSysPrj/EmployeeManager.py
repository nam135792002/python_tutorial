from Employee import *
from Utility import *
from EmployeeNotFoundException import *

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        print("*" * 10 + " ADD A NEW EMPLOYEE " + "*" * 10)
        name = str(input("Enter employee name: ")).strip().title()
        age = check_input_is_integer("Enter employee age: ", 18, 65)
        salary = check_input_is_integer("Enter employee salary: ", 1000000, 100000000)

        self.employees.append(Employee(name, age, salary))

    def print_list(self):
        print("*" * 10 + " PRINT OF LIST EMPLOYEES " + "*" * 10)
        
        for employee in self.employees:
            print(employee)

    def delete_employees_with_range_age(self, age_from, age_to):
        self.employees = list(filter(lambda emp: not (age_from <= emp.age <= age_to), self.employees))
        print(f"Deleted with employee's age from {age_from} to {age_to}")

    def update_salary_by_name(self, name, salary):
        try:
            employee = self.find_employee_name(name)
            if employee is not None:
                employee.salary = salary
        except EmployeeNotFoundException as e:
            print(e)

    def find_employee_name(self, name) -> Employee:
        for employee in self.employees:
            if employee.name == name:
               return employee
        raise EmployeeNotFoundException(f"Employee with name: {name} is not found.")

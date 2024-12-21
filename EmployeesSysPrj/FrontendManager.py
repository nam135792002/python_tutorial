from EmployeeManager import *

class FrontendManager:
    def __init__(self):
        self.employees_manager = EmployeeManager()

    def print_menu(self) -> int:
        print(">" * 10 + " MENU " + "<" * 10)
        message = [">> 1. Add a new a employee.",
                   ">> 2. List all employees.",
                   ">> 3. Delete by age range.",
                   ">> 4. Update salary given a name.",
                   ">> 5. End the program"]
        print('\n'.join(message))
        return check_input_is_integer(f'Enter your choice from 1 to {len(message)}: ', 1, len(message))
    
    def run(self):
        while True:
            choice = self.print_menu()
            
            if choice == 1:
                self.employees_manager.add_employee()
            elif choice == 2:
                self.employees_manager.print_list()
            elif choice == 3:
                age_from = check_input_is_integer(">> Enter age from: ", 18, 65)
                age_to = check_input_is_integer(">> Enter age to: ", 18, 65)
                if age_from >= age_to:
                    print("Valid age from-to is invalid. Try again!")
                else:
                    self.employees_manager.delete_employees_with_range_age(age_from, age_to)
            elif choice == 4:
                name = str(input(">> Enter your name which you'd like to update: ")).strip().title()
                salary = check_input_is_integer(">> Enter your salary which you'd like to update(1,000,000 - 100,000,000): ", 1000000, 100000000)
                self.employees_manager.update_salary_by_name(name, salary)
            elif choice == 5:
                print("Thank you for your using. Good bye")
                break
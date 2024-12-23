from Specialization import *
from Utility import *

class OperationManager:
    
    def __init__(self):
        self.specs = []

    def print_menu(self):
        print(">" * 10 + " MENU " + "<" * 10)
        message = [">> 1. Add a new a patient.",
                   ">> 2. Print all patients.",
                   ">> 3. Get next patient.",
                   ">> 4. Remove a leaving patient.",
                   ">> 5. End the program"]
        print('\n'.join(message))
        return check_input_is_integer(f'Enter your choice from 1 to {len(message)}: ', 1, len(message))

    def run(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                spec_name = str(input("Enter specialization: ")).strip()
                patient_name = str(input("Enter patient name: ")).strip().title()
                patient_status = check_input_is_integer("Enter status (1 normal / 2 urgent / 3 super urgent): ")
                spec_in_list = self.find_spec(spec_name)
                if spec_in_list is not None:
                    spec_in_list.add_new_patient(patient_name, patient_status)
                else:
                    new_spec = Specialization(spec_name)
                    new_spec.add_new_patient(patient_name, patient_status)
                    self.specs.append(new_spec)

            elif choice == 2:
                for spec in self.specs:
                    print(f">> The {spec.name} has {len(spec.queue)} patients <<")
                    spec.print_all_of_patient()

            elif choice == 3:
                spec_name = str(input("Enter specialization: ")).strip()
                spec_in_list = self.find_spec(spec_name)
                if spec_in_list is not None:
                    spec_in_list.get_next_patient()
                else:
                    print(f"{spec_name} is not found in sys")

            elif choice == 4:
                spec_name = str(input("Enter specialization: ")).strip()
                spec_in_list = self.find_spec(spec_name)
                if spec_in_list is not None:
                    patient_name = str(input("Enter patient name: ")).strip().title()
                    try:
                        spec_in_list.remove_leave_patient(patient_name)
                    except PatientNotFoundException as ex:
                        print(ex)
                else:
                    print(f"{spec_name} is not found in sys")

            else:
                print("Thank you for your using. Good bye")
                break

    def find_spec(self, name) -> Specialization:
        for spec in self.specs:
            if spec.name == name:
                return spec
        return None

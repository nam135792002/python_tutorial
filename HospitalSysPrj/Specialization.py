from Patient import *
from PatientStatus import *
from PatientNotFoundException import *

class Specialization:

    MAX_CAPACITY = 5
    
    def __init__(self, name):
        self.name = name
        self.queue = []

    def add_new_patient(self, name, status):
        if len(self.queue) >= self.MAX_CAPACITY:
            print("Apologies, the queue is full for this specalization.")
            return
        
        if not status in PatientStatus._value2member_map_:
            print("Invalid status. Please select valid status!")
            return
        
        new_patient = Patient(name, status)
        self.queue.append(new_patient)
        self.queue.sort(key=lambda x : x.status, reverse=True)
        print(f"Patient: {new_patient.name} is {PatientStatus(new_patient.status).name}")

    def print_all_of_patient(self):
        for patient in self.queue:
            print(f"- Patient: {patient.name} is {PatientStatus(patient.status).name}")

    def get_next_patient(self):
        if len(self.queue) == 0:
            print(">> The spec is empty!")
        else:
            patient = self.queue.pop(0)
            print(f"Please, patient: {patient.name} go to meet doctor")
    
    def remove_leave_patient(self, name):
        for patient in self.queue:
            if patient.name == name:
                self.queue.remove(patient)
                print(f"Patient's name {name} is deleted successfully.")
                return 
        raise PatientNotFoundException(f"Patient's name {name} is not found")

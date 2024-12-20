# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

# file_path = "IOFilePython/WritingFile/output.txt"

# try:
#     with open(file_path, "w") as file:
#         for employee in employees:
#             file.write(employee + "\n")
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")

# import json

# employee = {
#     "name": "Ri Nguyen",
#     "age": 22,
#     "job": "Programmer"
# }
# file_path = "IOFilePython/WritingFile/output.json"

# try:
#     with open(file_path, "w") as file:
#         json.dump(employee, file, indent=4)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")

import csv
employees = [["Name", "Age", "Job"],
             ["Nam Nguyen", 30, "Cook"],
             ["Tay Nguyen", 22, "Programmer"],
             ["Bac Nguyen", 20, "Driver"],
             ["Ri Nguyen", 18, "Scientist"]]

file_path = "IOFilePython/WritingFile/output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")

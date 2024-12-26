from Utility import *
from Admin import *

class OperationsManager:

    def __init__(self):
        self.admin = Admin()

    def print_menu(self) -> int:
        print(">" * 10 + " MENU " + "<" * 10)
        message = [">> 1. Add a new book.",
                   ">> 2. Print library books.",
                   ">> 3. Print books by keyword.",
                   ">> 4. Add a new user.",
                   ">> 5. Borrow book.",
                   ">> 6. Return book",
                   ">> 7. Print users borrowed book",
                   ">> 8. Print users",
                   ">> 9. End the program"]
        print('\n'.join(message))
        return check_input_is_integer(f'Enter your choice from 1 to {len(message)}: ', 1, len(message))
    
    def run(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                self.admin.add_book()
            elif choice == 2:
                self.admin.print_all_books()
            elif choice == 3:
                self.admin.search_for_book()
            elif choice == 4:
                self.admin.add_user()
            elif choice == 5:
                try:
                    self.admin.borrow_book()
                except ResourceNotFoundException as e:
                    print(e)
                except AppException as e:
                    print(e)
            elif choice == 6:
                try:
                    self.admin.return_book()
                except ResourceNotFoundException as e:
                    print(e)
            elif choice == 7:
                self.admin.print_users_borrowed()
            elif choice == 8:
                self.admin.print_all_user()
            elif choice == 9:
                print("Thank you for your using. Good bye")
                break

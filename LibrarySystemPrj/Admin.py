from Book import *
from User import *
from Utility import *
from ResourceNotFoundException import *
from AppException import *

class Admin:
    def __init__(self):
        self.books = []
        self.users = {}

    def add_book(self):
        while True:
            book_id = input("Enter the book id: ")
            if self.find_book_by_id(book_id) is not None:
                print(f"With book's ID: {book_id} have ever existed.")
            else:
                break
        book_name = input("Enter the book name: ").strip().title()
        book_quantity = check_input_is_integer("Enter the book quantity: ")
        new_book = Book(book_id, book_name, book_quantity)
        self.books.append(new_book)
        print(f"Book with ID's {book_id} is added successfully!")

    def find_book_by_id(self, book_id) -> Book:
        for book in self.books:
            if book.id == book_id:
                return book
        return None
    
    def find_user_by_id(self, user_id) -> User:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def print_all_books(self):
        for book in self.books:
            print(book)

    def search_for_book(self):
        keyword = input("Enter the keyword which you are searching: ").strip()
        found_books = [book for book in self.books if keyword.upper() in book.name.upper()]
        if len(found_books) == 0:
            print(f"Not found book with keyword {keyword}")
        else:
            for book in found_books:
                print(book)

    def add_user(self):
        while True:
            user_id = input("Enter the user id: ").strip()
            if self.find_user_by_id(user_id) is not None:
                print(f"With user's ID: {user_id} have ever existed.")
            else: break
        user_name = input("Enter the user name: ").strip().title()
        user = User(user_id, user_name)
        self.users[user] = None
        print(f"Add new user with name {user_name} successfully!")

    def print_all_user(self):
        for user in self.users:
            print(user)

    def borrow_book(self):
        user_id = input("Enter the user id: ").strip()
        user = self.find_user_by_id(user_id)
        if user is None:
            raise ResourceNotFoundException(f"Not found user with ID: {user_id}")
        
        book_id = input("Enter the book id: ").strip()
        book = self.find_book_by_id(book_id)
        if book is None:
            raise ResourceNotFoundException(f"Not found book with ID: {book_id}")

        if book.quantity <= 0:
            raise AppException("Insufficient quantity!")
        
        book.quantity -= 1
        if self.users[user] is None:
            self.users[user] = [book]
        else:
            self.users[user].append(book)

        return print(f"The user {user.name} borrowed {book.name}")    

    def print_users_borrowed(self):
        users_found = {user: book for user, book in self.users.items() if book is not None}
        if len(users_found) > 0:
            for user, books in users_found.items():
                book_borrowed = ", ".join(book.name for book in books)
                print(f'The user {user.name} borrowed the books: {book_borrowed}')
        else:
            print("There are no users borrowed any book")

    def return_book(self):
        user_id = input("Enter the user id: ").strip()
        user = self.find_user_by_id(user_id)
        if user is None:
            raise ResourceNotFoundException(f"Not found user with ID: {user_id}")
        
        if not self.users[user]:
            print(f"User {user.name} has not borrowed any book.")
            return
        
        book_id = input("Enter the book id: ").strip()
        list_borrowed = self.users[user]
        book_found_borrowed = False

        for book in list_borrowed:
            if book.id == book_id:
                book.quantity += 1
                list_borrowed.remove(book)
                if not list_borrowed:
                    self.users[user] = None
                book_found_borrowed = True
                break
            
        if not book_found_borrowed:        
            print(f"Not found book with ID: {book_id} in list of borrowed.")
        else: print(f"User: {user.name} returned book successfully!")

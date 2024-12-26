class Book:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity
        
    def __str__(self):
        return f"--> ID: {self.id}, Name: {self.name}, Quantity: {self.quantity}"

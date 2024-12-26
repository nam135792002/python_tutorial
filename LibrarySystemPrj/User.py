class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"--> ID: {self.id}, Name: {self.name}"

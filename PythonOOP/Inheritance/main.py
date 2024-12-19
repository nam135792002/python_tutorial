class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")    
    
class Dog(Animal):
    def speak(self):
        print("GO GO!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak():
        print("SQUEEK!")    
   
dog = Dog("Scooby")
cat = Cat("Tom")
mouse = Mouse("Jerry")   

dog.eat()
cat.sleep()
print(mouse.is_alive)

cat.speak()
    
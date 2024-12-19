class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"This {self.name} is eating")
        
    def sleep(self):
        print(f"This {self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabit = Rabbit("Bug")
hawk = Hawk("Debug")
fish = Fish("Fix")

hawk.hunt()
rabit.eat()
hawk.sleep()

fish.flee()

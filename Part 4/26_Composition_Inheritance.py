
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal): # is-a Relationship
    def bark(self):
        print("Barking...")

# rocky = Dog()
# rocky.eat()


class Engine:
    def start(self):
        print("Engine Started....")

class ElectricEngine(Engine):
    def start(self):
        print("Electric Engine Started....")


class Car():
    def __init__(self,engine):
        self.engine = engine() # has-a Relationship
    
    def drive(self):
        self.engine.start()
        print("Car is moving...")

# car = Car(ElectricEngine)
# car.drive()

# When Inheritance makes sense:
# Clear hierarchy ho
# Example: Human -> Employee -> Manager

# When Composition makes sense:
# jb ek object multiple components se bana ho
# Example: Computer -> RAM, CPU, SSD




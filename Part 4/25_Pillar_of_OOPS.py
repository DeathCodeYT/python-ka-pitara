# 1. Single Inheritance
# class Animal:
#     def eat(self):
#         print("Eating...")

# class Dog(Animal):
#     def bark(self):
#         print("Barking...")

# rocky = Dog()
# rocky.eat()

# 2. Multiple Inheritance
# class Father:
#     def height(self):
#         print("Height is 6 Feet.")

# class Mother:
#     def skin_color(self):
#         print("Skin color is fair.")

# class Child(Father,Mother):
#     def brain_power(self):
#         print("Intelligent")

# boy = Child()
# boy.height()
# boy.skin_color()
# boy.brain_power()

# Multilevel Inheritance
# class Vehicle:
#     def __init__(self):
#         print("From Vehicle class")
#     def engine(self):
#         print("Engine is running...")

# class Car(Vehicle):
#     def __init__(self):
#         super().__init__()
#         print("From Car class")
#     def drive(self):
#         print("Car is moving...")

# class ElectricCar(Car):
#     def __init__(self):
#         super().__init__()
#         print("From Electric Car class")
#     def charging(self):
#         print("Car is Charging...")

# swift = Car()
# swift.engine()
# swift.drive()

# tesla = ElectricCar()

# tesla.engine()
# tesla.drive()
# tesla.charging()

# class GameCharacter:
#     def __init__(self,name,hp,weapon):
#         self.name = name
#         self.__hp = hp # Private Variable
#         self.weapon = weapon
    
#     def get_hp(self):
#         return self.__hp
#     def set_hp(self,hp):
#         if hp > 0:
#             self.__hp = hp
    
# class Warrior(GameCharacter):
#     def attack(self):
#         print(f"{self.name} attacks with {self.weapon}")

# class Maze(GameCharacter):
#     def __init__(self, name, hp):
#         super().__init__(name,hp,"Fireball")
#         self.mana = 100
#     def attack(self):
#         if self.mana < 20:
#             print("You dont have enough mana")
#             return
#         self.mana -= 20
#         print(f"{self.name} is attacks with Fireball🔥")

# class Archer(GameCharacter):
#     def __init__(self, name, hp):
#         super().__init__(name, hp, "Arrows")
#         self.arrows = 50
#     def attack(self):
#         if self.arrows < 1:
#             print("No arrows left.")
#             return
#         self.arrows -= 1
#         print(f"{self.name} is attacks with Arowws🏹")


# # w1 = Warrior("Arjun",1000,"Bow & Arrows")

# # w1.attack()
# # print(w1.get_hp())
# m1 = Maze("Gerlat",100)
# m1.attack()
# m1.attack()
# m1.attack()
# m1.attack()
# m1.attack()
# m1.attack()
# m1.attack()
# print(m1.mana)
# a1 = Archer("Eklavya",200)
# a1.attack()
# a1.attack()
# a1.attack()
# print(a1.arrows)



# class Bird():
#     def fly(self):
#         print("Bird is flying")

# class Penguin(Bird):
#     def fly(self):
#         print("Penguins cant fly, they swim.")

# p1 = Penguin()
# p1.fly()


# class A:
#     def process(self):
#         print("Processing from A")
# class O:
#     def process(self):
#         print("Processing from O")
# class B(A):
#     # def process(self):
#     #     print("Processing from B")
#     pass
    
# class C(A):
#     # def process(self):
#     #     print("Processing from C")
#     pass

# class D(B,C):
#     pass

# d = D()
# d.process()
# print(D.mro())


# class Parent:
#     def show(self):
#         self.goldCoin = 2
#         print("This is the parent class")

# class Child(Parent):
#     def show(self):
#         super().show()
#         self.silverCoin = 4
#         print("This is the child class")

# c = Child()
# c.show()
# print(c.silverCoin)

# 🧠 OOP Practice Questions (Beginner Level)
# 🔹 1. Classes & Objects:
# Q1:
# Create a class Car that has two attributes: brand and model.
# Write an __init__ method and a function display_info() that prints the car details.
# Then create two objects of this class.

# 🔹 2. self and __init__:
# Q2:
# What is the role of self in Python classes?
# Explain with a small example class Student with attributes name and grade.

# 🔹 3. Inheritance + super():
# Q3:
# Create a base class Animal with a method speak().
# Now create a class Dog that inherits from Animal and overrides the speak() method.
# Use super() inside the Dog class to also call the speak() method of Animal.

# 🔹 4. Polymorphism:
# Q4:
# Create a class Bird with a method make_sound().
# Then create two subclasses: Sparrow and Peacock that override make_sound() in their own way.
# Write a loop that calls make_sound() for each object and observe polymorphism in action.

# 🔹 5. MRO (Method Resolution Order):
# Q5:
# Create 3 classes: A, B, and C, where:

# B inherits from A

# C inherits from B

# Add a method show() in all three classes that prints class name.
# Create an object of class C and call show() method.
# Observe which method is called and explain why.

# ✅ BONUS (Concept Check Questions)
# Q6: What is the difference between a class and an object in your own words?
# Q7: How is super() useful in inheritance?
# Q8: What is Polymorphism in one line, and how do you use it in Python?
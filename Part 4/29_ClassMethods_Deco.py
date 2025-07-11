
# class School:
#     school_name = "Orange valley High School"

#     @classmethod
#     def get_school_name(cls):
#         return cls.school_name
    
#     @classmethod
#     def set_school_name(cls,school_name):
#         cls.school_name = school_name

# s1 = School()
# s1.school_name = "DeathCode School"
# print(s1.get_school_name())
# # print(School.get_school_name())
# School.set_school_name("Deathcode 2 School")
# print(s1.get_school_name())


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_year(cls,name,birth_year):
#         age = 2025-birth_year
#         return cls(name,age)

# p1 = Person("Rahul",34)

# print(p1.age,p1.name)
# p2 = Person.from_birth_year("Vivek",1998)
# print(p2.age,p2.name)


# class MathOperations:

#     @staticmethod
#     def add(x,y):
#         return x+y

# print(MathOperations.add(34,43))


# class Validator:

#     @staticmethod
#     def is_even(number):
#         return number % 2 == 0

# print(Validator.is_even(57))


# class Circle:
#     def __init__(self,radius):
#         self._radius = radius

#     @property # (getter)
#     def radius(self):
#         return self._radius
    
#     @radius.setter # (Setter) Syntac => @<property>.setter 
#     def radius(self,v):
#         if v < 0:
#             raise ValueError("Radius Cannot be negative.")
#         self._radius = v

# c = Circle(56)

# print(c.radius)

# c.radius = 88

# print(c.radius)



# class Temprature:
#     def __init__(self,celsius):
#         self._celsius = celsius

#     @property
#     def fahernheit(self):
#         return (self._celsius*9/5)+ 32 

#     @property
#     def celsius(self):
#         return self._celsius
    
#     @celsius.setter
#     def celsius(self,v):
#         self._celsius = v

#     @fahernheit.setter
#     def fahernheit(self,v):
#         self._celsius = (v-32)*5/9


# temp = Temprature(45)

# # print(temp.fahernheit)
# # print(temp.celsius)

# temp.fahernheit = 113

# print(temp.fahernheit)
# print(temp.celsius)


# 1. classmethod

    # Question 1:
    # Create a class called Car that has a class variable total_cars which tracks the number of cars created. Use a classmethod to increment and display the total number of cars each time a new car is instantiated.

    # Question 2:
    # Write a class Person with a classmethod called from_string(cls, person_string) that takes a string like "John,25" and returns an instance of Person with name and age attributes.

# 2. staticmethod

    # Question 1:
    # Create a class MathOperations with a staticmethod called is_prime(number), which takes an integer and returns True if the number is prime, otherwise returns False.

    # Question 2:
    # Write a class Temperature with a staticmethod called convert_celsius_to_fahrenheit(celsius), which converts a given temperature in Celsius to Fahrenheit.

# 3. property Decorators

    # Question 1:
    # Create a class Circle that has an instance variable radius. Use a property decorator to calculate and return the area of the circle when accessed as circle_instance.area.

    # Question 2:
    # Write a class Person with a property called full_name that combines the first_name and last_name attributes. Make sure it returns a full name when accessed.



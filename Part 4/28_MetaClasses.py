
# Metaclass = class of a class
# class Person:
#     def eat(self):
#         print("yum yum...")

# class CustomMeta(type):
#     def __new__(cls,name,bases,attrs):
#         print(f"Creating class: {name}")
#         if "school" not in attrs:
#             raise Exception("'school' attr is not provided")
#         bases = (Person,)
#         return super().__new__(cls,name,bases,attrs)

# class Student(metaclass=CustomMeta):
#     school = "ABC School"
# class Graduated(Student):
#     school = "G School"
# Graduated().eat()


class SingletonMeta(type):
    _instances = {}
    def __call__(cls,*args,**kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args,**kwargs)
        return cls._instances[cls]

        


class MongoDB(metaclass=SingletonMeta):
    pass

class MySQL(metaclass=SingletonMeta):
    pass

db1 = MySQL()
db2 = MySQL()





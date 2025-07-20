
import sys
class NormalStudent:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class SlotStudent:
    __slots__ = ['name','age']
    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = NormalStudent("Kabutar",2)
s2 = SlotStudent("Kabutar",2)
# s1.grade = "A"
# print(s1.__dict__)
# print(s1.name,s1.age)

print(sys.getsizeof(s1.__dict__))
print(sys.getsizeof(s2))
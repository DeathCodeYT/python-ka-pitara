
# print(5+10) # Output: 15
# print("Hello"+" DeathCode") # Output: Hello DeathCode

# *, ==, +,-,/,<,>,[],()

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return 56

    
pyBook = Book("Python ka Pitara","DeathDcode")
jsBook = Book("JS Journey","DeathDcode")
l = [1,3,5,454,34]
# print(pyBook)
# print(jsBook)


# print(len(pyBook))



# Operator Overloading
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x},{self.y})"
    
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    
    def __lt__(self,other):
        return self.x<other.x and self.y < other.y
    
v1 = Vector(2,3)
v2 = Vector(4,5)

v3 = v1 + v2

# print(v1)
# print(v2)
# print(v3<v1)


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def __lt__(self,other):
        return self.marks < other.marks
    
    def __str__(self):
        return f"Student({self.name},{self.marks})"
    
    def __repr__(self):
        return f"Student({self.name},{self.marks})"

# s1 = Student("Aman",85)
# s2 = Student("Ravi",90)

# print(sorted([s2,s1]))

class Counter:
    def __init__(self):
        self.count = 0
    
    def __call__(self):
        self.count += 1
        print(f"Count: {self.count}")
    

c = Counter()

c()
c()
c()
c()

print(c.count)



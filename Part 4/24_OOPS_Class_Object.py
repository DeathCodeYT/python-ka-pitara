# class Cookie:
#     def __init__(self,aata,flavour,shape):
#         self.aata = aata
#         self.flavour = flavour
#         self.shape = shape

#     def detail(self):
#         print(f"This cookie is made of {self.aata} flour, has {self.flavour} flavour, and is {self.shape} in shape.")

# c1 = Cookie('wheat','chocolate','bar')
# c2 = Cookie('maida','vanila','heart')

# c1.detail()
# c2.detail()

# class GameCharacter:
#     def __init__(self,weapon):
#         self.weapon = weapon

#     def print_self(self):
#         print(self)

# archer = GameCharacter("arrows")
# wizard = GameCharacter("magic")
# archer.power = 45
# print(archer.weapon)
# print(archer.weapon)
# print(archer)
# archer.print_self()

class Car:
    wheels = 4 # class attribute

    def __init__(self,color):
        self.color = color # instance attribute

car1 = Car("Red")
car2 = Car("Blue")
car2.wheels = 7

print(car1.color,car1.wheels)
print(car2.color,car2.wheels)

print(Car.wheels)



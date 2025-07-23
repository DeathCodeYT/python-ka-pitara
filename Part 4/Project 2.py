# Animal Kingdom Simulator

class Animal:
    def __init__(self,name):
        self.name = name
    def make_sound(self):
        print(f"{self.name} makes a genric sound.")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Pet:
    def __init__(self,owner):
        self.owner = owner
        print(f"Pet has owner: {self.owner}")
    
    def play(self):
        print(f"Playing with {self.owner}")
    
    def make_sound(self):
        print("Pet makes a happy sound")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    
    def make_sound(self):
        print(f"{self.name} (a {self.breed}) says Woof! Woof!")

    def fetch(self,item):
        print(f"{self.name} is fetching the {item}")

class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color = color
    
    def make_sound(self):
        print(f"{self.name} (a {self.color}) says Meow! Meow!")

class ServiceDog(Dog,Pet):
    def __init__(self, name, breed,owner,service_type):
        Dog.__init__(self,name,breed)
        Pet.__init__(self,owner)
        self.service_type = service_type
        print(f"{self.name} is a {self.service_type} service dog")

    def assist_owner(self):
        print(f"{self.name} is assisting {self.owner} with {self.service_type} duties.")
    
    def make_sound(self):
        print(f"{self.name} (Service Dog) gives a gentle bark!")

my_dog = Dog("Pari","Indian Spitz")
my_dog.make_sound()
my_dog.fetch("bone")
my_dog.sleep()

my_cat = Cat("Meera","white")
my_cat.make_sound()
my_cat.sleep()

# animals = [my_dog,my_cat,Animal("Miko")]

# for animal in animals:
#     animal.make_sound()

service_buddy = ServiceDog('Max',"German Shepherd",'Jatin',"Guide")

service_buddy.make_sound()
service_buddy.assist_owner()
service_buddy.play()


print("--- MRO for Service Dog ---")
print(ServiceDog.__mro__)
# Function Syntax

# def function_name(parameters):
#     #code block
#     return

# def => Keyword jo function ko define krta hai
# function_name => function ka name
# parameters => input (optional)
# return => output (optional)


# Type of Functions
# 1. Without Parameters and without return
# 2. With Parameters and without return
# 3. Withnot Parameters and with return
# 4. With Parameters and with return

def say_hello():
    print("Hello")

# say_hello()

def greet(name="Guest"):
    print("Hello,",name)

# greet("DeathCode")

def add7and4():
    return 7+4

# t = add7and4()
# print(t)

def add(a,b):
    return a+b

# print(add(7,8))

# prtReturn = print("Dekhte hai kya return hoyega")

# print(prtReturn)\

def avg(x,y,z):
    return (x+y+z)//3

# print(avg(43,65,29))
# print(avg(45,77))

# greet("DeathCode")


def intro(name,age,phone):
    print(name,"is",age,"years old and PHone:",phone)
# intro("DeathCode",phone=234234,age=99)

intro2 = intro
myprint = print
# intro2("DeathCode",12,"1234")

# myprint("hello kese ho sab, abhi tk video ko like nhi kiya kya?")
print(len([3,4,5,6]))

print(sum([134,46,2,45]))


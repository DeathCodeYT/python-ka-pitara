# def fun(*args,**kwargs)

# def greet(name,age):
#     print(f"Hello {name}, you are {age} years old.")

def addNumbers(*num):
    print(sum(num))

# addNumbers(23,44,55)

def displayInfo(**data):
    for item in data.values():
        print(item)

# displayInfo(name="DeathCode",age=67,comments=["I like this tutorial","Subscribe bhi krdo"])


def mixed(a,*args,**kwargs):
    print(a,args,kwargs)

# mixed(67,234,"askldj","4345",99,k=88,uu=99)

# * => tuple
# ** => dict

data = (1,2,3)

def fun(a,b,c):
    print(a,b,c)

# fun(*data)

def display_info(name,age):
    print(f'{name} and {age}.')

data = {"name":"Death","age":56}

# display_info(**data)


def log_events(eventType,*details,**meta):
    print(f"[{eventType}] => Details: {details} | Metadata: {meta}")

# log_events("LOGIN","user1234","1234",ip="192.168.1.1",device="mobile")




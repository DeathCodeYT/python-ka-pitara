


def greet(name,age):
    print(f"Hello {name}, You are {age} years old.")

# greet("Death",300)


def addNumbers(*args):
    argList = list(args)
    print(sum(args),argList)

# addNumbers(1,3,4,454,234,2,5,456,45)
# data = (1,2,3,4,5,6,7)
# addNumbers(*data)


def displayInfo(**data):
    print(data)
data = {
    "name":"DeathCode",
    'susb':"1M"
}
# displayInfo(**data)
# displayInfo(a=8,b=9,name="DeathCode",subs="1M")

def mixed(a,*args,b,**kwargs):
    print(a,args,b,kwargs)

# mixed(45,33,233,2349,b=78,name="DeathCode")

def log_event(event_type,*details,**meta):
    print(f"{event_type} => Details: {details} |  Metadata: {meta}")

log_event("LOGIN","user1234","1234",device="mobile",ip="192.168.1.1")


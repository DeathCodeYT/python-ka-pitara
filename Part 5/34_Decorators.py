

# def decorator_function(original_function):
#     def wrapper_function(*args,**kwargs):
#         print("Wrapper executed this before the original function")
#         original_function(*args,**kwargs)
#         print("Wrapper executed this after the original function")
#     return wrapper_function

# @decorator_function
# def display_info(name,age):
#     print(f"Name: {name},Age: {age}")

# display = decorator_function(display)


# display_info("Ravi",25)


# 1. Logging - Auto Track function call

# def logger(func):
#     def wrapper(*args,**kwargs):
#         print(f"Executing '{func.__name__}' with arguments: {args} {kwargs}")
#         return func(*args,**kwargs)
#     return wrapper

# @logger
# def add(x,y):
#     return x+y

# print(add(34,56))
# print(add(498,78))

# from functools import wraps
# 2. Authentication - Access control layer
# def require_authentication(func):
#     @wraps(func)
#     def wrapper(user):
#         if not user.get("is_authenticated"):
#             print("User is not authenticated")
#             return
#         return func(user)
#     return wrapper

# @require_authentication
# def show_profile(user):
#     """This is documentation string of this function"""
#     print(f"Welcome, {user['name']}")

# user1 = {"name":"Ravi",'is_authenticated':False}
# user2 = {"name":"Ajay",'is_authenticated':True}

# print(show_profile.__doc__)
# print(show_profile.__name__)
# show_profile(user1)
# show_profile(user2)




def deco1(func):
    def wrapper():
        print("Deco 1")
        func()
    return wrapper

def deco2(func):
    def wrapper():
        print("Deco 2")
        func()
    return wrapper

@deco2
@deco1
def say_hello():
    print("Hello, Deathcode")

# say_hello = deco1(deco2(say_hello))

say_hello()


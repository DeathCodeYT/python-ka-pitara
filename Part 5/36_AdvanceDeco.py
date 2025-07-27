
# def simple_deco(func):
#     def wrapper(*args,**kwargs):
#         print(f"--- Calling '{func.__name__}' ---")
#         result = func(*args,**kwargs)
#         print(f"--- '{func.__name__} Finished' ---")
#         return result
#     return wrapper

# @simple_deco
# def calculate_area(l,w):
#     return l*w

# print(f"Area: {calculate_area(5,10)}")


# def repeat_call(n):
#     def deco(func):
#         def wrapper():
#            for i in range(n):
#                print(f"Executing '{func.__name__}' times({i+1}) :'")
#                func()
#         return wrapper
#     return deco

# @repeat_call(3)
# def say_hello():
#     print("Hello, Deathcode")

# say_hello()

import time
from functools import wraps

# def rate_limit(max_calls,period):
#     def deco(func):
#         call_times = [] # 001
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             now = time.time()
#             call_times[:] = [t for t in call_times if now - t < period]
#             if len(call_times) >= max_calls:
#                 wait_duration = period - (now - call_times[0])
#                 print(f"Rate limit exceeded for '{func.__name__}'. Waiting for {wait_duration:.2f}s ")
#                 time.sleep(wait_duration)
#                 call_times.pop(0)
#             call_times.append(time.time())
#             print(f"Calling '{func.__name__}'. Calls in window: {len(call_times)}/{max_calls}")
#             return func(*args,**kwargs)            
#         return wrapper
#     return deco


# @rate_limit(max_calls=2,period=5)
# def fetch_user_profile(user_id):
#     print(f"Fetching profile for user: {user_id}")
#     return {'id':user_id,'user':f"User_{user_id}"}


# class LoggingDecorator:
#     def __init__(self,func):
#         self.func = func
#         self.call_count = 0
#         print(f"LoggingDecorator initialized for '{func.__name__}'.")
    
#     def __call__(self, *args, **kwds):
#         self.call_count += 1
#         print(f"Log: Calling '{self.func.__name__}. ")
#         result = self.func(*args,**kwds)
#         print(f"Log: '{self.func.__name__}' returned '{result}'")
#         return result

# @LoggingDecorator
# def perform_calculation(x,y):
#     return x + y

# @LoggingDecorator
# def send_email(x,y):
#     return x * y
# perform_calculation = LoggingDecorator(perform_calculation)

# print(perform_calculation(5,6))

# class AuthGuardMeta(type):
#     def __getitem__(self,required_role):
#         print(f"AuthGuard configured for role: '{required_role}'")
#         def deco_for_method(func):
#             @wraps(func)
#             def wrapper(user_obj,*args,**kwargs):
#                 if user_obj.get('role') == required_role:
#                     print(f"Access granted for {user_obj['username']}({user_obj['role']})")
#                     return func(user_obj,*args,**kwargs)
#                 else:
#                     print(f"Access DENIED for {user_obj['username']}.")
#                     return None
#             return wrapper
#         return deco_for_method

# class AuthGuard(metaclass=AuthGuardMeta):
#     def __init__(self,default_role="guest"):
#         self.default_role = default_role
#         print(f"AuthGuard initialized with default role: {default_role}")

#     def __call__(self, func):
#         @wraps(func)
#         def wrapper(user_obj,*args,**kwargs):
#             if user_obj.get('role') == self.default_role:
#                 print(f"Default Access granted for {user_obj['username']} ({self.default_role})")
#                 return func(user_obj,*args,**kwargs)
#             else:
#                 print(f"Default access denied for {user_obj['username']}.")
#                 return None
#         return wrapper

#     def __getitem__(self,required_role):
#         print(f"AuthGuard configured for role: '{required_role}'")
#         def deco_for_method(func):
#             @wraps(func)
#             def wrapper(user_obj,*args,**kwargs):
#                 if user_obj.get('role') == required_role:
#                     print(f"Access granted for {user_obj['username']}({user_obj['role']})")
#                     return func(user_obj,*args,**kwargs)
#                 else:
#                     print(f"Access DENIED for {user_obj['username']}.")
#                     return None
#             return wrapper
#         return deco_for_method
    

# user_admin = {'username':"DeathCode",'role':'admin'}
# user_editor = {'username':'Sagar','role':'editor'}
# user_guest = {'username':'Harshit','role':'guest'}

# @AuthGuard()
# def view_public_page(user):
#     print(f"Viewing publig page as {user['username']}.")


# @AuthGuard['editor']
# def edit_article(user):
#     print(f"Editing article page as {user['username']}.")

# view_public_page(user_guest)
# edit_article(user_editor)

def make_immutable(cls):
    original_setattr = cls.__setattr__
    def new_setattr(self,name,value):
        if hasattr(self,'_initialized') and self._initialized:
            raise AttributeError(f"Cannot modify attribute '{name}'.")
        original_setattr(self,name,value)

    cls.__setattr__ = new_setattr

    original_init = cls.__init__
    @wraps(original_init)
    def wrapper_init(self,*args,**kwargs):
        original_init(self,*args,**kwargs)
        original_setattr(self,"_initialized",True)
    cls.__init__ = wrapper_init
    print(f"Class '{cls.__name__}' made immutable")
    return cls
    

@make_immutable
class Config:
    def __init__(self,version,debug_mode):
        self.version = version
        self.debug_mode = debug_mode
    
    def display(self):
        print(f"Config: Version={self.version}, Debug={self.debug_mode}")


app_config = Config("1.0.0",True)

app_config.display()

app_config.version = "1.0.4"
# app_config.display()


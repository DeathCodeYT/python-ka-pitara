

# def outer_function():
#     print("Outer function is running")
#     li = 9
#     def inner_function():
#         print(li)
#         print("Inner Function is running")
    
#     return inner_function


# closure_instance = outer_function()
# closure_instance()


# def counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     return increment

# c1 = counter()
# print(c1())
# print(c1())
# print(c1())
# print(c1())
# print(c1())

# 1. Data Encapsulation wihtout classes
# def make_muliptlier(x):
#     def multiplier(n):
#         return x*n
#     return multiplier

# times10 = make_muliptlier(10)
# print(times10(6))
# print(times10(89))
# print(times10(7))
# times45 = make_muliptlier(45)
# print(times45(2))
# print(times45(56))
# print(times45(978))

# 2. Factory Functions - Dynamic Function Creators
# def html_tag(tag):
#     def wrap_text(msg):
#         return f"<{tag}>{msg}</{tag}>"
#     return wrap_text

# h1 = html_tag("h1")
# div = html_tag("div")

# print(h1("Welcome to Python ka pitara"))
# print(div("Welcome to Python ka pitara"))


def outer(func):
    def inner():
        print("Before function execution")
        func()
        print("After function execution")
    return inner

@outer
def display():
    print("Display Function is running")

display()




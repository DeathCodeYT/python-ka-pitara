
# def fun():
#     age = 45

#     def innerFun():
#         innerAge = 56
#         print("Innter Function age:",innerAge)
#         print("Outer age from inner Function",age)
#     innerFun()
#     print("Outer Function Funciton:",age)
#     return

# fun()
# innerFun()

# print(age) # => It will give NameError

# if 48>5:
#     age = 56

# print(age)

# LEGB Rule
# L=> Local Scope
# E=> Enclosed Scope
# G=> Global Scope
# B=> Built - in Scope


# x = "global"

# func()
# def func():
#     global x
#     x = "local"
#     print(x)

# func()
# print(x)


add = lambda a,b: a+b
print(add(45,54))


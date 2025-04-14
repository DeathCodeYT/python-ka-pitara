# List Comprehensions 

# [expression for item in iterable if condition]


arr1 = []
# for i in range(1,11):
#     if i>5:
#         arr.append(i**2)

# arr = [i**2 for i in range(1,11) if i>5]
# [
#     (1,0),
#     (1,1),
#     (2,0),
#     (2,1),
#     (3,0),
#     (3,1),
# ]
for i in range(1,4):
    for j in range(2):
        arr1.append((i,j))

arr2 = [(i,j) for i in range(1,4) for j in range(2)]

# print(arr1)
# print(arr2)

# Dic Comprehensions

# {key:value for item in iterable} => dict comprehensions syntax
dict1 = {}
for x in range(1,6):
    dict1[x]=x*2

dict2 = {x:x*2 for x in range(1,6) if x > 2}
# print(dict1)
# print(dict2)


# text = "banana"
# freq = {ch:text.count(ch) for ch in text}
# print(freq)

# Set Comprehensions

# {expression for item in iterable}

# text = "Hello, DeathCode World"

# unique_chars = {ch for ch in text if ch != " "}
# print(unique_chars)


# Short hand if-else
age = 17

# status = None
# if age >= 18:
#     status = "Adult"
# else:
#     status = "Child"

# status = "Adult" if age >= 18 else "Child"

# print(status)


# Short hand Function
# var = lambda args: expression => expression always return automatically

isEven = lambda x: x%2 == 0

print(isEven(7))



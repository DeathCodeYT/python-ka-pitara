
# map() => Apply a function to each item in an iterable (The Transformer)
# def sq(n):
#     return n**2

# def myMap(func,it):
#     items = []
#     for i in it:
#         val = func(i)
#         items.append(val)
#     return items

# nums = [1,2,3,4]
# squares = list(map(lambda x:x**2,nums))
# print(squares)

# filter() => Keep only values that pass a condition (The Bouncer)
# def myFilter(func, it):
#     items = []
#     for i in it:
#         if func(i):
#             items.append(i)
#     return items
# def isEven(x):
#     return x%2 == 0

# nums = [x for x in range(1, 101)]
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)

# zip() => Combine multiple iterables element-wise (The Zipper)
# names = ["Rahul","Amit","Mandeep"]
# marks = [44,23,89]

# combined = list(zip(names,marks))
# print(combined)
# a,b = zip(*combined)
# print(a,b)

# enumerate() => Add index to iterable (Index Manager)
# fruits = ["apple","banana","cherry"]
# for idx,fruit in enumerate(fruits):
#     print(fruit,idx)

# any() => Returns True if any one item is True (Truth Checkers)
# bools = [False, False, True]
# print(any(bools))

# all() => Returns True if all items are Ture (Truth Checkers)
# bools = [True, True, True]
# print(all(bools))

students = ["Ram", "Shyam", "Anjali"]
marks = [90, 45, 60]

# result = zip(students,marks)
# result = filter(lambda x: x[1]>=50,result)


result = list(filter(lambda x: x[1] >= 50, zip(students, marks)))

print(result)


def sq(x):
    return x**2

# 1. map() => The Transformer

nums = [1,2,3,4]
squares = list(map(lambda x:x**2,nums))

# def myMap(fun,iter):
    # l1 = []
    # for n in iter:
    #     l1.append(fun(n))
    # return l1

# squares = myMap(lambda x:x**2,nums)

# print(squares)

# 2. filter() => The Bouncer

nums = [x for x in range(1,11)]
# evens = list(filter(lambda x:x%2==0,nums))

# def myFilter(fun,iter):
#     l1 = []
#     for item in iter:
#         if fun(item):
#             l1.append(item)
#     return l1

# print(myFilter(lambda x:x%2==0,nums))

squares_even = map(lambda x:x**2,filter(lambda x:x%2==0,nums))
# print(list(squares_even))




# 3. zip() => The Zipper
names=["A","B","C"]
marks=[56,67,89]

combined = list(zip(names,marks))
# print(combined)

a,b = zip(*combined)
# print(a,b)

# 4. enumerate() => Index Manager
fruits = ['apple','banana','cherry']
# for idx,fruit in enumerate(fruits,start=5):
#     print(idx,fruit)

# print(list(enumerate(fruits,start=1)))

# 5. any() & all() => Truth Checker

bools = [True,True,True]
# print(any(bools))
# print(all(bools))


# ages = [21,34,18]

# all_adults = all([age>=18 for age in ages])

# print(all_adults)


students = ['ram','shyam','geeta']
marks = [90,45,60]

result = list(filter(lambda x: x[1] >= 50,zip(students,marks)))

print(result)



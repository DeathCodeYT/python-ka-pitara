# Immutable ------------------
# a = 10
# print(id(a))
# a = 20
# print(id(a))
# x = 'hello'
# print(id(x))
# x = x.upper()
# print(id(x))


# Mutable ------------------
# list1 = [1,2,3,4]
# print(id(list1))
# list1.append(57)
# print(id(list1))
# print(list1)

# dict1 = {"a":2}
# dict2 = dict1

# dict1['b'] = 3

# print(dict2)


# l1 = ['a','b','c']
# l2 = l1
# s1 = "abc"
# s2 = s1

# l2.append('d')
# s2 = "abcd"

# print(f"List1 id:{id(l1)} list2 id: {id(l2)}")
# print(f"Str1 id:{id(s1)} Str2 id: {id(s2)}")

# import sys
# list1 = [1,2,3,4]
# print(sys.getsizeof(list1))


# d1 = {
#     "name":"Deathcode",
#     34: '43',
#     (1,2,3):"123"
# }

# print(d1[(1,2,3)])


import copy

l = [1,2,3,["h","e"]]
# l2 = [x for x in l]
# l2 = copy.copy(l)
l2 = copy.deepcopy(l)

print(id(l[3]),id(l2[3]))



# def func():
#     a = 10 # 'a' Stack memory
#     b = [1,2] # 'b' Heap memory
#     return b

# func()
# b = func()
# print(id(b))



import sys

# a = [1,2,3,4]
# b = a
# c = b
# print(sys.getrefcount(a))

# import gc
# class A:
#     def __init__(self,name):
#         self.name = name
#         self.ref = self

# a1 =A("Deathcode")
# del a1
# gc.collect()
# print(gc.get_objects())


# gc.disable()
# # havey memory task

# gc.enable()


# a = [1,2]
# b = [1,2]

# print(id(a),id(b))


import tracemalloc

tracemalloc.start()
# falskdjf
print(tracemalloc.get_traced_memory())
tracemalloc.stop()
# pympler, objgraph, memory_profiler
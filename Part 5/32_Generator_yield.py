

# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
#     yield 4

# gen = simple_generator()


# def get_number():
#     return [1,2,3,4,5]

# print(get_number())

# def generate_numbers():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# for num in generate_numbers():
#     print( num)



# 1. Infinite Sequences:
# def infinite_counter():
#     n = 0
#     while True:
#         yield n
#         n += 1

# c1 = infinite_counter()


# print(next(c1))
# print(next(c1))
# print(next(c1))
# print(next(c1))


# 2. Reading large Files
# def read_large_file(file_path):
#     with open(file_path,'r') as file:
#         for line in file:
#             yield line

# for line in read_large_file('data.txt'):
#     print(line)


# 3. Efficient Data Processing:
# def even_numbers(n):
#     for i in range(n):
#         if i%2 == 0:
#             yield i

# for nums in even_numbers(34):
#     print(nums)



# squares = [x*x for x in range(5)]
# print(squares)

# squares_gen = (x*x for x in range(5))
# print(next(squares_gen))
# print(next(squares_gen))
# print(next(squares_gen))


# import time

# def live_data_stream():
#     data = 0
#     while data< 5:
#         data+=1
#         yield f"Data Pakcet {data}"
#         time.sleep(1)



# for packets in live_data_stream():
#     print(packets)
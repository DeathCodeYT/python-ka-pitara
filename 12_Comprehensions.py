
# new_list = []
# for i in range(10):
#     if i%2 ==0:
#         new_list.append(i**2)

# new_list = [i for i in range(10) if i%2==0]
# print(new_list)

# List Comprehension Syntax
# [expression for item in iterable if condition]

def sq(n):
    return n**2

l = [sq(x) for x in range(1,11)]
# print(l)

# l= [(x,y) for x in range(1,4) for y in range(1,3)]
# l= ['Even' if x%2==0 else "Odd" for x in range(1,11)]


# print(l)

matrix = [
    [1,2],
    [3,4],
    [5,6]
]

flat = [num for row in matrix for num in row]

# print(flat)

# Dic Comprehensions
# {key:value for item in iterbale} => Syntax

# squares = { x: "EVEN" if x%2==0 else "ODD" for x in range(1,11)}
# print(squares)

# text = "banana"

# freq = {ch: text.count(ch) for ch in text}
# print(freq)


# Set Comprehensions
# {expression for item in iterale}

# unique_chars = {ch for ch in 'Hello world'}
# print(unique_chars)

age = 18
status = 'Adult' if age>=18 else 'Child' # Ternary Expression
# print(status)

# o = [print(i) for i in range(10)]
# print(o)

# is_even = lambda x: x%2==0

# print(is_even(23458))


data=  ['a','b','c']

mapped = {i:val for i,val in enumerate(data)}
print(mapped)



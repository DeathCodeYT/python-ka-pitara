

def add(*args):
    return sum(args)

def greet(name):
    return f"Hello, {name}"

def square(n):
    return n**2

age = 66

print(f"From Utility: {__name__=}")
if __name__ == "__main__":
    print(age)
    print(add(234,453,6,6))
    print(square(56))


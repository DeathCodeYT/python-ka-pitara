

# print("Hello, %s! you are %d years old."%("Ravi",25))
# print("Hello, {}! you are {age} years old.".format("Ravi",age=25))
# print("Hello, {0}! you are {1} years old. {0} again".format("Ravi",25))
name = "Ravi"
age = 25
# print(f"Hello {name}! you are {age} year old.")

# s = "{:.2f}".format(3.14159)
s = "{:>10}".format("Hello")
# print(s)
pi = 3.14159
person = {"name": "Ravi", "age": 25}
# print(f"{person["name"]} is {person["age"]} years old")

# print(f"{pi:.2f}")

# print(f"{"Hello":>10}")
# print(f"{"Hi":<10}")
# print(f"{"Bye":^10}")
# print(f"{100000000:,}")

# users = [{"name":"Amit","score":88.455},{"name":"Sahil","score":73.765}]
# for user in users:
#     print(f"{user['name']:10} | {user['score']:>6.2f}")

print(f""" Ye bhi ek string hai {45.2345235:.2f}""")
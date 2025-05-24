


li = [1,2,3,4,5,6,"hello",False]


# for item in li:
#     print(item)
# for i in range(501):
#     print(i)

# count = 0
# while count <= 5:
#     print(count)
#     count += 1

# password = ""
# while password != "deathcode":
#     password = input("Enter Password:")
# print("Access Granted✅")


user = {
    "name":"Death",
    "age":45,
    'channel':"Death Code"
}

# for item in user.keys():
#     print(user[item])
# for a,b in user.items():  
#     print(a,"=",b)

# Break => loop ko turant rok deta hai, Continue => Current iteration skip krdeta hai, Pass=> placeholder (kuch nhi krta)

# for i in range(11):
#     if i == 5:
#         break
#     print(i)

# for i in range(10):
#     if i == 2:
#         continue
#     print(i)

# for i in range(5):
#     pass

# for i in range(1,11):
#     print("2 X",i,"=",2*i)

for i in range(1,4):
    for j in range(1,11):
        print(i , "X" , j , "=" , i*j)
    print()
    print("----------------------")
    print()

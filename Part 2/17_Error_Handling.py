# print("COde started")

# try:
#     n = int(input("Enter a number: "))
#     c = 45/n
#     print(c)
# except (ZeroDivisionError,ValueError):
#     print("Invalid number OR ZeroDivision error")
# except Exception as e:
#     print("Error: ",e)



# print("Important code")



# try:
#     file = open('data.txt','r')
#     # file operation
#     c = 4/0
# except Exception as e:
#     print("Error:",e)
# finally:
#     print("Cleaning up resources")
#     file.close()

# print(file.read())


# def set_age(age):
#     if age < 0:
#         raise ValueError("Age Can't be negative")
#     print("Age set to:",age)

# try:
#     set_age(-7)
# except Exception as e:
#     print("Error:",e)


# class TooYoungError(Exception):
#     pass

# def register(age):
#     if age<15:
#         raise TooYoungError("You must be 15+ to register.")
#     print("Registerd")


# try:
#     register(6)
# except TooYoungError as e:
#     print(e)


# File Upload System
# try:
#     upload_file('profil.png')
# except FileSizeLimitError as e:
#     print("Error:",e)

# API Intergration
# try:
#     data = fetch_data()
# except Exception as e:
#     print("server error")

def demo_return_and_finally():
    try:
        4/0
        return "No error occured"
    except Exception as e:
        return e
    finally:
        print("important code")

print(demo_return_and_finally())

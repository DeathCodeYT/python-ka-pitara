
# f = open("tt.txt","r")

# print(f.readline())

# f.close()

# f = open("dc.txt","w")
# f.write("\np = DeathCode")
# f.close()

# f = open("cc.txt",'r')

# print(f.read())
# print("------------------------------------")
# f.seek(0)
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.seek(0)
# print(f.readlines())

# [print(line) for no,line in enumerate(f.readlines()) if no<6]

# f.close()



# f = open("data.txt",'w')
# f.write("Welcome to DeathCode\n")
# f.write("Subscribe now\n")
# f.close()

# f = open("data.txt",'a')
# f.write("More Content....\n")
# f.close()


# with open('data.txt','r') as f:
#     print(f.read())

from datetime import datetime
# with open("log.txt",'a') as log:
#     log.write(f"{datetime.now()} - Process Started\n")

# user = input("Enter your name:")
# with open("data.txt",'a') as f:
#     f.write(f"{user}\n")

# import json
# with open("sample.json",'r') as f:
#     data = json.load(f)
#     print(data[1]['color'])

def log(message):
    with open("log.txt",'a') as l:
        l.write(f"{datetime.now()} - {message}\n")

log("someone subscribed")
log("someone Comment on Python 11th part")


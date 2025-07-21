# with open('data.txt','r') as f:
#     pass

# class MyContextManager:
#     def __init__(self,filepath,mode='r'):
#         self.filepath = filepath
#         self.mode = mode

#     def __enter__(self):
#         self._file = open(self.filepath,self.mode)
#         return self._file
    
#     def __exit__(self,exc_type,exc_value,traceback):
#         print("Exiting the context...")
#         if exc_type:
#             print(f"Exception Handled: {exc_value}")
#         self._file.close()
#         print("Resource Released")

# m1 = MyContextManager('data.txt')

# with m1 as res:
#     for line in res:
#         print(line)
#     x = 10/0


# import sqlite3

# with sqlite3.connect('example.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
#     cursor.execute("INSERT INTO users VALUES (1,'Ravi')")
#     conn.commit()


# from threading import Lock

# lock = Lock()

# with lock:
#     print("Res is locked")

# from contextlib import contextmanager

# @contextmanager
# def open_file(file,mode='r'):
#     f = open(file,mode)
#     try:
#         yield f
#     finally:
#         f.close()

# with open_file("data.txt") as f:
#     print(f.readline())
#     x = 10/0


with open('data.txt') as f1, open('cc.txt') as f2:
    print(f1.readlines())
    print(f2.readlines())
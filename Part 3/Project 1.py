# Object Inspector
import ast
import sys

def convert_to_python_object(user_input):
    try:
        return ast.literal_eval(user_input)
    except:
        return user_input

def is_mutable(obj):
    mutable_types = (list,dict,set,bytearray)
    return isinstance(obj,mutable_types)

def object_inspector(obj):
    print("\n🔎 Object Inspection Result:")
    print("-"*40)
    print(f"📌 Type         : {type(obj)}")
    print(f"📌 Memory ID    : {id(obj)}")
    print(f"📌 Size (bytes) : {sys.getsizeof(obj)}")
    
    if is_mutable(obj):
        print(f"📌 Mutablity    : Mutable ✅")
    else:
        print(f"📌 Mutablity    : Immutable 🔒")
    print("-"*40)


print("🧠 Welcome to Object Inspector 🧠")
user_input = input("Enter any Object (e.g. 42, 'hello',[1,2,3],{1:'a'},{1,2,3,4}):\n")

obj = convert_to_python_object(user_input)
object_inspector(obj)

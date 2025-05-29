# Function Call Stack Visualizer

stack_depth = 0

def func3():
    global stack_depth
    stack_depth += 1
    print(" "*stack_depth+f"➡️ Entering Func3 (stack depth: {stack_depth})")
    print(" "*stack_depth+"Doing work in func3")
    print(" "*stack_depth+f"⬅️ Exiting Func3 (stack depth: {stack_depth})")
    stack_depth -= 1

def func2():
    global stack_depth
    stack_depth += 1
    print(" "*stack_depth+f"➡️ Entering Func2 (stack depth: {stack_depth})")
    func3()
    print(" "*stack_depth+f"⬅️ Exiting Func2 (stack depth: {stack_depth})")
    stack_depth -= 1

def func1():
    global stack_depth
    stack_depth += 1
    print(" "*stack_depth+f"➡️ Entering Func1 (stack depth: {stack_depth})")
    func2()
    print(" "*stack_depth+f"⬅️ Exiting Func1 (stack depth: {stack_depth})")
    stack_depth -= 1


func1()


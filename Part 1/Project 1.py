# 1. Simple CLI Calculator
history = []

def calculate(num1,num2,operator):
    match operator:
        case '+': 
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case _:
            return None

    

def printHistory():
    print("\n---------History----------")
    for h in history:
        print("=>",h)
    print("--------------------------\n")


while True:
    print("\nType 'exit' to quit or 'history' to view previous calculations.")
    n1 = input("Enter 1st number:")

    if n1 == "exit":
        break
    elif n1 == "history":
        printHistory()
        continue

    n2 = input("Enter 2nd number:")
    if n2 == "exit":
        break
    elif n2 == "history":
        printHistory()
        continue

    operator = input("Enter Operation(+,-,*,/):")
    if operator == "exit":
        break
    elif operator == "history":
        printHistory()
        continue

    result = calculate(int(n1),int(n2),operator)
    if result:
        r = f"{n1}{operator}{n2} = {result}"
        # Store history
        history.append(r)
        print(r)
    else:
        print("Invalid Input, Please Try Again!")

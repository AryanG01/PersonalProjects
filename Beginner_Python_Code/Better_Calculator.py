num1 = float(input("Enter the First number: "))
OP = input("Enter the tpye of Operator: ")
num2 = float(input("Enter the Second number: "))

def Calculator(num1,OP, num2):
    if OP == "+":
        return num1 + num2
    elif OP == "-":
        return num1 - num2
    elif OP == "/":
        return num1 / num2
    elif OP == "*":
        return num1 * num2
    else:
        return "Invalid Operator"

print(Calculator(num1, OP, num2))








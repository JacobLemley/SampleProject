#float() converts input number into a float
num1 = float(input("Enter first number m8: "))
op = input("Enter Operator: ")
num2 = float(input("Enter second number m8: "))

if op == "+" :
    print(num1 + num2)
elif op == "-" :
    print(num1 - num2)
elif op == "/" :
    print(num1 / num2)
elif op == "*" :
    print(num1 * num2)
else :
    print("invalid operator you cunt")

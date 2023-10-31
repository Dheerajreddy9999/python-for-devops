import sys

def add(num1,num2):
    a = num1+num2
    return a

def sub(num1,num2):
    s = num1-num2
    return s

def mul(num1,num2):
    m = num1 * num2
    return m

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])


if operation == "add":
    print(add(num1,num2))
elif operation == "sub":
    print(sub(num1,num2))
elif operation == "mul":
    print(mul(num1,num2))
else:
    print("error")


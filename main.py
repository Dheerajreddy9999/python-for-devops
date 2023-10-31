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

num1 = sys.argv[0]
num2 = sys.argv[1]

x=add(num1,num2)
print(x)

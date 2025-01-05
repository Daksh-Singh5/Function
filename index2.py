num1 = float(input("Enter your number: "))
num2 = float(input("Enter your second number: "))
operator =input("Enter + to add, - to subtract ,x to multiply, / to divide,xx for power(22 for Square root and 33 for cube root) and // for remainder: ")
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a//b
def power(a,b):
    return a**b
def remainder(a,b):
    return a%b



if operator == "+":
    ans = add(num1,num2)
elif operator == "-":
    ans = subtract(num1,num2)
elif operator == "x":
    ans = multiply(num1,num2)
elif operator == "/":
    ans = divide(num1,num2)
elif operator == "xx":
    ans = power(num1,num2)
elif operator == "//":
    ans = remainder(num1,num2)
elif operator == "22":
    ans = power(num1,0.5)
elif operator == "33":
    ans = power(num1,(1/3))


print(ans)


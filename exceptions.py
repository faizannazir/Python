import sys
try:
    x=int(input("Enter value of x: "))
    y= int(input("Enter value of y: "))
except ValueError:
    print("Please enter integer numbers only. ")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x}/{y} = {result}")
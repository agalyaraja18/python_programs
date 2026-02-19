import calculator as c
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
op=input("Enter operation (add, sub, mul, div):")
if op=="add":
    print(c.add(a+b))
elif op=="sub":
    print(c.sub(a,b))
elif op=="mul":
    print(c.mul(a,b))
elif op=="div":
    print(c.div(a,b))
else:
    print("Invalid operation")
def apply_twice(func,x):
    return func(func(x))
def square(n):
    return n**2
def cube(n):
    return n**3
n=int(input("Enter a number:"))
print(apply_twice(square,n))
print(apply_twice(cube,n))
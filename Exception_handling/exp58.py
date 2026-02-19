numbers = [10, 5, 0, 20, 4, 0]

for num in numbers:
    try:
        result = 100 / num
        print(f"100 / {num} = {result}")
    except ZeroDivisionError:
        print(f"Cannot divide by zero for value: {num}")
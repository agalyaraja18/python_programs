a = list(map(int, input("Enter the elements for 1st list:").split()))
b = list(map(int, input("Enter the elements for 2nd list:").split()))
result = []
i = 0
while i < len(a) and i < len(b):
    result.append(a[i])
    result.append(b[i])
    i += 1
print(result)
